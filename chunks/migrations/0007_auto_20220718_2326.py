# Generated by Django 2.1 on 2022-07-18 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0006_chunks_movie_trailer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chunks',
            old_name='movie_trailer',
            new_name='chunks_trailer',
        ),
    ]
