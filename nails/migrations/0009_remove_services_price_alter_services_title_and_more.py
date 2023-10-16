# Generated by Django 4.2.2 on 2023-08-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0008_specializations_services_users_specialization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='price',
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='sid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='specializations',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastName',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
