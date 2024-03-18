import requests
import datetime as dt


today = dt.date.today()
yesterday = today - dt.timedelta(days=3)
day_before_yesterday = today - dt.timedelta(days=4)

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

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_api_params = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": STOCK,
    "apikey": stock_api_key
}


def get_news():
    pass


stock_results = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={stock_api_key}")
stock_results.raise_for_status()
print(stock_results.json())
stock_data = stock_results.json()
print(stock_data["Time Series (Daily)"])
last_day_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["1. open"])
two_days_before_price = float(stock_data["Time Series (Daily)"][str(day_before_yesterday)]["1. open"])
price_diff = last_day_price - two_days_before_price
if price_diff > 0:
    print("stock at peak")
    percentage_difference = round(price_diff / last_day_price * 100, 2)
    print(f"Increased by {percentage_difference}")
    get_news()
elif price_diff < 0:
    print("stock at down")
    percentage_difference = round(price_diff / two_days_before_price * 100, 2)
    print(f"Decreased by {percentage_difference}")
    get_news()
elif price_diff == 0:
    print("stock at level")

print("###########################################")
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_api_params = {
    "country": "in",
    "apiKey": news_api_key,
    "category": "business",
}

# headlines = requests.get(url=f"https://newsapi.org/v2/top-headlines", params=news_api_params)
# headlines.raise_for_status()
# print(headlines.json())


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

