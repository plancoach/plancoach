# Generated by Django 3.2.18 on 2024-10-30 09:14

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
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('graden', 'N수'), ('grade3', '3학년'), ('grade2', '2학년'), ('grade1', '1학년'), ('middle', '중등')], max_length=20)),
                ('belong', models.CharField(max_length=8)),
                ('want', models.TextField(max_length=500)),
                ('problem', models.TextField(max_length=500)),
                ('strategy', models.TextField(max_length=500)),
                ('state', models.CharField(choices=[('applied', '신청완료'), ('matching', '매칭중')], default='applied', max_length=20)),
                ('updated_at', models.DateTimeField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application_student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
