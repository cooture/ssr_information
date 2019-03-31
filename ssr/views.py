import json
import os
import subprocess
import sys
import time

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ssr.haha import getssr
import base64


# Create your views here.
def dingyue(request):
    url, _ = getssr()

    # data = {
    #     'data': str(base64.b64encode(url.encode("utf-8")), 'utf-8')
    # }
    #  Text file  
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=my.txt'
    response.write(str(base64.b64encode(url.encode("utf-8")), 'utf-8'))


    return response

def status(request):
    cmd = "/etc/init.d/shadowsocks status"
    (status, output) =  subprocess.getstatusoutput(cmd)
    return HttpResponse(output)


def getlog(request):
    cmd = "tail -n 50 /var/log/shadowsocksr.log"
    (status, output) = subprocess.getstatusoutput(cmd)
    return HttpResponse(output)


def getRawConfig(request):
    url, _ = getssr()

    return HttpResponse(url)


def getConfig(request):
    jsonfile = open("/etc/shadowsocks.json")
    conjson = json.load(jsonfile)
    return JsonResponse(conjson)


def getQRCode(request):
    _, qr = getssr()
    qr.save("static/qrcode.jpg")
    return render(request,"qr.html", {"time": str(time.asctime( time.localtime(time.time()) ))})


def getLinkInfo(request):
    cmd = '''netstat -anp |grep 'ESTABLISHED' |grep 'python' |grep 'tcp6' |awk '{print $5}' |awk -F ":" '{print $1}' |sort -u'''
    (status, output) = subprocess.getstatusoutput(cmd)
    output = output.split()
    res = '<br>'.join(output)
    return HttpResponse(res)



def getAllLink(request):
    return render(request, "link.html")