# Generated by Django 4.1.6 on 2023-04-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_parser_app', '0002_remove_record_field3_alter_record_field2'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key1', models.CharField(max_length=50)),
                ('key2', models.CharField(max_length=50)),
                ('value1', models.CharField(max_length=50)),
                ('value2', models.CharField(max_length=50)),
            ],
        ),
    ]
