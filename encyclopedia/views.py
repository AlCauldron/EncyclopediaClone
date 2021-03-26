from django.shortcuts import render
from . import util
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import random

def contains(query):
    for title in util.list_entries():
        if query.lower().strip() in title.lower():
            return True
    return False

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    if util.get_entry(title) == None:
        return render(request,"encyclopedia/errorpage.html")
    return render(request,"encyclopedia/body.html",{
        "name": title,
        "body": util.get_entry(title)
    })

def search(request):
    if request.method == "POST":
        entry = request.POST['query']
        if util.get_entry(entry) != None:
            return render(request,"encyclopedia/body.html",{
                "name": entry,
                "body": util.get_entry(entry)
            })
        else:
            if(contains(entry)):
                all = []
                for title in util.list_entries():
                    if entry.lower().strip() in title.lower():
                        all.append(title)
                return render(request,'encyclopedia/search.html',{
                    'entries':all
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries()
                })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request):
    if request.method == "POST":
        name = request.POST['title']
        content = request.POST['content']
        if name in util.list_entries():
            return HttpResponse('<h1>Title already taken</h1>')
        else:
            util.save_entry(name,content)
            return HttpResponseRedirect(reverse('index'))
    return render(request,'encyclopedia/newpage.html')

def edit(request,title):
    return render(request,'encyclopedia/edit.html',{
        "name":title,
        "content":util.get_entry(title)
    })

def save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def chaos(request):
    topic = random.choice(util.list_entries())
    return render(request,"encyclopedia/body.html",{
        "name":topic,
        "body":util.get_entry(topic)
    })