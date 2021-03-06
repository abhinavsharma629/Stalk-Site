# Generated by Django 2.1.4 on 2019-01-01 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0006_auto_20190101_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('college_name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacherprofiles',
            name='user',
        ),
        migrations.DeleteModel(
            name='TeacherProfiles',
        ),
    ]
