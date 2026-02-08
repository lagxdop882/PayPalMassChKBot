import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# --- CONFIGURATION ---
BOT_TOKEN = "8505905087:AAFNlk5FBJOXMJfxxAlE2xwC5IMMOb7M6DE"  # Paste your token from BotFather
ALLOWED_USERS = [8597415233, 987654321] # Replace with your actual User IDs (Integers, not strings)

# Enable logging to see errors in console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # Check if the user is in the allowed list
    if user_id in ALLOWED_USERS:
        await update.message.reply_text(f"✅ **Access Granted!**\n\nWelcome, Master. System is ready.")
    else:
        await update.message.reply_text(f"⛔ **ACCESS DENIED**\n\nUser ID: `{user_id}` is not authorized.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Security Check for every message
    if user_id not in ALLOWED_USERS:
        await update.message.reply_text("⛔ Access Denied. Do not touch.")
        return # Stop the function here

    # If allowed, process the message
    await update.message.reply_text(f"Processing command: {update.message.text}")

if __name__ == '__main__':
    # Build the application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    print("Bot is running...")
    application.run_polling()
