# Generated by Django 3.0.1 on 2021-05-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('description', models.TextField()),
                ('code', models.URLField()),
                ('deployment', models.URLField()),
            ],
        ),
    ]
