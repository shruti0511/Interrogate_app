# Generated by Django 3.2.3 on 2021-07-07 13:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0011_remove_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
