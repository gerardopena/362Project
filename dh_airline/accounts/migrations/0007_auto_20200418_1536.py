# Generated by Django 3.0.3 on 2020-04-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200418_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='city_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='state_address',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='street_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='zip_address',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
