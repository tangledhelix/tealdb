from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def sites(request):
    return render(request, 'sites.html')


def add_site(request):
    return render(request, 'add_site.html')
