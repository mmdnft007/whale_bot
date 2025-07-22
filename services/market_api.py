import httpx

async def is_valid_symbol(symbol: str) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
            response = await client.get(url)
            return response.status_code == 200
    except Exception:
        return False

async def get_symbol_analysis(symbol: str) -> str:
    try:
        async with httpx.AsyncClient() as client:
            url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol.upper()}"
            response = await client.get(url)
            data = response.json()

            price = float(data['lastPrice'])
            percent_change = float(data['priceChangePercent'])
            volume = float(data['volume'])

            signal = ""
            if percent_change > 1.5:
                signal = "📈 احتمال روند صعودی (Long)"
            elif percent_change < -1.5:
                signal = "📉 احتمال روند نزولی (Short)"
            else:
                signal = "🔄 وضعیت نوسانی یا خنثی"

            return (
                f"📊 تحلیل نماد: {symbol}\n"
                f"قیمت فعلی: {price} USDT\n"
                f"تغییرات ۲۴ساعته: {percent_change}%\n"
                f"حجم معاملات ۲۴ساعته: {volume:.2f}\n\n"
                f"📌 سیگنال احتمالی: {signal}"
            )
    except Exception as e:
        return f"❌ خطا در دریافت اطلاعات: {e}"
