# Generated by Django 2.1 on 2022-07-19 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0007_auto_20220718_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunks',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
