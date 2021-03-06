# Generated by Django 2.1.1 on 2019-03-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20190306_2348'),
        ('login', '0004_remove_cart_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='company',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='description',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Register'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='company.Product'),
        ),
    ]
