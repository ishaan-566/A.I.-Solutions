# Generated by Django 2.1.1 on 2019-03-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_remove_register_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='user/%Y/%m/%d'),
        ),
    ]
