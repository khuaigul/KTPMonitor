# Generated by Django 4.1.7 on 2023-04-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KTP_Monitor', '0004_alter_myuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]