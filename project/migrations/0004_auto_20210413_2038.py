# Generated by Django 2.2.7 on 2021-04-14 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210413_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samples',
            name='ct_values',
            field=models.TextField(blank=True, null=True),
        ),
    ]