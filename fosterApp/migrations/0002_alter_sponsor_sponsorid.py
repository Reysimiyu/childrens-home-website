# Generated by Django 4.2 on 2023-08-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fosterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsorId',
            field=models.CharField(max_length=10),
        ),
    ]
