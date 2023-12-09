# Generated by Django 3.2.18 on 2023-12-09 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Refusal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('matching', '매칭 종료'), ('consult', '컨설팅 종료'), ('teacherapply', '컨설팅 신청 종료'), ('refund', '컨설팅 환불 완료')], default='matching', max_length=30)),
                ('content', models.CharField(max_length=21, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='refusal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
