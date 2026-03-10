import requests

def get_market_news(sector):

    url = f"https://newsapi.org/v2/everything?q={sector}+india&apiKey=AIzaSyDKM0ER7NWjndvjD97y0wUyDgvka01d0zY"

    response = requests.get(url)

    if response.status_code != 200:
        return "No news data available"

    articles = response.json()["articles"][:5]

    news_summary = []

    for article in articles:
        news_summary.append(article["title"])

    return news_summary
