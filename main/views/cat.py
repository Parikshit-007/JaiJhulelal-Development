from django.shortcuts import render, redirect
from main.models import Professional
from datetime import date

def professionals_by_profession(request, profession):
    professionals = Professional.objects.filter(profession=profession, is_verified=True)
    template_name = f'{profession}.html'
    context = {'professionals': professionals}
    return render(request, template_name, context)

def separate_profession(request, profession):
    # Assuming PROFESSION_CHOICES is defined in your models.py
    profession_display_name = dict(Professional.PROFESSION_CHOICES).get(profession)
    
    if profession_display_name:
        professionals = Professional.objects.filter(profession=profession, is_verified=True)
        verified_count = professionals.count()
        template = f'{profession}s.html'

        result_count = f"{verified_count} Results on {date.today()}"
        
        context = {
            'professionals': professionals,
            'current_date': date.today(),
            'verified_count': verified_count,
            'profession_name': profession_display_name.title(),
            'result_count': result_count,
        }
        
        return render(request, template, context)
    else:
        # Handle the case when an invalid profession is selected
        return redirect('home')  # Redirect to the home page or any other desired page
