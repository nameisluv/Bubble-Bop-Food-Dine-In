# Generated by Django 3.0.3 on 2022-08-16 19:25

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('final_amt', models.FloatField(default=0)),
                ('items', jsonfield.fields.JSONField()),
                ('user', jsonfield.fields.JSONField()),
                ('status', models.CharField(default='unpaid', max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('number', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('tableNo', models.IntegerField(default=0)),
                ('otp', models.IntegerField(default=0)),
                ('otp_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
