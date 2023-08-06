# Generated by Django 4.2.4 on 2023-08-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_performance', models.TimeField(null=True)),
                ('time_created', models.TimeField(auto_now_add=True)),
                ('time_changed', models.TimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
                ('date_start', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('time', models.TimeField(auto_now=True)),
                ('telegram', models.CharField(max_length=100, null=True)),
                ('annotation', models.JSONField(null=True)),
            ],
        ),
    ]
