# Generated by Django 3.2.18 on 2023-12-09 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consult_qnaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qna_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consult_qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qna_like', to='consult_qnaapp.consult_qna')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qna_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'consult_qna')},
            },
        ),
    ]
