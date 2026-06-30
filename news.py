import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from utils import remove_html_tags


# Yahoo Finance RSS에서 뉴스 수집
def find_news(ticker):
    url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s="
    url = url + urllib.parse.quote(ticker) + "&region=US&lang=en-US"

    news_list = []

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = urllib.request.urlopen(request, timeout=10)
    text = response.read().decode("utf-8", errors="ignore")

    root = ET.fromstring(text)
    items = root.findall(".//item")

    for item in items:
        title_tag = item.find("title")
        link_tag = item.find("link")
        summary_tag = item.find("description")

        if title_tag is not None and title_tag.text is not None:
            news = {
                "title": title_tag.text,
                "link": "",
                "summary": ""
            }

            if link_tag is not None and link_tag.text is not None:
                news["link"] = link_tag.text

            if summary_tag is not None and summary_tag.text is not None:
                news["summary"] = remove_html_tags(summary_tag.text)

            news_list.append(news)

    return news_list
