# Generated by Django 2.1.4 on 2019-01-01 18:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0004_auto_20190101_2321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeacherProfile',
            new_name='TeacherProf',
        ),
    ]