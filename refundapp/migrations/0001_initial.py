# Generated by Django 3.2.18 on 2024-10-30 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salaryapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('is_given', models.BooleanField(default=False)),
                ('bank', models.CharField(choices=[('BNK부산은행', 'BNK부산은행'), ('DGB대구은행', 'DGB대구은행'), ('IBK기업은행', 'IBK기업은행'), ('KB국민은행', 'KB국민은행'), ('MG새마을금고', 'MG새마을금고'), ('SC제일은행', 'SC제일은행'), ('Sh수협은행', 'Sh수협은행'), ('광주은행', '광주은행'), ('농협', '농협'), ('신한은행', '신한은행'), ('신협', '신협'), ('우리은행', '우리은행'), ('우체국은행', '우체국은행'), ('저축은행', '저축은행'), ('카카오뱅크', '카카오뱅크'), ('케이뱅크', '케이뱅크'), ('토스', '토스'), ('하나은행', '하나은행')], max_length=20)),
                ('accountnumber', models.CharField(max_length=30)),
                ('depositor', models.CharField(max_length=6)),
                ('given_at', models.DateTimeField(null=True)),
                ('salary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refund', to='salaryapp.salary')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refund', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
