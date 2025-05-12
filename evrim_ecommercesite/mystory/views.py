from django.shortcuts import render

def my_story(request):
    return render(request, "mystory/mystory.html")