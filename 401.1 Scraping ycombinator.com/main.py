#SCRAPING https://news.ycombinator.com/news
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.a.getText() #gets just the text
article_link = article_tag.a.get("href") #gets just the link
article_upvote = soup.find(name="span", class_="score").getText()
