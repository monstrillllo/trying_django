# Generated by Django 3.2 on 2021-04-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime_lists', '0002_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Titles',
        ),
    ]
