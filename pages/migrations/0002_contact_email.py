# Generated by Django 2.2.7 on 2021-03-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='noemail@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
