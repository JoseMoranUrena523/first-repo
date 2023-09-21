# Generated by Django 4.2.5 on 2023-09-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.IntegerField(default=6)),
                ('bookingdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField(default=5)),
            ],
        ),
    ]