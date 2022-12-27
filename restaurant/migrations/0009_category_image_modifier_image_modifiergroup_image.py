# Generated by Django 4.1.4 on 2022-12-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.AddField(
            model_name='modifier',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='modifiers/'),
        ),
        migrations.AddField(
            model_name='modifiergroup',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='modifiergroups/'),
        ),
    ]