# Generated by Django 5.0 on 2023-12-19 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-due_date']},
        ),
    ]
