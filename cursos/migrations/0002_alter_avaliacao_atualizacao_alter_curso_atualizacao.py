# Generated by Django 4.1.3 on 2023-01-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
