from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')


def add_contact(request):
    return render(request, 'add_contact.html')


def sites(request):
    return render(request, 'sites.html')


def add_site(request):
    return render(request, 'add_site.html')
