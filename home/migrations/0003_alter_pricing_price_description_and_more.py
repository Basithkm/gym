# Generated by Django 4.1 on 2022-08-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_trainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='price_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='price_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
