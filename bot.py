import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN", "").strip()⁠

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm alive on Render")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You said: " + update.message.text)

async def main():
    # 1. Build the app
    app = Application.builder().token(TOKEN).build()
    
    # 2. Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    
    # 3. Initialize and run
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    # Keep the bot running until the process is interrupted
    try:
        await asyncio.Event().wait()
    finally:
        # This part runs when the bot is stopped, preventing the RuntimeError
        await app.updater.stop()
        await app.stop()
        await app.shutdown()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
