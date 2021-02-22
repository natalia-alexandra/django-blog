from django.shortcuts import render


def home(req):
    context = {}
    return render(req, 'pages/index.html', context)
