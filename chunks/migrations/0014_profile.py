# Generated by Django 2.1 on 2022-07-24 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0013_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('age_limit', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=5)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
    ]
