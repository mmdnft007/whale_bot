from handlers.address_handler import wallet_command_handler
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start_handler import start_handler
from handlers.signal_handler import signal_handler
from handlers.symbol_handler import symbol_handler
# از اینجا به بعد اگر خواستی آدرس ولت هم اضافه کنیم، این هندلر رو فعال می‌کنی
# from handlers.address_handler import address_handler
from config import TELEGRAM_BOT_TOKEN

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(wallet_command_handler)


    # ثبت دستورات
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("signal", signal_handler))
    app.add_handler(CommandHandler("analyze", symbol_handler))
    # app.add_handler(CommandHandler("address", address_handler))

    print("✅ ربات با موفقیت اجرا شد.")
    await app.run_polling()

# رفع خطای asyncio در ویندوز (event loop)
import nest_asyncio
nest_asyncio.apply()

# اجرای برنامه
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
