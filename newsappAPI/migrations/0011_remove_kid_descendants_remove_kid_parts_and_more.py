# Generated by Django 4.1.5 on 2023-01-10 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsappAPI', '0010_rename_kids_kid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kid',
            name='descendants',
        ),
        migrations.RemoveField(
            model_name='kid',
            name='parts',
        ),
        migrations.RemoveField(
            model_name='kid',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='kid',
            name='score',
        ),
    ]