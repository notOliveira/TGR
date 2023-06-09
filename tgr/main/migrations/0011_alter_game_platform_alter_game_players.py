# Generated by Django 4.2.2 on 2023-06-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_game_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.IntegerField(choices=[(1, 'PC'), (2, 'Xbox'), (3, 'Playstation'), (4, 'Switch'), (5, 'All')], default=1, max_length=4),
        ),
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.IntegerField(choices=[(1, 'Single player'), (2, 'Multiplayer'), (3, 'Both'), (4, 'Better with friends!')], default=1),
        ),
    ]
