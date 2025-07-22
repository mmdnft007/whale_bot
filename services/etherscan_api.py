import httpx
from config import ETHERSCAN_API_KEY

ETHERSCAN_API_URL = "https://api.etherscan.io/api"

async def get_transactions(address, limit=10):
    """
    گرفتن تراکنش‌های اخیر یک آدرس ولت اتریوم
    """
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": limit,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(ETHERSCAN_API_URL, params=params)
            data = response.json()
            if data["status"] == "1":
                return data["result"]
            else:
                return []
        except Exception as e:
            print(f"خطا در دریافت تراکنش‌ها: {e}")
            return []

async def analyze_wallet(address):
    """
    تحلیل ساده از رفتار ولت بر اساس تراکنش‌ها
    """
    transactions = await get_transactions(address)
    if not transactions:
        return "❌ نتونستم تراکنشی برای این ولت پیدا کنم."

    incoming = 0
    outgoing = 0
    total_in = 0
    total_out = 0

    for tx in transactions:
        value_eth = int(tx["value"]) / 1e18  # تبدیل به ETH
        if tx["to"].lower() == address.lower():
            incoming += 1
            total_in += value_eth
        else:
            outgoing += 1
            total_out += value_eth

    result = f"📊 تحلیل ولت `{address}`:\n\n"
    result += f"✅ تراکنش‌های ورودی: {incoming} (مجموع: {total_in:.4f} ETH)\n"
    result += f"❌ تراکنش‌های خروجی: {outgoing} (مجموع: {total_out:.4f} ETH)\n"

    net = total_in - total_out
    if net > 0:
        result += f"\n💰 ولت در حال **جمع‌آوری** داراییه (Net: {net:.4f} ETH)"
    elif net < 0:
        result += f"\n📤 ولت در حال **خروج دارایی**ه (Net: {net:.4f} ETH)"
    else:
        result += f"\n⚖️ ولت وضعیت خنثی داره (Net: {net:.4f} ETH)"

    if total_in + total_out > 1000:
        result += "\n\n🐳 احتمالاً این ولت **نهنگ** هست."

    return result
