# Generated by Django 5.0.2 on 2024-02-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wetherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=100)),
                ('coord', models.CharField(max_length=30)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=20)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=20)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]