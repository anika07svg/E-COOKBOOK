# Generated by Django 2.2 on 2020-10-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManagement', '0009_auto_20201004_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Food_Img',
        ),
        migrations.AlterField(
            model_name='food',
            name='Food_Category',
            field=models.CharField(max_length=50),
        ),
    ]
