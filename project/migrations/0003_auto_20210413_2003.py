# Generated by Django 2.2.7 on 2021-04-14 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210413_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samples',
            name='researcher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Researcher'),
        ),
    ]
