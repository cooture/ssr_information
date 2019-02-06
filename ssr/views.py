import os
import sys

from django.shortcuts import render
from django.http import HttpResponse
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
    (status, output) =  os.subprocess.getstatusoutput('cat /proc/cpuinfo')
    return HttpResponse(output)
