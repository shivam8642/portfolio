# Generated by Django 4.1.6 on 2023-02-02 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
