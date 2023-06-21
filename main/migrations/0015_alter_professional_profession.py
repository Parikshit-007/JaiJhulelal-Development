# Generated by Django 4.1.3 on 2023-06-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_professional_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='profession',
            field=models.CharField(blank=True, choices=[('', 'Custom'), ('estate_agent', 'Estate Agent'), ('papad_seller', 'Papad Seller'), ('maharaj_swami', 'Maharaj Swami'), ('lada_singer', 'Lada Singer'), ('rasoiyo', 'Rasoiyo'), ('maitinwaro', 'Maitinwaro'), ('maitinwari', 'Maitinwari'), ('doctor', 'Doctor'), ('engineer', 'Engineer'), ('genuine_properties', 'Genuine Properties'), ('safe_tourism', 'Safe Tourism'), ('social_workers', 'Social Workers'), ('education', 'Education'), ('food_industries', 'Food Industries'), ('advocates', 'Advocates')], max_length=50, null=True),
        ),
    ]
