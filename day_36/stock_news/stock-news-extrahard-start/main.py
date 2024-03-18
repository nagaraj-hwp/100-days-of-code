import requests
import datetime as dt
from twilio.rest import Client

today = dt.date.today()
yesterday = today - dt.timedelta(days=4)
day_before_yesterday = today - dt.timedelta(days=5)

print(yesterday)
print(day_before_yesterday)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
with open("../../../ignore_dir/api_key.txt") as key_file:
    key_data = key_file.readlines()
    stock_api_key = key_data[20].strip()
    news_api_key = key_data[18].strip()
    twilio_api_key = key_data[11].strip()
    twilio_account_sid = key_data[9].strip()
    from_number = key_data[5].strip()
    to_number = key_data[7].strip()

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}


def get_news():
    pass


stock_results = requests.get(url="https://www.alphavantage.co/query", params=stock_api_params)
stock_results.raise_for_status()
print(stock_results.json())
stock_data = stock_results.json()
print(stock_data)
print(stock_data["Time Series (Daily)"])
last_day_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])
two_days_before_price = float(stock_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])
price_diff = last_day_price - two_days_before_price
percentage_difference = 0
up_down = "↔️"
if price_diff > 0:
    up_down = "🔺"
    print("stock at peak")
    percentage_difference = round(price_diff / last_day_price * 100, 2)
    print(f"Increased by {percentage_difference}")
elif price_diff < 0:
    up_down = "🔻"
    print("stock at down")
    percentage_difference = round(price_diff / two_days_before_price * 100, 2)
    print(f"Decreased by {percentage_difference}")
elif price_diff == 0:
    print("stock at level")

if percentage_difference > 4:
    get_news()


print("###########################################")
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_api_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
}

news_response = requests.get(url=f"https://newsapi.org/v2/everything", params=news_api_params)
news_response.raise_for_status()
print(news_response.json())

articles = news_response.json()["articles"][:3]
print(articles)

msg_text = [f"{STOCK}: {up_down}Headline: {article['title']}{percentage_difference}%.\nBrief: {article['description']}" for article in articles]
print(msg_text)


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
client = Client(twilio_account_sid, twilio_api_key)
for article in msg_text:
    message = client.messages.create(
        body=article,
        from_=from_number,
        to=to_number
    )
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

