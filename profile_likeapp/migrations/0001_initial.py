# Generated by Django 3.2.18 on 2023-12-09 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profileapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_like', to='profileapp.profile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'profile')},
            },
        ),
    ]
