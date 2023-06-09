# Generated by Django 4.2.2 on 2023-06-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_game_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='connectivity',
            field=models.IntegerField(choices=[(1, 'Offline'), (2, 'Online'), (3, 'Ambos')], default=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.IntegerField(choices=[(1, 'Single player'), (2, 'Multiplayer'), (3, 'Ambos'), (4, 'Melhor com amigos!')], default=1),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.IntegerField(choices=[(1, 'Ação'), (2, 'Aventura'), (3, 'Luta'), (4, 'Plataforma'), (5, 'Quebra-cabeça'), (6, 'Corrida'), (7, 'RPG'), (8, 'Tiro'), (9, 'Simulação'), (10, 'Esportes'), (11, 'Estratégia'), (12, 'MOBA')]),
        ),
    ]
