# Generated by Django 4.1.7 on 2023-04-25 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Div_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('/menu', ''), ('/signin', ''), ('/sendProfileData', ''), ('/teacherProfile', ''), ('/viewProfileData', ''), ('/editTeacherProfile', ''), ('/pupilProfile', '')),
            },
        ),
        migrations.CreateModel(
            name='Teacher_Info',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('lastname', models.CharField(default='ooo', max_length=100)),
                ('firstname', models.CharField(default='ooo', max_length=100)),
                ('secondname', models.CharField(default='ooo', max_length=100)),
                ('CF', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='123', max_length=100)),
                ('div_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='KTP_Monitor.div_info')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil_Info',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('secondname', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('CF', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('e_mail', models.EmailField(max_length=254)),
                ('phone', models.SlugField()),
                ('div_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='KTP_Monitor.div_info')),
            ],
        ),
    ]
