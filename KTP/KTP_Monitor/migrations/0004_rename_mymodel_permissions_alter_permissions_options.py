# Generated by Django 4.1.7 on 2023-04-09 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KTP_Monitor', '0003_alter_mymodel_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyModel',
            new_name='Permissions',
        ),
        migrations.AlterModelOptions(
            name='permissions',
            options={'permissions': (('/menu', ''), ('/signin', ''), ('/sendProfileData', ''), ('/teacherProfile', ''))},
        ),
    ]
