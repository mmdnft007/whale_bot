from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
from services.etherscan_api import analyze_wallet


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await analyze_wallet()
    await update.message.reply_text(message)

signal_handler = CommandHandler("signal", signal)
