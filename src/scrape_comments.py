# MANAGE ENVIRONNEMENT
import re
import requests
from bs4 import BeautifulSoup


def comments_scraping(url: str, regex_pattern_class: str, html_tag: str) -> list:
    """scrape comments from the supplied url, regex pattern class and html tag"""

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    regex = re.compile(regex_pattern_class)
    results = soup.find_all(html_tag, {'class': regex})

    if len(results) == 0:
        print()
        print("No match found ❌")

    else:
        print()
        print("Matches found ✅")
        comments = [result.get_text() for result in results]
        print(f'{len(comments)} comments were recovered')

        return comments
