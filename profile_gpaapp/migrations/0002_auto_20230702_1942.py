# Generated by Django 3.2.18 on 2023-07-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_gpaapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile_gpa',
            name='gpaactivityverificationimage',
        ),
        migrations.RemoveField(
            model_name='profile_gpa',
            name='gpascoreverificationimage',
        ),
        migrations.RemoveField(
            model_name='profile_gpa',
            name='record',
        ),
        migrations.AddField(
            model_name='profile_gpa',
            name='gpaverificationimage',
            field=models.ImageField(blank=True, null=True, upload_to='profile_gpa/'),
        ),
    ]
