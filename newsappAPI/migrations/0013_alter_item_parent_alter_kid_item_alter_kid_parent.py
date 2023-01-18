# Generated by Django 4.1.5 on 2023-01-10 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsappAPI', '0012_kid_descendants_kid_parts_kid_poll_kid_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='parent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kid',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='newsappAPI.item'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kid',
            name='parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]