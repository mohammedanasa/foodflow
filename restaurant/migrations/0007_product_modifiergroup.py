# Generated by Django 4.1.4 on 2022-12-26 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_modifiergroup_modifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modifiergroup',
            field=models.ManyToManyField(blank=True, null=True, to='restaurant.modifiergroup'),
        ),
    ]
