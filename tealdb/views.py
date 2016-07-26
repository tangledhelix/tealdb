from django.shortcuts import render, redirect
from django.db.models import Q

from tealdb.models import Site, Contact
from tealdb import views


def contacts(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts.html', context)


def contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {'contact': contact}
    return render(request, 'contact.html', context)


def add_contact(request):
    error = None
    sites = Site.objects.all()
    context = {'sites': sites}

    if request.method == 'POST':
        if 'inputSite' not in request.POST:
            error = 'Site is required.'
        elif not request.POST['inputSite'].strip():
            error = 'Site is required.'

        if 'inputFirstName' not in request.POST:
            error = 'First name is required.'
        elif not request.POST['inputFirstName'].strip():
            error = 'First name is required.'

        if 'inputLastName' not in request.POST:
            error = 'Last name is required.'
        elif not request.POST['inputLastName'].strip():
            error = 'Last name is required.'

        if error:
            context['error'] = error
        else:
            contact = Contact()
            site = Site.objects.get(id=request.POST['inputSite'])
            contact.site = site
            contact.first_name = request.POST['inputFirstName'].strip()
            contact.last_name = request.POST['inputLastName'].strip()
            if 'inputAddress1' in request.POST:
                contact.address1 = request.POST['inputAddress1'].strip()
            if 'inputAddress2' in request.POST:
                contact.address2 = request.POST['inputAddress2'].strip()
            if 'inputCity' in request.POST:
                contact.city = request.POST['inputCity'].strip()
            if 'inputState' in request.POST:
                contact.state = request.POST['inputState'].strip()
            if 'inputPostalCode' in request.POST:
                contact.postal_code = request.POST['inputPostalCode'].strip()
            if 'inputCountry' in request.POST:
                contact.country = request.POST['inputCountry'].strip()
            if 'inputPhone' in request.POST:
                contact.phone = request.POST['inputPhone'].strip()
            if 'inputFax' in request.POST:
                contact.fax = request.POST['inputFax'].strip()
            if 'inputMobilePhone' in request.POST:
                contact.mobile_phone = request.POST['inputMobilePhone'].strip()
            if 'inputEmail' in request.POST:
                contact.email = request.POST['inputEmail'].strip()
            if 'inputSocialTwitter' in request.POST:
                contact.social_twitter = request.POST['inputSocialTwitter'].strip()
            if 'inputSocialFacebook' in request.POST:
                contact.social_facebook = request.POST['inputSocialFacebook'].strip()
            if 'inputSocialInstagram' in request.POST:
                contact.social_instagram = request.POST['inputSocialInstagram'].strip()
            if 'inputNotes' in request.POST:
                contact.notes = request.POST['inputNotes'].strip()
            if 'inputAsshole' in request.POST:
                contact.asshole = True
            if 'inputOfficial' in request.POST:
                contact.official = True
            contact.save()
            return redirect(views.contacts)

    return render(request, 'add_contact.html', context)


def sites(request):
    sites = Site.objects.all()
    for site in sites:
        contact_count = Contact.objects.filter(site=site).count()
        site.contact_count = contact_count

    context = {
        'sites': sites,
    }
    return render(request, 'sites.html', context)


def site(request, site_id):
    site = Site.objects.get(id=site_id)
    disposition = None

    for d in Site.DISPOSITION_CHOICES:
        if d[0] == site.disposition:
            disposition = d[1]

    context = {
        'disposition': disposition,
        'site': site,
    }
    return render(request, 'site.html', context)


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


def search(request):
    if 'needle' not in request.POST:
        return redirect('main')

    needle = request.POST['needle'].strip()

    sites = Site.objects.filter(name__icontains=needle)
    contacts = Contact.objects.filter(
        Q(first_name__icontains=needle) | Q(last_name__icontains=needle)
    )

    context = {'sites': sites, 'contacts': contacts, 'needle': needle}
    return render(request, 'search.html', context)
