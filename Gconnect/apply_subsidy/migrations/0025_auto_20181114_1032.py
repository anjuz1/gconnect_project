# Generated by Django 2.0.7 on 2018-11-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_subsidy', '0024_remove_applysubsidy_cons_widow'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='login_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='status',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
