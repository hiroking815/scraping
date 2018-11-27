from bs4 import BeautifulSoup
 

html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"


# 第一引数に解析したいもの
# 第二引数にパーサ

soup = BeautifulSoup(html, "html.parser")

print(soup.select("h1"))



