from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def hello_page(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "mainpage/index.html",
        {
            "title": "Main",
        },
    )
