# ptt 股票版爬蟲實作
# 啟動虛擬環境 .\ptt\Scripts\activate
# 產生requirement檔案指令=> pip freeze > requirements.txt
# 關閉虛擬環境 deactivate
# 測試html網頁，新增html後，安裝live server 套件，對著檔案右鍵open with live server開啟網頁
# 爬蟲需要帶有header 中的 user agent，模擬使用的狀況
# 分為urllib.request(標準函式庫)、requests(第三方函式庫，需安裝)
# 正確寫法的輔助工具 linter
# ----------------------------------------------------------
# # 方法一: 使用urllib函式庫的request模組(標準)
# #取得網址給html字串
# # request.Request 為urllib.request 模組提供的固定用法，Request為類別

# #新宣告一個useragent，貼上網站network找到的useragent資訊
# from urllib import request

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
# }
# #url = "網址"
# url = "https://www.ptt.cc/bbs/Stock/M.1710770280.A.8D1.html"

# urllib 將物件放入後 =>打開內容，requests只要一行就好
# # 先進行初始化，將物件放進去
# req = request.Request(url = url, headers=headers)
# # 打開物件
# res = request.urlopen(req) # 直接打開網址，後面不用

# #decode變將它用utf-8解碼變成字串
# html = res.read().decode("utf-8")
# print(html)
# ----------------------------------------------------------
# # 方法二: 使用requests函式庫(第三方)
# # 需先安裝requests函式庫，pip install requests
# import requests
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
# }
# #url = "網址"
# url = "https://www.ptt.cc/bbs/Stock/M.1710770280.A.8D1.html"

# res = requests.get(url, headers=headers) # 直接打開網址，後面不用，注意url後不能有空白
# # print(res) # 回傳 <Response [200]>，代表物件，代表成功回傳物件
# print(res.text) # 顯示內容

# ----------------------------------------------------------
# # 使用beautifulsoup套件
# # pip install bs4
# # bs4使用 find(顯示第一個符合的)、findAll(顯示全部)

# import requests
# from bs4 import BeautifulSoup
# #url = "網址"
# url = "https://www.ptt.cc/bbs/Stock/index.html"

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
# }

# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, "html.parser" )
# print(soup)
# bs4 用法，先找出所有符合條件的標籤
# =>findAll(tag, attribute)
# title_tag = soup.findAll('a',{'id':'logo'})
# findAll的寫法不太正確，但其實底層還是會呼叫findall

# # findAll 寫法一:字典
# title_tag = soup.findAll('div',{'class':'title'}) 

# findAll 寫法二: html的class為python中的保留字，因此無法直接使用，須加上底線_
# title_tag = soup.findAll('div',class_= 'title')
#  title_tag = soup.findAll('div',class_= 'date') # 測試

# print(title_tag)
# 會顯示 <a href="/bbs/Stock/M.1711204415.A.57A.html">[請益] 美股或美國科技股或台股的泡沫會來嗎??</a>

# ----------------------------------------------------------
# 使用beautifulsoup套件
# pip install bs4
# bs4使用 select_one(僅顯示一個)、select(顯示全部)
# import requests
# from bs4 import BeautifulSoup
# #url = "網址"
# url = "https://www.ptt.cc/bbs/Stock/index.html"

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
# }

# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, "html.parser" ) 

# # select 用法
# # select(‘tag[attribute]’)
# #寫法一: select(‘tag[attribute]’)
# title_tag = soup.select('a[class= "right small"]')
# title_tag = soup.select('a[id= "logo"]')

# title_tag = soup.select('div[class= "title"]') # 註:此處class不用加上底線_

# #寫法二: id class寫法轉換
# title_tag = soup.select('a.right.small') #class=right.small
# title_tag = soup.select('a#logo')  # id=logo
# title_tag = soup.select('div.title') # 註:class用.替代

# 註:
# id可用# 替代 如:div#apple，代表<div id=“apple”>
# class可用.替代 如:div.r-ent，代表<div class=“r-ent”>

# # 兩種條件，會找到符合a 或是 符合class條件的
# title_tag = soup.select('a', class_='right small') 

# print(title_tag)# 顯示<a href="/bbs/Stock/M.1711266983.A.CF0.html">[新聞] 三檔金融股 股利政策吸睛</a>

# # 若只想抓取title，可使用.text，搭配list[]
# print(title_tag[9].text) # 指定顯示第幾個的title文本
# # 顯示 [新聞] 三檔金融股 股利政策吸睛

# print(title_tag[0]) # 指定顯示第幾個的title文本
# #  顯示 <a class="right small" href="/about.html">關於我們</a>

# print(title_tag[0]["href"]) # 指定顯示第幾個文本的href，
# # 顯示 /about.html

# 顯示網址
# print("http://www.ptt.cc"+title_tag[0]["href"])
# ----------------------------------------------------------
# # 實作 找出ptt文章的標題，爬取一頁
# import requests
# from bs4 import BeautifulSoup
# #url = "網址"
# url = "https://www.ptt.cc/bbs/Stock/index.html"

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
# }

# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, "html.parser" ) 

# title_tag_list = soup.select('div.title a')

# print(title_tag_list)

# # 使用迴圈印出結果
# for title_tag in title_tag_list:
#     title = title_tag.text
#     print(title)
# ----------------------------------------------------------
# # 實作 找出ptt文章的標題，爬取多頁
# # 方法一:網址有規律，使用page-1的方式爬取
# """This is python program"""
# import requests
# from bs4 import BeautifulSoup
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0"
# }

# # https://www.ptt.cc/bbs/Stock/index7071.html
# # 觀察每頁網址變化，只會變動到數字，將數字進行挖空
# url = "https://www.ptt.cc/bbs/Stock/index%s.html"
# page = 7071
# for i in range(5):
#     res = requests.get(url % (page), headers=headers, timeout=30)
#     soup = BeautifulSoup(res.text, "html.parser" ) 

#     title_tag_list = soup.select('div.title a')
#     # print(title_tag_list)

#     # 使用迴圈印出結果

#     for title_tag in title_tag_list:
#         title = title_tag.text
#         article_url = "https://www.ptt.cc/" + title_tag["href"]
#         print(title)
#         print(article_url)
#     page -=1

# ----------------------------------------------------------
# 實作 找出ptt文章的標題，爬取多頁 multi_pages
# 方法二:按上下頁進行爬取
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

# ----------------------------------------------------------