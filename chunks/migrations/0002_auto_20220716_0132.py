# Generated by Django 2.1 on 2022-07-16 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chunks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='chunks')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('D', 'DRAMA'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=1)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('GR', 'GERMAN')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'Recently Added'), ('MW', 'Mostly watched'), ('TR', 'Top Rated')], max_length=2)),
                ('cast', models.CharField(max_length=100)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='chunksLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DOWNLOAD LINK'), ('W', 'WATCH LINK')], max_length=1)),
                ('link', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='chunks.chunks')),
            ],
        ),
        migrations.DeleteModel(
            name='chunk',
        ),
    ]
