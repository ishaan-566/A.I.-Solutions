# Generated by Django 2.1.1 on 2019-04-15 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_register_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Bill')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Cart')),
            ],
        ),
    ]