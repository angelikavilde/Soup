from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import re


def get_soup_html(website) -> 'BeautifulSoup':
    """Get Soup of the website"""
    html = urlopen(website).read()
    return BeautifulSoup(html, "html.parser")


def get_bbc_recipe_info(search: str) -> None:
    """"""
    url = f"https://www.bbcgoodfood.com/search?q={search}"
    failed_page_count = 0; page_count = 1
    text_page = ""

    while failed_page_count < 5:
        soup = get_soup_html(url)
        all_matching_divs = soup.find_all("div", {"class" : "card__section card__content"})
        all_content_with_links = [(div.find("a", {"data-component" : "Link"})) for div in all_matching_divs]
        recipe_links = {link.text : link.get("href") for link in all_content_with_links if link.get("href").startswith("/")}

        for title, link in recipe_links.items():
            full_link = f"https://www.bbcgoodfood.com{link}"
            soup = get_soup_html(full_link)
            ingredients = soup.find_all("li", {"class" : "pb-xxs pt-xxs list-item list-item--separator"})
            method = soup.find("ul", {"class" : "grouped-list__list list"})
            text_page += ("--------------------- \n")
            text_page += title.replace("App only", "").replace(
                    ". This is a premium piece of content available to registered users.", "") + link + "\n"

            for ingredient in ingredients:
                text_page += ingredient.text + "\n"
            text_page += re.sub(r"(STEP \d+)", r"\1: ", method.text) + "\n"

        if not recipe_links:
            failed_page_count += 1

        page_count += 1
        url += f"&page={page_count}"
    return text_page


if __name__ == "__main__":

    #! Disabled SSL verification
    ssl._create_default_https_context = ssl._create_unverified_context
    food = "yellow"
    food_data = get_bbc_recipe_info(food)
    with open("data.txt", "w") as f:
        f.write(food_data)
    # findings: reads up to 60 food items without scrolling
