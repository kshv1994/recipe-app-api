# Generated by Django 2.1.15 on 2020-11-06 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='title',
            new_name='recipe_title',
        ),
    ]
