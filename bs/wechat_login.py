from urllib import request, parse
import time
import re
import os
import webbrowser
import sys
import subprocess
import signal


def get_uuid():
    print('Getting the uuid...')

    url = 'https://login.wx.qq.com/jslogin'

    data = {
        'appid': 'wx782c26e4c19acffb',
        'redirect_uri': 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
        'fun': 'new',
        'lang': 'en_US',
        '_': int(time.time())
    }

    req = request.Request(url=url, data=parse.urlencode(data).encode('utf-8'))
    rsp = request.urlopen(req).read().decode('utf-8')

    regex = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
    uuid = re.search(regex, rsp).group(2)

    print('Done.')
    return uuid


def get_qrcode(uuid, path):
    print('Getting the qrcode...')

    url = 'https://login.weixin.qq.com/qrcode/' + str(uuid)

    req = request.Request(url=url)
    rsp = request.urlopen(req)

    with open(path, 'wb') as f:
        f.write(rsp.read())

    sp = subprocess.Popen(['display', path])

    # fd = os.popen('display {}'.format(path))

    print('Done.')
    print('Please use your phone to scan the qrcode...')

    return sp


def login(uuid):
    url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'

    data = {
        'loginicon': 'true',
        'uuid': str(uuid),
        'tip': 1,
        '_': int(time.time())
    }

    try:
        req = request.Request(url=url,
                              data=parse.urlencode(data).encode('utf-8'))
        rsp = request.urlopen(req).read().decode('utf-8')

        regex = r'window.code=(\d+);'
        code = re.search(regex, rsp).group(1)
        link = ''

        if code == '200':
            print('Login success.')
            regex = r'window.redirect_uri="(\S+?)"'
            link = re.search(regex, rsp).group(1)
        elif code == '201':
            print('Done. Waiting confirm...')
        elif code == '408':
            print('Login timeout. Waiting scan...')
        else:
            print('window.code=' + str(code))

        return {'code': code, 'link': link}
    except KeyboardInterrupt as err:
        print(err)
        print('Exit.')
        sys.exit(0)


def main():
    uuid = get_uuid()
    path = os.path.join(os.getcwd(), 'qrcode.png')

    sp = get_qrcode(uuid, path)

    info = login(uuid)
    while info['code'] != '200':
        info = login(uuid)
        pass

    os.kill(sp.pid, signal.SIGTERM)

    os.remove(path)

    webbrowser.open(info['link'])
