# Generated by Django 4.0.3 on 2022-03-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('date_time', models.DateField(auto_now=True)),
                ('weather', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]