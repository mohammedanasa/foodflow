# Generated by Django 4.1.4 on 2022-12-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_modifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='restaurant.category'),
        ),
    ]