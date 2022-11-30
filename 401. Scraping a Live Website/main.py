from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text) #prints all the HTML code
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title) #<title>Hacker News</title>
print(soup.title.text) #Hacker News
print("----------------------------------------------------------------------------")

article_tag = soup.find(name="span", class_="titleline")
print(article_tag) #<span class="titleline"><a href="https://btm.qva.mybluehost.me/building-arbitrary-life-patterns-in-15-gliders/">In Game of Life any buildable pattern can be constructed by colliding 15 gliders</a><span class="sitebit comhead"> (<a href="from?site=mybluehost.me"><span class="sitestr">mybluehost.me</span></a>)</span></span>
article_tag = article_tag.a
print(article_tag)#<a href="https://btm.qva.mybluehost.me/building-arbitrary-life-patterns-in-15-gliders/">In Game of Life any buildable pattern can be constructed by colliding 15 gliders</a>
print("----------------------------------------------------------------------------")

article_text = article_tag.getText() #gets just the text
print(article_text) #In Game of Life any buildable pattern can be constructed by colliding 15 gliders
article_link = article_tag.get("href") #gets just the link
print(article_link) #https://btm.qva.mybluehost.me/building-arbitrary-life-patterns-in-15-gliders/
print("----------------------------------------------------------------------------")

article_upvote = soup.find(name="span", class_="score")
print(article_upvote)
article_upvote = article_upvote.getText()
print(article_upvote)
print("----------------------------------------------------------------------------")