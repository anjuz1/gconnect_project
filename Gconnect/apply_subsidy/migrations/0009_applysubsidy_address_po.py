# Generated by Django 2.0.7 on 2018-11-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_subsidy', '0008_applysubsidy_address_hname'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='Address_po',
            field=models.CharField(default='', max_length=20),
        ),
    ]
