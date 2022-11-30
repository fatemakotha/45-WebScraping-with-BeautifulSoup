import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

movies_page = requests.get(URL)
movies_page = movies_page.text
# print(movies_page)

soup = BeautifulSoup(movies_page, "html.parser")
# print(soup)

movie_list = []

titles = soup.find_all(name="h3", class_="title")
print(titles)
for each_item in titles:
    mov_name_num = each_item.text
    movie_list.append(mov_name_num)

print(movie_list) #prints list from 100 to 0
#Reversing the list starting from 1-100
movie_list.reverse()
# or : movies = movie_list[::-1]
print(movie_list)

with open("Top 100 movies list", 'w') as f:
    for each_movie in movie_list:
        f.write(each_movie)
        f.write("\n")