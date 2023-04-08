# Generated by Django 4.1.1 on 2023-04-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Div_Info',
            fields=[
                ('div_id', models.AutoField(primary_key=True, serialize=False)),
                ('div_year', models.IntegerField()),
                ('div_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('/menu', ''), ('/signin', '')),
            },
        ),
    ]
