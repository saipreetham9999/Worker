import requests

def get_weather(lat=37.6872, lon=-97.3301):
    """
    Fetches current weather from Open-Meteo (Free, No Key).
    Default location: Wichita, Kansas (lat=37.6872, lon=-97.3301)
    """
    try:
        # Open-Meteo API (Free, no API key required)
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            current = data.get("current_weather", {})
            return {
                "location": "Wichita, KS",
                "temperature": current.get("temperature"),
                "windspeed": current.get("windspeed"),
                "weathercode": current.get("weathercode")
            }
    except Exception as e:
        print(f"⚠️ Weather fetch failed: {e}")
    
    return None

def get_coinbase_price(pair="BTC-USD"):
    """
    Fetches crypto price from Coinbase Public API.
    """
    try:
        url = f"https://api.coinbase.com/v2/prices/{pair}/spot"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "pair": pair,
                "amount": data.get("data", {}).get("amount"),
                "currency": data.get("data", {}).get("currency")
            }
    except Exception as e:
        print(f"⚠️ Coinbase fetch failed: {e}")
    
    return None

def get_usd_to_inr():
    """
    Fetches USD to INR exchange rate from a public API.
    """
    try:
        # Using a free public API for exchange rates
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates", {})
            inr_rate = rates.get("INR")
            return {
                "from": "USD",
                "to": "INR",
                "rate": inr_rate
            }
    except Exception as e:
        print(f"⚠️ Currency fetch failed: {e}")
    
    return None

def get_crypto_news():
    """
    Fetches the latest crypto news from CoinGecko (Free, No Key).
    """
    try:
        url = "https://api.coingecko.com/api/v3/news"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("data"):
                latest_news = data["data"][0]
                return {
                    "title": latest_news.get("title"),
                    "source": latest_news.get("news_site"),
                    "url": latest_news.get("url")
                }
    except Exception as e:
        print(f"⚠️ News fetch failed: {e}")
    
    return None