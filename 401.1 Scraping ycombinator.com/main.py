#SCRAPING https://news.ycombinator.com/news
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

#Tapping into ONE in the website:
# soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="span", class_="titleline")
# article_text = article_tag.a.getText() #gets just the text
# article_link = article_tag.a.get("href") #gets just the link
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

#Tapping into ALL ENTRIES in the website:
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
print(articles)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    # print(text)
    link = soup.find(name="span", class_="titleline")
    link = link.a.get("href")
    article_links.append(link)
    # print(link)

votes = []
article_upvotes = soup.find_all(name="span", class_="score")
# print(article_upvotes)
for score in article_upvotes:
    vote = score.getText()
    # print(vote)
    vote = int(vote.split(" ")[0])
    # print(vote)
    votes.append(vote)


# print(article_texts)
# print(article_links)
print(votes)

for each_item in votes: #[109, 48, 351, 776, 57, 55, 72, 407, 135, 6, 32, 14, 120, 86, 279, 174, 274, 77, 148, 142, 99, 90, 918, 594, 120, 65, 83, 63, 85, 37]
    print(each_item)
#
largest_number = max(votes) #which is 925
largest_index = votes.index(largest_number) #which is 21

print(article_texts[largest_index])
print(article_links[largest_index])



#
# print(votes.index(max(votes))) #21
# print(article_texts[21])
# print(article_links[21])



