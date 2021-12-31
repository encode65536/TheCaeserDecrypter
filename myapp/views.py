from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    return render(request, 'a.html')


def counter(request):
    s = request.POST['text']
    r = {}
    for i in range(25):
        s1 = ''
        for k in s:
            t = ord(k)
            if (ord('z') > t >= ord('a')) or (ord('Z') > t >= ord('A')):
                s1 += chr(t + 1)
            elif t == ord('Z') or t == ord('z'):
                s1 += chr(t - 25)
            else:
                s1 += k
        r["CypherNo"+str(i+1)] = s1
        s = s1
    return render(request, 'b.html', r)

