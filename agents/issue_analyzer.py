import requests
from bs4 import BeautifulSoup

def extract_issue(issue_url):
    response = requests.get(issue_url)

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    body = soup.get_text()

    return {
        "title": title,
        "description": body[:5000]
    }