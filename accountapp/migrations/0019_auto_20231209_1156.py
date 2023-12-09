# Generated by Django 3.2.18 on 2023-12-09 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0018_alter_customuser_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='signup_at',
            field=models.DateField(default=datetime.date(2023, 12, 9)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
