# Generated by Django 2.0.7 on 2018-07-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_auto_20180728_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notpreferred',
            name='not_preferred_drug_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='preferred',
            name='preferred_drug_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
