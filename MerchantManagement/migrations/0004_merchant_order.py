# Generated by Django 2.2 on 2020-09-20 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderManagement', '0001_initial'),
        ('MerchantManagement', '0003_merchant_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='OrderManagement.Order'),
        ),
    ]
