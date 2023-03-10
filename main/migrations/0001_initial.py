# Generated by Django 4.0.4 on 2023-01-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestersRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('flex_timings', models.BooleanField()),
                ('no_of_assets', models.IntegerField()),
                ('asset_types', models.CharField(choices=[('LAPTOP', 'LAPTOP'), ('PACKAGE', 'PACKAGE'), ('TRAVEL_BAG', 'TRAVEL_BAG')], max_length=20)),
                ('asset_sensitive', models.CharField(choices=[('HIGHLY_SENSITIVE', 'HIGHLY_SENSITIVE'), ('NORMAL', 'NORMAL'), ('SENSITIVE', 'SENSITIVE')], max_length=20)),
                ('whom_to_deliver', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RiderRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField()),
                ('flex_timings', models.BooleanField()),
                ('travel_medium', models.CharField(choices=[('BUS', 'BUS'), ('CAR', 'CAR'), ('TRAIN', 'TRAIN')], max_length=20)),
                ('asset_quantity', models.IntegerField()),
            ],
        ),
    ]
