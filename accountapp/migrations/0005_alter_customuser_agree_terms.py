# Generated by Django 3.2.18 on 2023-08-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0004_customuser_agree_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='agree_terms',
            field=models.BooleanField(),
        ),
    ]
