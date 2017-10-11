from urllib import request, parse
import time
import re
import os
import webbrowser


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

    os.popen('display {}'.format(path))

    print('Done.')
    print('Please use your phone to scan the qrcode...')


def login(uuid):
    url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'

    data = {
        'loginicon': 'true',
        'uuid': str(uuid),
        'tip': 1,
        '_': int(time.time())
    }

    req = request.Request(url=url, data=parse.urlencode(data).encode('utf-8'))
    rsp = request.urlopen(req).read().decode('utf-8')

    regex = r'window.code=(\d+);'
    code = re.search(regex, rsp).group(1)

    if code == '200':
        print('Login success.')
        regex = r'window.redirect_uri="(\S+?)"'
        webbrowser.open(re.search(regex, rsp).group(1))
    elif code == '201':
        print('Done. Waiting confirm...')
    elif code == '408':
        print('Login timeout. Waiting scan...')
    else:
        print('window.code=' + str(code))

    return code


def main():
    uuid = get_uuid()
    path = os.path.join(os.getcwd(), 'qrcode.png')

    get_qrcode(uuid, path)

    while login(uuid) != '200':
        pass

    os.remove(path)


if __name__ == '__main__':
    main()
