# Generated by Django 4.1.4 on 2023-01-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_recipe_cooktime_recipe_recipe_des_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_date',
            field=models.DateField(blank=True),
        ),
    ]
