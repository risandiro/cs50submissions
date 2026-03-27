from django.shortcuts import render, redirect
from random import choice
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "title": util.get_title(title),
            "content": util.markdown_convert(content)
        })
    return render(request, "encyclopedia/error.html")

def search(request):
    query = request.POST.get("q")
    content = util.list_entries()
    for item in content:
        if query.lower() == item.lower():
            return redirect(f"/wiki/{query}")
        
    suggestions = []
    for item in content:
        if query.lower() in item.lower():
            suggestions.append(item)
            
    return render(request, "encyclopedia/search.html", {
        "suggestions": suggestions
    })

def newpage(request):
    if request.method == "POST":
        title = request.POST.get("newpage_title")
        content = request.POST.get("newpage_content")

        # check if the name isn't already taken, if so, return the form back
        for item in util.list_entries():
            if item.lower() == title.lower():
                return render(request, "encyclopedia/newpage.html", {
                    "newpage_title": title,
                    "newpage_content": content
                })

        util.save_entry(title, content)
        return redirect(f"/wiki/{title}")

    return render(request, "encyclopedia/newpage.html")

def editpage(request, title):
    if request.method == "POST":
        content = request.POST.get("page_content")
        util.save_entry(title, content)
        return redirect(f"/wiki/{title}")
    
    # check if the page that he wants to render actually exists
    for item in util.list_entries():
        if item.lower() == title.lower():
            return render(request, "encyclopedia/editpage.html", {
            "page_title": title,
            "page_content": util.get_entry(title)
            })

    # if it doesn't return an error message    
    return render(request, "encyclopedia/error.html")

def random(request):
    random_page = choice(util.list_entries())
    return redirect(f"/wiki/{random_page}")