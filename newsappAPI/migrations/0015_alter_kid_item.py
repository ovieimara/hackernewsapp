# Generated by Django 4.1.5 on 2023-01-10 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsappAPI', '0014_alter_item_descendants_alter_item_poll_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='newsappAPI.item'),
        ),
    ]
