# Generated by Django 2.1 on 2022-07-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='chunks')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('D', 'DRAMA'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=1)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('GR', 'GERMAN')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'Recently Added'), ('MW', 'Mostly watched'), ('TR', 'Top Rated')], max_length=2)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
    ]
