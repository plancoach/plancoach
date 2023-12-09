# Generated by Django 3.2.18 on 2023-12-09 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_profileimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_profileimage/')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_profileimage', to='profileapp.profile')),
            ],
        ),
    ]
