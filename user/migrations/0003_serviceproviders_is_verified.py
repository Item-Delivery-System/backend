# Generated by Django 5.0.3 on 2024-03-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_bio_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceproviders',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
