# Generated by Django 4.2.2 on 2023-08-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0002_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
    ]
