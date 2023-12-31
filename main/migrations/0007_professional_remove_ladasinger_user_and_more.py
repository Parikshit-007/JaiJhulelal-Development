# Generated by Django 4.1.3 on 2023-05-17 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_estateagent_is_verified_ladasinger_is_verified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('profession', models.CharField(choices=[('estate_agent', 'Estate Agent'), ('papad_seller', 'Papad Seller'), ('maharaj_swami', 'Maharaj Swami'), ('lada_singer', 'Lada Singer'), ('rasoiyo', 'Rasoiyo'), ('maitinwaro', 'Maitinwaro'), ('maitinwari', 'Maitinwari')], default='estate_agent', max_length=50)),
                ('other_profession', models.CharField(blank=True, max_length=50, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ladasinger',
            name='user',
        ),
        migrations.RemoveField(
            model_name='maharajswami',
            name='user',
        ),
        migrations.RemoveField(
            model_name='maitinwari',
            name='user',
        ),
        migrations.RemoveField(
            model_name='maitinwaro',
            name='user',
        ),
        migrations.RemoveField(
            model_name='papadseller',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rasoiyo',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='ref_num',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='reference',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='EstateAgent',
        ),
        migrations.DeleteModel(
            name='LadaSinger',
        ),
        migrations.DeleteModel(
            name='MaharajSwami',
        ),
        migrations.DeleteModel(
            name='Maitinwari',
        ),
        migrations.DeleteModel(
            name='Maitinwaro',
        ),
        migrations.DeleteModel(
            name='PapadSeller',
        ),
        migrations.DeleteModel(
            name='Rasoiyo',
        ),
    ]
