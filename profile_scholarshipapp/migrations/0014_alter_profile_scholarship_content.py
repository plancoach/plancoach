# Generated by Django 3.2.18 on 2023-07-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_scholarshipapp', '0013_alter_profile_scholarship_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_scholarship',
            name='content',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
