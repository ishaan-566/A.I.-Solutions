# Generated by Django 2.1.1 on 2019-04-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20190417_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
