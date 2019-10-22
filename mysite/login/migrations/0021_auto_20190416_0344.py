# Generated by Django 2.1.1 on 2019-04-15 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20190306_2348'),
        ('login', '0020_auto_20190416_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='item',
        ),
        migrations.AddField(
            model_name='log',
            name='Quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='log',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='company.Product'),
        ),
    ]