# Generated by Django 4.1.6 on 2023-04-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_parser_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='field3',
        ),
        migrations.AlterField(
            model_name='record',
            name='field2',
            field=models.CharField(max_length=500),
        ),
    ]
