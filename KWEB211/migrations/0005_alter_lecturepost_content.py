# Generated by Django 3.2.3 on 2021-06-03 12:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KWEB211', '0004_auto_20210523_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturepost',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
