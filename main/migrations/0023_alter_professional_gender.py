# Generated by Django 4.1.3 on 2023-06-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_professional_sindhi_sub_caste_professional_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=10),
        ),
    ]
