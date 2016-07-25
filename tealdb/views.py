from django.shortcuts import render, redirect

from tealdb.models import Site, Contact
from tealdb import views


def main(request):
    return render(request, 'main.html')


def contacts(request):
    return render(request, 'contacts.html')


def contact(request, contact_id):
    return render(request, 'contact.html')


def add_contact(request):
    return render(request, 'add_contact.html')


def sites(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request, 'sites.html', context)


def site(request, site_id):
    return render(request, 'site.html')


def add_site(request):
    error = None
    context = {}

    if request.method == 'POST':
        if 'inputName' not in request.POST:
            error = 'Site name is required.'
        elif not request.POST['inputName'].strip():
            error = 'Site name is required.'

        if error:
            context['error'] = error
        else:
            site = Site()
            site.name = request.POST['inputName'].strip()
            if 'inputAddress1' in request.POST:
                site.address1 = request.POST['inputAddress1'].strip()
            if 'inputAddress2' in request.POST:
                site.address2 = request.POST['inputAddress2'].strip()
            if 'inputCity' in request.POST:
                site.city = request.POST['inputCity'].strip()
            if 'inputState' in request.POST:
                site.state = request.POST['inputState'].strip()
            if 'inputPostalCode' in request.POST:
                site.postal_code = request.POST['inputPostalCode'].strip()
            if 'inputCountry' in request.POST:
                site.country = request.POST['inputCountry'].strip()
            if 'inputWebSite' in request.POST:
                site.web_site = request.POST['inputWebSite'].strip()
            if 'inputEmail' in request.POST:
                site.email = request.POST['inputEmail'].strip()
            if 'inputPhone' in request.POST:
                site.phone = request.POST['inputPhone'].strip()
            if 'inputFax' in request.POST:
                site.fax = request.POST['inputFax'].strip()
            if 'inputYearsLit' in request.POST:
                site.years_lit = request.POST['inputYearsLit'].strip()
            if 'inputMapLink' in request.POST:
                site.map_link = request.POST['inputMapLink'].strip()
            if 'inputNotes' in request.POST:
                site.notes = request.POST['inputNotes'].strip()
            if 'inputDisposition' in request.POST:
                site.disposition = request.POST['inputDisposition'].strip()
            if 'inputFee' in request.POST:
                site.fee = True
            if 'inputHaveLit' in request.POST:
                site.have_lit = True
            site.save()
            return redirect(views.sites)

    return render(request, 'add_site.html', context)
