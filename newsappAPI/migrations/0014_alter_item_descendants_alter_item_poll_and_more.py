# Generated by Django 4.1.5 on 2023-01-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsappAPI', '0013_alter_item_parent_alter_kid_item_alter_kid_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descendants',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='poll',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kid',
            name='descendants',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='kid',
            name='poll',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]