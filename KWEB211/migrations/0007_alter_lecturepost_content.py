# Generated by Django 3.2.3 on 2021-06-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KWEB211', '0006_alter_lecturepost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturepost',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
