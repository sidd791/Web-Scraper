from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    if request.method == "POST":
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, "html.parser")
        for i in soup.find_all("a"):
            link_name = i.string
            address = i.get('href')
            Link.objects.create(name= link_name, link_address = address)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
    return render(request, 'layout/index.html', {'data': data})

def delete(request):
    Link.objects.all().delete()
    return HttpResponseRedirect('/')
