from numpy import diff
import requests 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "Y5SSEIPLSA500ARN"
NEWS_API_KEY = "4b54367b7ce94ab9ac57c6add79ab49c"


stock_params = {

    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,

}


response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]


yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)


diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)


if diff_percent > 1: 
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }

news_response = requests.get(NEWS_ENDPOINT,params=news_params)
articles = news_response.json()["articles"]


three_articles = articles[:3]
for i in three_articles: 
    print("")
    print(i["description"])