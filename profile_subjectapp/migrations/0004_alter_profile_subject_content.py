# Generated by Django 3.2.18 on 2023-07-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_subjectapp', '0003_alter_profile_subject_subjectclassification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_subject',
            name='content',
            field=models.TextField(max_length=300),
        ),
    ]
