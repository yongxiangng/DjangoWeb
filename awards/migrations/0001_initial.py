# Generated by Django 3.0.1 on 2021-05-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
