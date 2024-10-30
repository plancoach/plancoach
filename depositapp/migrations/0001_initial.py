# Generated by Django 3.2.18 on 2024-10-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(choices=[('BNK부산은행', 'BNK부산은행'), ('DGB대구은행', 'DGB대구은행'), ('IBK기업은행', 'IBK기업은행'), ('KB국민은행', 'KB국민은행'), ('MG새마을금고', 'MG새마을금고'), ('SC제일은행', 'SC제일은행'), ('Sh수협은행', 'Sh수협은행'), ('광주은행', '광주은행'), ('농협', '농협'), ('신한은행', '신한은행'), ('신협', '신협'), ('우리은행', '우리은행'), ('우체국은행', '우체국은행'), ('저축은행', '저축은행'), ('카카오뱅크', '카카오뱅크'), ('케이뱅크', '케이뱅크'), ('토스', '토스'), ('하나은행', '하나은행')], max_length=20)),
                ('accountnumber', models.CharField(max_length=30)),
                ('depositor', models.CharField(max_length=20)),
            ],
        ),
    ]
