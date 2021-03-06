# Generated by Django 2.2.6 on 2020-03-24 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0008_recruiterprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('experience', models.CharField(max_length=1)),
                ('deadline', models.DateField()),
                ('skill', models.CharField(max_length=30)),
                ('salary', models.IntegerField()),
                ('posting_date', models.DateField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
