# Generated by Django 4.2.2 on 2023-06-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_connectivity_genre_platform_players_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectivity',
            old_name='connectivity',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='platform',
            old_name='platform',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='players',
            old_name='players',
            new_name='name',
        ),
    ]
