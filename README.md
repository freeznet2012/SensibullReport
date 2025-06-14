# Sensibull Automation Setup Guide

## � System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.7 or higher
- **Browser**: Microsoft Edge (recommended) or Google Chrome
- **Internet**: Stable connection for Sensibull access and Telegram API
- **Memory**: At least 4GB RAM (for PDF processing)
- **Storage**: ~100MB for dependencies + space for generated PDFs

## 📦 Required Python Packages
- `selenium>=4.15.0` - Web browser automation
- `requests>=2.31.0` - HTTP requests for Telegram API

## �🚀 Features Added
Your automation script now supports:
- ✅ **Auto-zipping** all generated PDFs
- ✅ **Telegram bot messaging** with zip file attachment
- ✅ **Configurable settings** in config.py
- ✅ **Multi-page PDF capture** with custom scaling
- ✅ **Pre-print actions** (clicking buttons, expanding sections)
- ✅ **Error handling** and recovery

## � Telegram Bot Setup

### Step 1: Create a Telegram Bot
1. Open Telegram and message **@BotFather**
2. Type `/newbot` and follow the instructions
3. Choose a name for your bot (e.g., "Sensibull Reports Bot")
4. Choose a username for your bot (must end in 'bot', e.g., "sensibull_reports_bot")
5. **Copy the bot token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Get Your Chat ID
1. **Start a chat** with your new bot (search for its username)
2. **Send any message** to your bot (e.g., "Hello")
3. Open this URL in browser: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Replace `<YOUR_BOT_TOKEN>` with your actual bot token
4. **Find your chat ID** in the response (look for `"chat":{"id":123456789}`)

### Step 3: Secure Configuration Setup
1. **Copy the example file**: 
   ```bash
   cp .env.example .env
   ```
2. **Edit the .env file** with your credentials:
   ```bash
   # Edit .env file
   TELEGRAM_BOT_TOKEN=
   TELEGRAM_CHAT_ID=
   ```
3. **Verify .env is in .gitignore** (it already is!)

### ⚠️ Security Note
- **Never commit .env file** to version control
- **Keep your bot token secret** - don't share it
- **The .gitignore file** ensures secrets won't be accidentally committed

### Old Method (Not Recommended)
```python
# DON'T DO THIS - hardcoded secrets in config.py
TELEGRAM_SETTINGS = {
    "bot_token": "your_token_here",  # This gets committed!
}
```

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.7+** installed on your system
- **Microsoft Edge** browser (script uses Edge WebDriver)
- **Internet connection** for Telegram API

### Step 1: Install Dependencies
```bash
# Option 1: Install all dependencies from requirements.txt (recommended)
pip install -r requirements.txt

# Option 2: Install packages individually
pip install selenium>=4.15.0
pip install requests>=2.31.0
```

### Step 2: WebDriver Setup
The script uses Microsoft Edge WebDriver, which should be automatically managed by Selenium 4.15+. If you encounter WebDriver issues:

1. **Check Edge version**: `edge://version/`
2. **Update Edge**: Download latest from Microsoft
3. **Alternative**: The script includes fallback to Chrome if Edge fails

### Step 3: Project Setup
1. **Download/Clone** the project files
2. **Navigate** to the project directory
3. **Test installation** (optional but recommended):
   ```bash
   python test_requirements.py
   ```
4. **Configure** Telegram settings in `config.py`
5. **Run** the script

## 🎯 Usage
1. **Configure your Telegram settings** in `config.py`
2. **Run the script**: `python sensibull_screenshot_automation.py`
3. The script will:
   - Generate all PDFs from Sensibull pages
   - Create a zip file with all PDFs
   - Send the zip file to your Telegram chat

## 📁 Output Files
- Individual PDFs: `pdfs/YYYY-MM-DD/filename.pdf`
- Merged PDF: `pdfs/YYYY-MM-DD/Sensibull_Report.pdf`  
- Zip file: `pdfs/YYYY-MM-DD/Sensibull_Report_YYYY-MM-DD.zip`

## 🔧 Troubleshooting

### Installation Issues
- **Python version**: Ensure you're using Python 3.7+ (`python --version`)
- **pip not found**: Make sure pip is installed (`python -m pip --version`)
- **Permission errors**: Use `pip install --user` or run with admin privileges
- **Virtual environment** (recommended):
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # On Windows: .venv\Scripts\activate
  pip install -r requirements.txt
  ```

### WebDriver Issues
- **Edge not found**: Install Microsoft Edge browser
- **WebDriver errors**: Update Edge to latest version
- **Permission denied**: Check if Edge is running and close it
- **Chrome fallback**: Script will try Chrome if Edge fails

### Package Specific Issues
- **Selenium errors**: Try `pip install --upgrade selenium`
- **Requests errors**: Try `pip install --upgrade requests`

### Telegram Issues
- **Bot token error**: Make sure you copied the complete token from @BotFather
- **Chat ID error**: Ensure you've sent at least one message to the bot first
- **File too large**: Telegram has a 50MB file size limit for bots
- **Bot not responding**: Check that the bot token is correct and hasn't been revoked

### General Issues
- **Internet connection**: Check your connection for Telegram API access
- **File permissions**: Ensure the script can create files in the pdfs folder
- **PDF generation**: Check console output for any PDF generation errors

## 🎉 Success!
When everything works, you'll see:
```
✅ Zip file created: pdfs/2025-06-15/Sensibull_Report_2025-06-15.zip
✅ Telegram message sent successfully!
🎉 Automation complete!
```

And you'll receive:
1. **A message** in your Telegram chat: "📊 Daily Sensibull Report for 2025-06-15 is ready!"
2. **The zip file** containing all PDFs as a document

## 💡 Pro Tips
- **Test your bot** by sending it a message first
- **Keep your bot token secure** - don't share it publicly
- **Use a private chat** with your bot for security
- **Check file sizes** - very large PDFs might exceed Telegram limits
