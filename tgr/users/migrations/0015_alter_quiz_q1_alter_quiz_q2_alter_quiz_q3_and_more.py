# Generated by Django 4.2.2 on 2023-11-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_quiz_q10_remove_quiz_q8_remove_quiz_q9_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='q1',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='q2',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='q3',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='q4',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='q5',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='q6',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='q7',
            field=models.CharField(max_length=25),
        ),
    ]
