# Generated by Django 3.2.18 on 2024-10-30 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacherapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepttype', models.CharField(choices=[('학생부교과', '학생부교과'), ('학생부종합', '학생부종합'), ('논술', '논술'), ('특기자', '특기자'), ('정시', '정시'), ('기타', '기타')], max_length=20, null=True)),
                ('studentid', models.IntegerField(choices=[(9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], null=True)),
                ('schoolimage', models.ImageField(upload_to='teacherapply/')),
                ('userimage', models.ImageField(null=True, upload_to='teacherapply/')),
                ('school', models.CharField(choices=[('가천대학교', '가천대학교'), ('가톨릭관동대학교', '가톨릭관동대학교'), ('가톨릭대학교', '가톨릭대학교'), ('강원대학교', '강원대학교'), ('건국대학교', '건국대학교'), ('건양대학교', '건양대학교'), ('경북대학교', '경북대학교'), ('경상국립대학교', '경상국립대학교'), ('경희대학교', '경희대학교'), ('계명대학교', '계명대학교'), ('고려대학교', '고려대학교'), ('고신대학교', '고신대학교'), ('단국대학교', '단국대학교'), ('대구가톨릭대학교', '대구가톨릭대학교'), ('동국대학교(경주)', '동국대학교(경주)'), ('동아대학교', '동아대학교'), ('부산대학교', '부산대학교'), ('서강대학교', '서강대학교'), ('서울대학교', '서울대학교'), ('서울시립대학교', '서울시립대학교'), ('성균관대학교', '성균관대학교'), ('순천향대학교', '순천향대학교'), ('아주대학교', '아주대학교'), ('연세대학교(서울)', '연세대학교(서울)'), ('연세대학교(미래)', '연세대학교(미래)'), ('영남대학교', '영남대학교'), ('울산대학교', '울산대학교'), ('원광대학교', '원광대학교'), ('을지대학교', '을지대학교'), ('이화여자대학교', '이화여자대학교'), ('인제대학교', '인제대학교'), ('인하대학교', '인하대학교'), ('전남대학교', '전남대학교'), ('전북대학교', '전북대학교'), ('제주대학교', '제주대학교'), ('조선대학교', '조선대학교'), ('중앙대학교', '중앙대학교'), ('차의과학대학교', '차의과학대학교'), ('충남대학교', '충남대학교'), ('충북대학교', '충북대학교'), ('한국외국어대학교', '한국외국어대학교'), ('한림대학교', '한림대학교'), ('한양대학교', '한양대학교'), ('KAIST', 'KAIST'), ('POSTECH', 'POSTECH'), ('UNIST', 'UNIST'), ('DGIST', 'DGIST'), ('GIST', 'GIST')], max_length=20, null=True)),
                ('major', models.CharField(max_length=15, null=True)),
                ('bank', models.CharField(choices=[('BNK부산은행', 'BNK부산은행'), ('DGB대구은행', 'DGB대구은행'), ('IBK기업은행', 'IBK기업은행'), ('KB국민은행', 'KB국민은행'), ('MG새마을금고', 'MG새마을금고'), ('SC제일은행', 'SC제일은행'), ('Sh수협은행', 'Sh수협은행'), ('광주은행', '광주은행'), ('농협', '농협'), ('신한은행', '신한은행'), ('신협', '신협'), ('우리은행', '우리은행'), ('우체국은행', '우체국은행'), ('저축은행', '저축은행'), ('카카오뱅크', '카카오뱅크'), ('케이뱅크', '케이뱅크'), ('토스', '토스'), ('하나은행', '하나은행')], max_length=20, null=True)),
                ('accountnumber', models.CharField(max_length=30, null=True)),
                ('depositor', models.CharField(max_length=6, null=True)),
                ('consulttype', multiselectfield.db.fields.MultiSelectField(choices=[('정시', '정시'), ('내신', '내신'), ('학생부', '학생부'), ('중등', '중등')], max_length=20, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('has_userimage', models.BooleanField(default=False)),
                ('has_schoolimage', models.BooleanField(default=False)),
                ('has_bank', models.BooleanField(default=False)),
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacherapply', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
