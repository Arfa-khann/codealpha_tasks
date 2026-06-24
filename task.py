import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://quotes.toscrape.com/page/{}/"

with open("quote.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tag"])

    for page in range(1, 7):

        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        # print("Page:", page, "quotes:", len(quotes))  

        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text

            tags = q.find_all("a", class_="tag")
            tag = ", ".join([t.text for t in tags])

            writer.writerow([text, author, tag])

print("Done ✅")