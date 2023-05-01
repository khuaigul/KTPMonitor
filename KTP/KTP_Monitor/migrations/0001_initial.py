# Generated by Django 4.1.7 on 2023-05-01 19:08

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
            name='Contest_Div',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Contest_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
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
                'permissions': (('/menu', ''), ('/signin', ''), ('/sendProfileData', ''), ('/teacherProfile', ''), ('/viewProfileData', ''), ('/editTeacherProfile', ''), ('/pupilProfile', ''), ('/divisions', ''), ('/div_info', ''), ('/pupil', ''), ('/contest', ''), ('/contests', ''), ('/divisionStats', '')),
            },
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
                ('div', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='KTP_Monitor.div_info')),
            ],
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
                ('div', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='KTP_Monitor.div_info')),
            ],
        ),
        migrations.CreateModel(
            name='Task_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=100, null=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KTP_Monitor.contest_info')),
            ],
        ),
        migrations.CreateModel(
            name='Pupil_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnt_try', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=100, null=True)),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KTP_Monitor.pupil_info')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KTP_Monitor.task_info')),
            ],
        ),
        migrations.AddField(
            model_name='contest_info',
            name='divs',
            field=models.ManyToManyField(through='KTP_Monitor.Contest_Div', to='KTP_Monitor.div_info'),
        ),
        migrations.AddField(
            model_name='contest_div',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KTP_Monitor.contest_info'),
        ),
        migrations.AddField(
            model_name='contest_div',
            name='div',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KTP_Monitor.div_info'),
        ),
    ]
