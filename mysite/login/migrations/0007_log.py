# Generated by Django 2.1.1 on 2019-03-26 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_cart_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Cart')),
            ],
        ),
    ]
