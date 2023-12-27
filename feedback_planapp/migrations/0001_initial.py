# Generated by Django 3.2.18 on 2023-12-27 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consult_feedbackapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantime', models.DateField()),
                ('content', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('consult_feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_plan', to='consult_feedbackapp.consult_feedback')),
            ],
        ),
    ]
