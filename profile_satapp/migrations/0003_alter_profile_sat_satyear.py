# Generated by Django 3.2.18 on 2023-06-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_satapp', '0002_alter_profile_sat_satyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_sat',
            name='satyear',
            field=models.IntegerField(choices=[(12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35)]),
        ),
    ]
