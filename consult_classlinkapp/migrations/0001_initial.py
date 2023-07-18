# Generated by Django 3.2.18 on 2023-07-17 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult_classlink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekdate', models.CharField(choices=[('월요일', '월요일'), ('화요일', '화요일'), ('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일'), ('토요일', '토요일'), ('일요일', '일요일')], max_length=20)),
                ('classtime', models.CharField(max_length=15)),
                ('link', models.TextField(max_length=100)),
                ('consult', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consult_classlink', to='consultapp.consult')),
            ],
        ),
    ]
