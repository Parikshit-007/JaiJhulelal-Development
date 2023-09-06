from django.shortcuts import get_object_or_404, render
from main.models import Profile, Professional, Contact, WellWisher

# Create your views here.

def home(request):
    well_wishers = WellWisher.objects.all()
    for well_wisher in well_wishers:
        well_wisher.star_range = range(well_wisher.rating)
        well_wisher.empty_star_range = range(5 - well_wisher.rating)
    context = {
        'well_wishers': well_wishers,
    }
    return render(request, 'index.html', context)

def well_wisher_detail(request, slug):
    well_wisher = get_object_or_404(WellWisher, slug=slug)
    context = {
        'well_wisher': well_wisher,
    }
    return render(request, 'well_wisher.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contactus.html', {'thank': thank})

def terms_condition(request):
    return render(request, 'terms-condition')

from django.shortcuts import get_object_or_404, render
from main.models import Profile, Professional

def FullView(request, id):
    professional = get_object_or_404(Professional, id=id)
  #  profile = get_object_or_404(Profile, id=id)
    return render(request, 'fullview.html', {'professional': professional})#, 'profile': profile})

