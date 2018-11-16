# Generated by Django 2.0.7 on 2018-11-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply_subsidy', '0012_applysubsidy_social_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='applysubsidy',
            name='apl_bpl',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='land_area',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='prev_subsidy',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='applysubsidy',
            name='survey_no',
            field=models.CharField(default='', max_length=20),
        ),
    ]