# Generated by Django 2.2.7 on 2021-03-22 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20210322_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.Person'),
            preserve_default=False,
        ),
    ]
