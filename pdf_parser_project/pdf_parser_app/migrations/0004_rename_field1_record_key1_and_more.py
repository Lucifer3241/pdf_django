# Generated by Django 4.1.6 on 2023-04-29 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_parser_app', '0003_mydata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='field1',
            new_name='key1',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='field2',
            new_name='value1',
        ),
        migrations.RemoveField(
            model_name='mydata',
            name='key2',
        ),
        migrations.RemoveField(
            model_name='mydata',
            name='value2',
        ),
    ]
