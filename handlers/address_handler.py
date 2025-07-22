from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from services.etherscan_api import analyze_wallet

async def wallet_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("📌 لطفاً آدرس ولت رو به صورت زیر وارد کن:\n\n/wallet 0x1234...abcd")
        return

    address = context.args[0]

    if not address.startswith("0x") or len(address) != 42:
        await update.message.reply_text("❗️ آدرس ولت معتبر نیست. آدرس باید با `0x` شروع بشه و 42 کاراکتر باشه.")
        return

    await update.message.reply_text("⏳ در حال تحلیل ولت... لطفاً صبر کن.")

    result = await analyze_wallet(address)
    await update.message.reply_text(result)

# هندلر برای اضافه کردن به bot در main.py
wallet_command_handler = CommandHandler("wallet", wallet_handler)
