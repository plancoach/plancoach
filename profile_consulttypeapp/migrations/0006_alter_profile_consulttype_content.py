# Generated by Django 3.2.18 on 2023-07-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_consulttypeapp', '0005_alter_profile_consulttype_consulttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_consulttype',
            name='content',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
