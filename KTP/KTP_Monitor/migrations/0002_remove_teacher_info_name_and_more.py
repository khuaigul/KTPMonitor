# Generated by Django 4.1.7 on 2023-04-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KTP_Monitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_info',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacher_info',
            name='phone_num',
        ),
        migrations.AddField(
            model_name='teacher_info',
            name='firstname',
            field=models.CharField(default='ooo', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher_info',
            name='lastname',
            field=models.CharField(default='ooo', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher_info',
            name='phone',
            field=models.CharField(default='123', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher_info',
            name='secondname',
            field=models.CharField(default='ooo', max_length=100),
        ),
    ]
