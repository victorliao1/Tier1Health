# Generated by Django 2.1.5 on 2019-01-12 21:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('t1health_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='stats',
            new_name='Statistic',
        ),
    ]
