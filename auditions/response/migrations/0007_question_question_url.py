# Generated by Django 3.1.6 on 2022-03-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0006_alter_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_url',
            field=models.URLField(default='tinkercad.com', max_length=400),
            preserve_default=False,
        ),
    ]
