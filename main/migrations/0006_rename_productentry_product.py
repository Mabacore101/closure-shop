# Generated by Django 5.1.1 on 2024-09-21 07:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productentry_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductEntry',
            new_name='Product',
        ),
    ]
