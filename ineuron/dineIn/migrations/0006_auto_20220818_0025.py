# Generated by Django 3.0.3 on 2022-08-17 18:55

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dineIn', '0005_auto_20220818_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='items',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='user',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
