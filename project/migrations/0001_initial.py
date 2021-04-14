# Generated by Django 2.2.7 on 2021-04-13 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('orcid', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_id', models.TextField()),
                ('test_dates', models.TextField()),
                ('sample_results', models.TextField()),
                ('test_type', models.TextField()),
                ('sample_type', models.TextField()),
                ('collection_site', models.TextField()),
                ('ct_values', models.TextField()),
                ('researcher', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='project.Researcher')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=400)),
                ('project_title', models.CharField(max_length=400)),
                ('project_description', models.TextField()),
                ('positive_samples', models.PositiveIntegerField()),
                ('negative_samples', models.PositiveIntegerField()),
                ('sample_information', models.TextField()),
                ('date_request', models.TextField(blank=True)),
                ('researcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Researcher')),
            ],
        ),
    ]