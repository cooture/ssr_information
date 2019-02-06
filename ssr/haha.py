# ssr://base64(host:port:protocol:method:obfs:base64pass/?obfsparam=base64param&protoparam=base64param&remarks=base64remarks&group=base64group&udpport=0&uot=0

import base64
import json

import qrcode
import requests


# import qrcode


# define
def make_base64(something):
    return str(base64.urlsafe_b64encode(something.encode("utf-8")), 'utf-8').replace("=", "")


# var
host = "127.0.0.1"

port = "1234"
protocol = "auth_aes128_md5"
method = "aes-128-cfb"
obfs = "tls1.2_ticket_auth"
password = "aaabbb"
password_base = make_base64(password)
obfsparam = "breakwa11.moe"
obfsparam_base = make_base64(obfsparam)
protoparam = ""
protoparam = make_base64(protoparam)
remarks = "Google"
remarks_base = make_base64(remarks)


def getssr():
    try:
        host = requests.get("http://ifconfig.me").text
    except Exception as e:
        print("error internet with get ip")

    json_path = "/etc/shadowsocks.json"
    file = open(json_path, 'r')
    data = json.load(file)
    print(data)
    port = str(data['server_port'])
    protocol = str(data['protocol'])
    method = str(data['method'])
    obfs = str(data['obfs'])
    password = str(data['password'])
    password_base = make_base64(password)

    obfsparam = str(data['obfs_param'])
    obfsparam_base = make_base64(obfsparam)
    group="rankin"
    group_base = make_base64(group)

    # ssr://base64(host:port:protocol:method:obfs:base64pass/?obfsparam=base64param&protoparam=base64param&remarks=base64remarks&group=base64group&udpport=0&uot=0

    url_noparam = host + ":" + port + ":" + protocol + ":" + method + ":" + obfs + ":" + password_base
    param = "/?" + "obfsparam=" + obfsparam_base + "&remarks=" + remarks_base+"&group="+group_base
    url = url_noparam + param

    final = "ssr://" + make_base64(url)

    img = qrcode.make(final)
    # img.save('test.png')
    print(final)
    return final, img
