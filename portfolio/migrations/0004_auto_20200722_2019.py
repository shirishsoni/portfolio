# Generated by Django 3.0.8 on 2020-07-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200722_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languages',
            name='type',
            field=models.CharField(max_length=25),
        ),
    ]
