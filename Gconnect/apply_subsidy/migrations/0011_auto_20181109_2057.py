# Generated by Django 2.0.7 on 2018-11-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_subsidy', '0010_auto_20181109_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='ward_hno_new',
            field=models.BigIntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='ward_hno_old',
            field=models.BigIntegerField(default=23),
            preserve_default=False,
        ),
    ]