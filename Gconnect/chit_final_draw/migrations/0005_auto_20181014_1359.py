# Generated by Django 2.0.7 on 2018-10-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chit_final_draw', '0004_auto_20181014_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chitfinaldraw',
            name='chit_month',
        ),
        migrations.AlterField(
            model_name='chitfinaldraw',
            name='chit_install_amount',
            field=models.BigIntegerField(),
        ),
    ]