# Generated by Django 2.1.15 on 2020-11-06 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201106_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_title',
            new_name='title',
        ),
    ]
