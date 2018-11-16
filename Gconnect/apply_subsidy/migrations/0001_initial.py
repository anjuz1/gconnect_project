# Generated by Django 2.0.7 on 2018-10-28 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subsidy_types', '0001_initial'),
        ('subsidy_priority', '0003_auto_20181014_1509'),
        ('members', '0005_auto_20180924_2016'),
        ('subsidy_elig', '0004_subsidyeligibility_subsidy_ftype'),
        ('housename', '0005_auto_20180925_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplySubsidy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address_po', models.CharField(default='', max_length=20)),
                ('Address_road', models.CharField(default='', max_length=20)),
                ('mob', models.CharField(default='', max_length=10)),
                ('ward_hno_old', models.BigIntegerField()),
                ('ward_hno_new', models.BigIntegerField()),
                ('social_cat', models.CharField(default='', max_length=20)),
                ('land_area', models.CharField(default='', max_length=20)),
                ('survey_no', models.CharField(default='', max_length=20)),
                ('prev_subsidy', models.CharField(default='', max_length=20)),
                ('apl_bpl', models.CharField(default='', max_length=10)),
                ('special1_consideration', models.CharField(default='', max_length=20)),
                ('mental_physical_challenge', models.CharField(default='', max_length=10)),
                ('house_typ', models.CharField(default='', max_length=20)),
                ('ration_card_no', models.CharField(default='', max_length=20)),
                ('adhar_card_no', models.CharField(default='', max_length=20)),
                ('voter_id', models.CharField(default='', max_length=20)),
                ('form_priority_list', models.CharField(default='', max_length=40)),
                ('form_mark_list', models.BigIntegerField()),
                ('login_id', models.BigIntegerField()),
                ('Address_hname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housename.Housename')),
                ('applicant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
                ('first_elig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subsidy_elig.SubsidyEligibility')),
                ('first_prio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subsidy_priority.SubsidyPriority')),
                ('sub_typ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subsidy_types.SubsidyTypes')),
            ],
        ),
    ]