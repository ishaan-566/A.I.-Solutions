# Generated by Django 2.1.1 on 2019-03-12 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190312_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Index',
        ),
    ]
