# Generated by Django 4.1.7 on 2023-03-21 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listing_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='color',
        ),
    ]
