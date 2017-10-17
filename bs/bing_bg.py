from urllib import request
import re
import os
import time


def get_bg(bg_name):
    host = 'http://cn.bing.com'

    url = host + '/HPImageArchive.aspx?format=js&idx=0&n=1'

    req = request.Request(url=url)
    rsp = request.urlopen(req).read().decode('utf-8')

    regex = r'"url":"(\S+?)"'
    bg_url = host + re.search(regex, rsp).group(1)
    bg_req = request.Request(url=bg_url)
    bg_rsp = request.urlopen(bg_req)

    with open(str(bg_name), 'wb') as f:
        f.write(bg_rsp.read())


def set_bg(bg_name):
    bg_uri = os.path.join(os.getcwd(), str(bg_name))

    os.system('{}{}'.format(
        'gsettings set org.gnome.desktop.background picture-uri file:///',
        bg_uri))


def get_story():
    url = 'http://cn.bing.com/cnhp/coverstory'

    req = request.Request(url)
    rsp = request.urlopen(req)

    content = eval(rsp.read().decode('utf-8'))
    print(content['title'])
    print(content['date'])
    print(content['attribute'])
    print(content['para1'])


def main():
    time.sleep(5)
    bg_name = 'bg.png'
    get_bg(bg_name)
    set_bg(bg_name)
    # get_story()
