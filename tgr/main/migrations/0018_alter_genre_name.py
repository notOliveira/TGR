# Generated by Django 4.2.2 on 2023-06-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.IntegerField(choices=[(1, 'Action'), (2, 'Adventure'), (3, 'Fighting'), (4, 'Platform'), (5, 'Puzzle'), (6, 'Racing'), (7, 'RPG'), (8, 'Shooter'), (9, 'Simulation'), (10, 'Sports'), (11, 'Strategy'), (12, 'MOBA')]),
        ),
    ]
