# Generated by Django 3.2.18 on 2023-12-27 23:23

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
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('unextended', '미연장'), ('extended', '연장'), ('new', '신규')], default='new', max_length=20)),
                ('age', models.CharField(choices=[('graden', 'N수'), ('grade3', '3학년'), ('grade2', '2학년'), ('grade1', '1학년'), ('middle', '중등')], max_length=20)),
                ('belong', models.CharField(max_length=8)),
                ('tuition', models.IntegerField()),
                ('startdate', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('want', models.TextField(max_length=500)),
                ('problem', models.TextField(max_length=500)),
                ('strategy', models.TextField(max_length=500)),
                ('is_warned', models.BooleanField(default=False)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consult_student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consult_teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
