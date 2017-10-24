from urllib import request, parse
from bs4 import BeautifulSoup
import os

html_path = os.path.join(os.path.dirname(os.getcwd()),
                         'test/hzbook_download.html')

with open(html_path, 'r', encoding='gbk') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
link_list = soup.select("a")
book_path = os.path.join(os.path.dirname(os.getcwd()),
                         'test/')
book_list = 0
for link in link_list:
    if link.has_attr('href'):
        if link['href'].find('.pdf') != -1:
            url = link['href']
            print(url)
            req = request.Request(url=url)
            rsp = request.urlopen(req)
            # with open(book_path + str(book_list) + '.pdf', 'wb') as file:
            #     file.write(rsp.read())
            #     print(str(book_list) + ' book download success.')
            # book_list += 1
