# Generated by Django 4.2.2 on 2023-06-26 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_customuser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
