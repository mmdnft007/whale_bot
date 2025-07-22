from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات تحلیلگر نهنگ‌ها هستم. برای دیدن سیگنال‌ها از دستور /signal استفاده کن.")

start_handler = CommandHandler("start", start)
