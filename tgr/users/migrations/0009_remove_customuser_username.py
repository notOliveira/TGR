# Generated by Django 4.2.2 on 2023-06-26 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
