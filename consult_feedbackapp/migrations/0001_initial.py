# Generated by Django 3.2.18 on 2023-12-12 00:47

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', multiselectfield.db.fields.MultiSelectField(choices=[('국어', '국어'), ('영어', '영어'), ('수학', '수학'), ('물리', '물리'), ('지구과학', '지구과학'), ('화학', '화학'), ('생명과학', '생명과학'), ('통합과학', '통합과학'), ('생활과윤리', '생활과윤리'), ('윤리와사상', '윤리와사상'), ('한국지리', '한국지리'), ('세계지리', '세계지리'), ('동아시아사', '동아시아사'), ('세계사', '세계사'), ('경제', '경제'), ('정치와법', '정치와법'), ('사회문화', '사회문화'), ('통합사회', '통합사회'), ('한국사', '한국사'), ('예체능', '예체능'), ('기타', '기타')], max_length=100)),
                ('content', models.TextField(max_length=1000, null=True)),
                ('todo', models.TextField(max_length=1000, null=True)),
                ('classtime', models.DateField()),
                ('consult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consult_feedback', to='consultapp.consult')),
            ],
            options={
                'unique_together': {('consult', 'classtime')},
            },
        ),
    ]
