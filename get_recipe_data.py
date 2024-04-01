from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

#! Disabled SSL verification
ssl._create_default_https_context = ssl._create_unverified_context


def get_soup_html(website) -> 'BeautifulSoup':
    """Get Soup of the website"""
    html = urlopen(website).read()
    return BeautifulSoup(html, "html.parser")


if __name__ == "__main__":
    search = "chocolate"
    url = f"https://www.bbcgoodfood.com/search?q={search}"
    soup = get_soup_html(url)
    page_html_scraped = soup.find_all("div", {"class": "card__section card__content"})
    x = 0
    for div in page_html_scraped:
        g = div.find("a", {"data-component":"Link"})
        link = g.get("href")
        x += 1
        if not link.startswith("/"):
            continue
        if x >= 5:
            break
        full_link = f"https://www.bbcgoodfood.com{link}"
        soup = get_soup_html(full_link)
        ingredients = soup.find_all("li", {"class":"pb-xxs pt-xxs list-item list-item--separator"})
        print("---------------------")
        print(g.text, link)
        for ingredient in ingredients:
            print(ingredient.text)