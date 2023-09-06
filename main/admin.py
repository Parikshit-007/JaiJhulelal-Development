from pyexpat.errors import messages
from django.contrib import admin
from django.urls import path, include
from main.forms import ExcelImportForm
from .models import Profile, Professional, VerifiedProfessionalAdmin, NonVerifiedProfessionalAdmin, Contact, WellWisher
from django.contrib.auth.decorators import user_passes_test
#from main.import_data import import_data_from_excel
from django.shortcuts import redirect,render

class CombinedProfessionalAdmin(VerifiedProfessionalAdmin, NonVerifiedProfessionalAdmin):
    pass

admin.site.register(Contact)
admin.site.register(Professional, CombinedProfessionalAdmin)

@admin.register(WellWisher)
class WellWisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'birthdate', 'rating')

# Define the custom admin view function
def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def upload_excel_view(request):
    if request.method == 'POST':
        form = ExcelImportForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            try:
                import_data_from_excel(excel_file)
                messages.success(request, "Data imported successfully.")
            except Exception as e:
                messages.error(request, f"Error importing data: {str(e)}")
            return redirect('admin:index')  # Redirect back to the admin index page
    else:
        form = ExcelImportForm()

    return render(
        request,
        "admin/import_excel.html",
        {"form": form},
    )

# Define the URL pattern for the custom view
urlpatterns = [
    path('upload_excel/', upload_excel_view, name='upload_excel'),
]
