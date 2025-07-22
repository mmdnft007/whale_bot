from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from services.market_api import get_symbol_analysis, is_valid_symbol

async def symbol_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("لطفاً نماد ارز را به صورت صحیح وارد کنید. مثال: /analyze BTCUSDT")
        return

    symbol = context.args[0].upper()

    is_valid = await is_valid_symbol(symbol)
    if not is_valid:
        await update.message.reply_text(f"نماد {symbol} در بازار یافت نشد. لطفاً نماد معتبری وارد کنید.")
        return

    await update.message.reply_text(f"⏳ در حال تحلیل {symbol} ... لطفاً صبر کنید...")

    try:
        analysis_result = await get_symbol_analysis(symbol)
        await update.message.reply_text(analysis_result)
    except Exception as e:
        await update.message.reply_text(f"❌ خطا در تحلیل نماد: {e}")
