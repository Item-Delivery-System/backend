# Generated by Django 5.0.3 on 2024-03-28 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='serviceProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_front', models.ImageField(upload_to='user/id')),
                ('id_back', models.ImageField(upload_to='user/id')),
                ('license_front', models.ImageField(upload_to='user/id')),
                ('license_back', models.ImageField(upload_to='user/id')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_provider', to='user.profile')),
            ],
        ),
    ]
