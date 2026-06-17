import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm alive on Render")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You said: " + update.message.text)

async def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    # Make sure your MessageHandler matches your specific filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
