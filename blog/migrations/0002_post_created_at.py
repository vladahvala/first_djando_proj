# Generated by Django 4.1.3 on 2022-12-10 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
