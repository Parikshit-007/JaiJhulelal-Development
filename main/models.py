from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.validators import MaxValueValidator
class ProfileManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(ProfileManager, self).get_queryset(*args, **kwargs).filter()

   
    def create_professional(self, user, **kwargs):
        return self.model.objects.create(user=user, **kwargs)
    
    

class Profile(models.Model):
    boolChoice = (("M", "Male"), ("F", "Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    profile_image = models.ImageField(upload_to='media/', blank=True)
    gender = models.CharField(max_length=10, choices=boolChoice, null=True)
    birthdate = models.DateField(null=True)
    reference = models.CharField(max_length=100, default='')
    ref_num = models.IntegerField(default=None, null=True)
    Sindhi_Sub_Caste = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username
    objects = ProfileManager()

    class Meta:
        abstract = True


class Professional(Profile):
    def generate_profession_choices():
        original_choices = [
            ('estate agent', 'Estate Agent'),
            ('papad_seller', 'Papad Seller'),
            ('maharaj_swami', 'Maharaj Swami'),
            ('lada_singer', 'Lada Singer'),
            ('rasoiyo', 'Rasoiyo'),
            ('maitinwaro', 'Maitinwaro'),
            ('maitinwari', 'Maitinwari'),
            ('doctor', 'Doctor'),
            ('engineer', 'Engineer'),
            ('genuine_properties', 'Genuine Properties'),
            ('safe_tourism', 'Safe Tourism'),
            ('social_workers', 'Social Workers'),
            ('education', 'Education'),
            ('food_industries', 'Food Industries'),
            ('advocates', 'Advocates'),
            ('entrepreneur', 'Entrepreneur'),
        ]

        choices = []
        for value, label in original_choices:
            # Add original choice
            choices.append((value, label))

            # Add lowercase choice
            choices.append((value.lower(), label.lower()))

            # Add uppercase choice
            choices.append((value.upper(), label.upper()))

            # Replace underscores with spaces and add
            space_label = label.replace('_', ' ')
            choices.append((value, space_label))
            choices.append((value.lower(), space_label.lower()))
            choices.append((value.upper(), space_label.upper()))

            # Add choice with underscores
            underscore_value = value.replace('_', ' ')
            choices.append((underscore_value, label))
            choices.append((underscore_value.lower(), label.lower()))
            choices.append((underscore_value.upper(), label.upper()))

        return choices
    PROFESSION_CHOICES = generate_profession_choices()

    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES, blank=True, null=True)
    desc = models.TextField(max_length=500, default='')
    is_verified = models.BooleanField(default=False)

def get_profession_choices(self):
    choices = self.PROFESSION_CHOICES.copy()
    if self.profession:
        formatted_profession = self.profession.replace('_', ' ').title()
        if (self.profession, formatted_profession) not in choices:
            choices.append((self.profession, formatted_profession))
    return choices


    def __str__(self):
        return self.user.username

from django.db import models


from django.db import models
from django.template.defaultfilters import slugify

class WellWisher(models.Model):
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=20)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    desc = models.TextField(max_length=500, default='')
    address = models.CharField(max_length=200, default='')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, default='')
    slug = models.SlugField(unique=True, blank=True, null=True)  # Add this field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class VerifiedProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'profession', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'address', 'phone_number')
    list_per_page = 20


class NonVerifiedProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'profession', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'address', 'phone_number')
    list_per_page = 20
