import os
import aiohttp
import asyncio
import mimetypes
from pyrogram import Client, filters
from pyrogram.types import Message
from queue import Queue

# Pyrogram and API Configuration
API_ID = "YOUR API ID"  # Get this from https://my.telegram.org
API_HASH = "YOUR API HASH"  # Get this from https://my.telegram.org
BOT_TOKEN = "YOUR BOT TOKEN"
GOFILE_API_TOKEN = "YOUR GOFILE API TOKEN"

# Specify the prioritized servers
PRIORITIZED_SERVERS = [
    "upload-na-phx",  # North America (Phoenix)
    "upload-ap-sgp",  # Asia Pacific (Singapore)
    "upload-ap-hkg",  # Asia Pacific (Hong Kong)
    "upload-ap-tyo",  # Asia Pacific (Tokyo)
    "upload-sa-sao",  # South America (São Paulo)
]
HEADERS = {"Authorization": f"Bearer {GOFILE_API_TOKEN}"}

# File size limit (in bytes)
MAX_FILE_SIZE = 4096 * 1024 * 1024  # 4096 MB

# Initialize Pyrogram Client
app = Client("advanced_gofile_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Initialize queues
download_queue = Queue()
upload_queue = Queue()
processing_queue = asyncio.Lock()

# Command: /start
@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text(
        "🚀 Welcome to the File-to-Link Bot! Effortlessly upload files to Gofile.io and get secure, shareable links in seconds. "
        "Send any file to get started, or use /help for more info.\n\n"
        "🌟 Proudly Powered by Zeabur - Your go-to platform for seamless app deployment: https://zeabur.com 🌟"
    )

# Command: /help
@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply_text(
        "📋 This bot lets you upload files to Gofile.io and receive secure, shareable links.\n\n"
        "How to use:\n"
        "1. Send any file (document, video, audio, or photo) up to 4096 MB.\n"
        "2. The bot will queue and upload your file to Gofile.io.\n"
        "3. You'll receive a download link once the upload is complete.\n\n"
        "Commands:\n"
        "/start - Start the bot and get a welcome message.\n"
        "/help - Show this help message.\n\n"
        "Made possible by Zeabur: https://zeabur.com"
    )

# File Upload Handler
@app.on_message(filters.document | filters.video | filters.audio | filters.photo)
async def add_to_queue(client: Client, message: Message):
    # Determine file size
    file_size = 0
    if message.document:
        file_size = message.document.file_size
    elif message.video:
        file_size = message.video.file_size
    elif message.audio:
        file_size = message.audio.file_size
    elif message.photo:
        file_size = message.photo.file_size

    # Check file size
    if file_size > MAX_FILE_SIZE:
        await message.reply_text(
            f"File size exceeds the 4096 MB limit. Your file is {file_size / (1024 * 1024):.2f} MB."
        )
        return

    # Add the file to the download queue
    download_queue.put(message)
    await message.reply_text(
        "Your file has been added to the queue! It will be processed shortly."
    )

    # Process the queue
    asyncio.create_task(process_queue(client))

async def process_queue(client: Client):
    async with processing_queue:
        # Process the download queue
        while not download_queue.empty():
            message = download_queue.get()
            await process_file(client, message)

async def process_file(client: Client, message: Message):
    # Notify the user that the upload is starting
    await message.reply_text("Processing your file. Please wait...")

    # Step 1: Get the file name and handle missing attributes
    if message.document:
        file_name = message.document.file_name or "file"
    elif message.video:
        file_name = message.video.file_name or "video.mp4"
    elif message.audio:
        file_name = message.audio.file_name or "audio.mp3"
    elif message.photo:
        # Photos don’t have a file_name attribute, assign a default name
        file_name = f"photo_{message.photo.file_id}.jpg"
    else:
        file_name = "unknown_file"

    # Step 2: Download the file from Telegram
    file_path = await client.download_media(message, file_name=f"./downloads/{file_name}")

    try:
        # Add the file to the upload queue
        upload_queue.put(file_path)

        # Process the upload queue
        while not upload_queue.empty():
            file_path = upload_queue.get()
            await upload_file_to_gofile(message, file_path)

    finally:
        # Clean up the downloaded file from the server
        if os.path.exists(file_path):
            os.remove(file_path)

async def upload_file_to_gofile(message: Message, file_path: str):
    try:
        # Determine MIME type
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type is None:
            mime_type = "application/octet-stream"  # Default MIME type

        # Step 2: Attempt to upload the file to each prioritized server
        for server in PRIORITIZED_SERVERS:
            try:
                async with aiohttp.ClientSession() as session:
                    with open(file_path, "rb") as f:
                        form_data = aiohttp.FormData()
                        form_data.add_field("file", f, filename=os.path.basename(file_path), content_type=mime_type)

                        async with session.post(
                            f"https://{server}.gofile.io/uploadfile", headers=HEADERS, data=form_data
                        ) as response:
                            result = await response.json()

                # Step 3: Check if the upload was successful
                if result.get("status") == "ok":
                    download_link = result["data"]["downloadPage"]
                    await message.reply_text(
                        f"✅ File uploaded successfully! Here's your link: {download_link}\n\n"
                        "🌟 Proudly Powered by Zeabur - Your go-to platform for seamless app deployment: https://zeabur.com 🌟"
                    )
                    break  # Exit the loop after a successful upload
                else:
                    error_message = result.get("message", "An unknown error occurred.")
                    raise Exception(f"Failed on server {server}: {error_message}")

            except Exception as e:
                # Log the error and try the next server
                await message.reply_text(
                    f"Failed to upload on server {server}. Trying the next server..."
                )

        else:
            # If all servers fail
            await message.reply_text(
                "All servers failed. Please try again later."
            )

    except Exception as e:
        await message.reply_text(
            f"An error occurred while uploading your file: {str(e)}"
        )

# Run the Bot
if __name__ == "__main__":
    app.run()
