# Generated by Django 2.0.7 on 2018-10-14 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chit_final_draw', '0005_auto_20181014_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitfinaldraw',
            name='chit_month',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
