# Generated by Django 4.1.5 on 2023-01-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsappAPI', '0004_item_parts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(default='', max_length=128),
        ),
    ]