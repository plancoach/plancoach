# Generated by Django 3.2.18 on 2023-07-17 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consult_feedbackapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consult_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_like', to='consult_feedbackapp.consult_feedback')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'consult_feedback')},
            },
        ),
    ]
