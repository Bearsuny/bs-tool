from urllib import request
import json
import re


def get_bg():
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

    req = request.Request(url=url)
    rsp = request.urlopen(req).read().decode('utf-8')

    print(rsp)
    test = "{'a':'s'}"
    print(json.dumps(eval(test)))

    regex = r'"url":"(\S+?)"'
    bg_url = re.search(regex, rsp).group(1)
    print(bg_url)

def get_story():
    url = 'http://cn.bing.com/cnhp/coverstory/'


get_bg()
