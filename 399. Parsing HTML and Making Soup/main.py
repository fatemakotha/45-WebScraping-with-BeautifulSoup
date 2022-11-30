from bs4 import BeautifulSoup
import lxml

#PART 1
print("PART 1: Opening and reading HTML file and creating a soup object to get hold of everything inside the HTML document:\n")
with open("website.html", encoding="utf8") as file: #without mentioning the encoding, the file will not open
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser") #passing in the file that is read as contents, the PARSER,

#PART 2
print("PART 2: Getting hold of entire document or first <h1> or first <p> or first <a> tags\n")
print(soup.title) #<title>Fatema's Personal Site</title>
print(soup.title.name) #title
print(soup.title.string) #Fatema's Personal Site
# print(soup) #PRINTS:whole document
# print(soup.prettify()) #INDENTS all in HTML file
print(soup.a) #prints first p

#PART 3
print("PART 2: Getting hold of ALL <h1> or <p> or <a> tags\n")
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags) #[<a href="https://www.northsouth.edu/">North South University</a>, <a href="hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]