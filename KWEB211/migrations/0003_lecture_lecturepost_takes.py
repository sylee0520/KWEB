# Generated by Django 3.2.3 on 2021-05-23 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KWEB211', '0002_alter_account_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturename', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.ForeignKey(db_column='lecture_id', on_delete=django.db.models.deletion.CASCADE, to='KWEB211.lecture')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='KWEB211.account')),
            ],
        ),
        migrations.CreateModel(
            name='LecturePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecture_id', models.ForeignKey(db_column='lecture_id', on_delete=django.db.models.deletion.CASCADE, to='KWEB211.lecture')),
            ],
        ),
    ]
