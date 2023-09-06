from django.db.models import Q
from main.models import Professional
from datetime import date
from django.shortcuts import render

def search(request):
    query = request.GET.get('q', '')
    name_results = request.GET.get('name_results', '').strip()
    profession_results = request.GET.get('profession_results', '').strip().lower()  # Normalize to lowercase
    address_results = request.GET.get('address_results', '').strip()

    professionals = Professional.objects.all()

    if profession_results:
        # Normalize the profession value to lowercase before filtering
        profession_results = profession_results.lower()
        professionals = professionals.filter(profession__iexact=profession_results)
    if address_results:
        professionals = professionals.filter(address__icontains=address_results)
    if name_results:
        professionals = professionals.filter(user__username__icontains=name_results)

    for professional in professionals:
        if not professional.profile_image:
            professional.profile_image = 'path/to/default/image.jpg'

    category_name = profession_results if profession_results else 'All Categories'
    
    profession_choices = professionals.values_list('profession', flat=True).distinct()
    
    verified_count = professionals.count()
    result_count = f"{verified_count} Results on {date.today().strftime('%d %B, %Y')}"

    context = {
        'query': query,
        'name_results': name_results,
        'profession_results': profession_results,
        'address_results': address_results,
        'professionals': professionals,
        'category_name': category_name,
        'profession_choices': profession_choices,
        'result_count': result_count,
    }

    return render(request, 'search.html', context)
