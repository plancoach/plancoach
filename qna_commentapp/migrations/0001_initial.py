# Generated by Django 3.2.18 on 2024-10-30 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consult_qnaapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Qna_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='qna_comment/')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('consult_qna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qna_comment', to='consult_qnaapp.consult_qna')),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qna_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
