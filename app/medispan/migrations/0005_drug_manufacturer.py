# Generated by Django 2.0.7 on 2018-07-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medispan', '0004_auto_20180717_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
