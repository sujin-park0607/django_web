from django.shortcuts import render


def index(request):
    return render(request, 'main/main.html')


def major(request):
    return render(request, 'main/major.html')


def test(request):
    return render(request, 'main/test.html')