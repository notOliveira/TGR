# Generated by Django 4.2.2 on 2023-06-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_online_game_connectivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Action'), (2, 'Adventure'), (3, 'RPG'), (4, 'Strategy'), (5, 'Sports'), (6, 'Simulation'), (7, 'Puzzle'), (8, 'Racing'), (9, 'Shooter'), (10, 'Fighting'), (11, 'MOBA'), (12, 'RTS')]),
        ),
    ]
