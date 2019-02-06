from django.shortcuts import render
from django.http import HttpResponse
from ssr.haha import getssr
import base64


# Create your views here.
def dingyue(request):
    url, _ = getssr()

    data = {
        'data': str(base64.b64encode(url.encode("utf-8")), 'utf-8')
    }
    return HttpResponse(str(base64.b64encode(url.encode("utf-8")), 'utf-8'))
