# api.py
import requests
from bs4 import BeautifulSoup

# Fetch articles from an example news API
def fetch_news_api(company_name):
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey=09f3680f7ad443cba0f978a64d1ee81a"
    response = requests.get(url)
    articles = []
    
    if response.status_code == 200:
        data = response.json()
        for item in data['articles']:
            article_info = {
                'title': item['title'],
                'summary': item['description'] if item['description'] else "No summary available",
                'url': item['url']
            }
            articles.append(article_info)
    else:
        print(f"Error fetching news. Status code: {response.status_code}")
    
    return articles
