# Generated by Django 2.1.1 on 2019-03-27 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_register_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='image',
        ),
    ]