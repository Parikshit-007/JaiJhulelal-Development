# Generated by Django 4.1.3 on 2023-05-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default=None, help_text='BirthDate'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
