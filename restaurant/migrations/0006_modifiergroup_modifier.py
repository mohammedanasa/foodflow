# Generated by Django 4.1.4 on 2022-12-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifiergroup',
            name='modifier',
            field=models.ManyToManyField(blank=True, null=True, to='restaurant.modifier'),
        ),
    ]
