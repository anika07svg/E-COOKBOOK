# Generated by Django 2.2 on 2020-09-20 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerManagement', '0004_auto_20200920_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='bill',
        ),
    ]
