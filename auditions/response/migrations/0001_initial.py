# Generated by Django 3.1.6 on 2021-02-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('N', 'NORMAL'), ('I', 'IMAGE')], max_length=1)),
                ('text', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='media.images')),
            ],
        ),
    ]
