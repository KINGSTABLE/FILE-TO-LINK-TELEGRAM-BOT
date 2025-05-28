# FILE-TO-LINK-TELEGRAM-BOT
A Telegram bot that uploads files to Gofile.io and returns a temporary download link with Zeabur sponsorship integration



# 📁 File-to-Link Telegram Bot

This is an open-source Telegram bot that lets users send files and receive instant download links via [Gofile.io](https://gofile.io). Designed for simplicity and speed, the bot also proudly displays sponsorship content from [Zeabur](https://zeabur.com).

---

## 🚀 Features

- Accepts file uploads up to (2–4 GB)
- Uploads files to Gofile.io cloud storage
- Returns a secure download link to the user
- Shows a Zeabur sponsorship banner with each link
- Queue system for handling multiple uploads
- Works with documents, photos, videos, and audio files

---

## Prerequisites
To run the bot, you’ll need:
- **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/).
- **Dependencies**:
  - `pyrogram`: For connecting to Telegram.
  - `aiohttp`: For uploading files to Gofile.io.
  - Optional: `python-magic` (for better file type detection on some systems).
- **API Credentials**:
  - Telegram Bot Token from [BotFather](https://t.me/BotFather).
  - Gofile.io API Token from [Gofile.io](https://gofile.io).
  - Telegram API ID and Hash from [my.telegram.org](https://my.telegram.org).
- **System**:
  - A computer or server with internet access.
  - A `./downloads/` folder for temporary file storage.
- **Hosting** (optional): A platform like [Zeabur](https://zeabur.com) for online deployment.

## Setup Instructions
Follow these steps to get the bot up and running. No coding experience? No problem! We’ll guide you through each step.

1. **Get the Code**:
   - Clone the repository to your computer.
     ```bash
     git clone https://github.com/KINGSTABLE/FILE-TO-LINK-TELEGRAM-BOT.git
     cd FILE-TO-LINK-TELEGRAM-BOT
     ```
   - **No Git?** Download the code as a ZIP from the GitHub page and unzip it.

2. **Install Python**:
   - Make sure Python 3.8 or higher is installed. Check by running:
     ```bash
     python --version
     ```
   - If not installed, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your system (Windows, macOS, or Linux).

3. **Install Required Libraries**:
   - Open a terminal or command prompt in the `file-to-link-bot` folder.
   - Install all required libraries using the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```
   - **Windows Users (Optional)**: For better file type detection, install `python-magic`:
     ```bash
     pip install python-magic
     ```
   - **Troubleshooting**: If `pip` doesn’t work, try `pip3` or ensure Python is added to your system’s PATH. If you see errors, make sure you’re in the correct folder with `requirements.txt`.

4. **Set Up API Credentials**:
   - Open the `file_to_link_bot.py` file in a text editor (like Notepad or VS Code).
   - Replace these values with your own:
     - `API_ID`: Your Telegram API ID from [my.telegram.org](https://my.telegram.org).
     - `API_HASH`: Your Telegram API Hash from [my.telegram.org](https://my.telegram.org).
     - `BOT_TOKEN`: Your bot token from [BotFather](https://t.me/BotFather).
     - `GOFILE_API_TOKEN`: Your token from [Gofile.io](https://gofile.io).
   - **How to Get Credentials**:
     - **Telegram**: Log in to [my.telegram.org](https://my.telegram.org), create an app, and copy the API ID and Hash. Then, message [BotFather](https://t.me/BotFather) on Telegram, use `/newbot`, and follow the prompts to get a bot token.
     - **Gofile.io**: Sign up at [Gofile.io](https://gofile.io), go to account settings, and generate an API token.
   - Save the file after updating.

5. **Create a Downloads Folder**:
   - The bot needs a folder to temporarily store files. Create it in the `file-to-link-bot` folder:
     ```bash
     mkdir downloads
     ```
   - **Windows Users**: You can also create a folder named `downloads` manually in the project directory.

6. **Run the Bot Locally**:
   - In the terminal, run:
     ```bash
     python file_to_link_bot.py
     ```
   - If it works, the bot will start and connect to Telegram. Test it by messaging your bot on Telegram with `/start`.
   - **Troubleshooting**: Ensure all credentials are correct. If you see errors, double-check the API tokens and installed libraries.

7. **Deploy to Zeabur (Optional)**:
   - Want to run the bot online 24/7? Use [Zeabur](https://zeabur.com) for easy deployment!
   - Sign up at [Zeabur](https://zeabur.com) and create a new project.
   - Upload the repository or connect it directly from GitHub.
   - Set these environment variables in Zeabur’s dashboard:
     - `API_ID`: Your Telegram API ID.
     - `API_HASH`: Your Telegram API Hash.
     - `BOT_TOKEN`: Your Telegram Bot Token.
     - `GOFILE_API_TOKEN`: Your Gofile.io API Token.
   - Deploy the project and follow Zeabur’s guide for Python apps.
   - **Why Zeabur?** It’s fast, reliable, and perfect for hosting bots like this one!

## Usage
1. Open Telegram and start the bot by sending `/start`.
2. Send a file (document, video, audio, or photo) up to (2–4 GB).
3. Wait for the bot to upload the file to Gofile.io.
4. Get a secure download link in the chat, like this:
   ```
   ✅ File uploaded successfully! Here's your link: https://gofile.io/d/XXXXXX
   🌟 Proudly Powered by Zeabur - Your go-to platform for seamless app deployment: https://zeabur.com 🌟
   ```
5. Use `/help` for detailed instructions.

  ---



## 🤝 Sponsorship
 This bot is proudly sponsored by Zeabur, a powerful platform for deploying modern web services.


 Every download link shared includes a custom message:

🌟 Proudly Powered by Zeabur - Your go-to platform for seamless app deployment 🌟
---


## ✨ Author
Made with ❤️ by Harsh Sharma

- **Developer**: Harsh Sharma
- **Telegram**: [@KINGS_TABLE](https://t.me/KINGS_TABLE)


## 📜 License
This project is licensed under the MIT License.






