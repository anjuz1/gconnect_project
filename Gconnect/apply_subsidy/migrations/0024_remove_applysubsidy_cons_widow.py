# Generated by Django 2.0.7 on 2018-11-14 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply_subsidy', '0023_applysubsidy_cons_widow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applysubsidy',
            name='cons_widow',
        ),
    ]
