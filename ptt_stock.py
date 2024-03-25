"""This is python program"""
import requests
from bs4 import BeautifulSoup
#url = "網址"
url = "https://www.ptt.cc/bbs/Stock/index.html"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
}
for _ in range(5):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser" ) 

    title_tag_list = soup.select('div.title a')

    # 使用迴圈印出結果
    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc/" + title_tag["href"]
        print(title)
        print(article_url)

    url = "https://www.ptt.cc/" + soup.select('a[class="btn wide"]')[1]["href"]

    print(url) #改成下一頁的url