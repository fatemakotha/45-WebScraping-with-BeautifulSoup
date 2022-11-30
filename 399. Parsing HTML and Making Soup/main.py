from bs4 import BeautifulSoup
import lxml

#PART 1: Opening and reading HTML file and creating a soup object to get hold of everything inside the HTML document:
with open("website.html", encoding="utf8") as file: #without mentioning the encoding, the file will not open
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser") #passing in the file that is read as contents, the PARSER,

#PART 2: Getting hold of entire document or first <h1> or first <p> or first <a> tags
print(soup.title) #<title>Fatema's Personal Site</title>
print(soup.title.name) #title
print(soup.title.string) #Fatema's Personal Site
# print(soup) #PRINTS:whole document
# print(soup.prettify()) #INDENTS all in HTML file
print(soup.a) #prints first p

#PART 3: Getting hold of ALL <h1> or <p> or <a> tags\
print("\n")
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags) #[<a href="https://www.northsouth.edu/">North South University</a>, <a href="hobbies.html">My Hobbies</a>, <a href="contact.html">Contact Me</a>]

#PART 4: How to get hold of all anchor tags"
print("\n")
for tag in all_anchor_tags:
    print(tag.getText()) #gets the text in all 3 of the anchor tags
print("\n")
for tag in all_anchor_tags:
    print(tag.get("href")) #prints just the links and not the text

#Part 5: Search using attribute name using HTML names
heading = soup.find(name="h1", id="name") #has a name of h1 and an id of name
print(heading)#<h1 id="name">Fatema Alam</h1>

section_heading = soup.find(name="h3", class_="heading")
print(section_heading) #<h3 class="heading">Education</h3>
print(section_heading.text) #Education
print(section_heading.name) #h3
print(section_heading.get("class")) #['heading']


#Part 6: Narrowing down the find using CSS selectors
company_url = soup.select_one(selector="p a")
print(company_url) #<a href="https://www.northsouth.edu/">North South University</a>

all_company_urls = soup.select(selector="p a")
print(all_company_urls) #prints all urls that are inside an a and a p

name = soup.select_one(selector="#name")
print(name) #<h1 id="name">Fatema Alam</h1>

headings = soup.select(".heading")
print(headings) #[<h3 class="heading">Education</h3>, <h3 class="heading">Other Pages</h3>]