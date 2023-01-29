from django.shortcuts import render


def test(request):
    return render(request, 'index.html')


def temp(request):
    return render(request, 'account/profile2.html')