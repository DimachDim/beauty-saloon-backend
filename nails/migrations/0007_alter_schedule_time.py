# Generated by Django 4.2.2 on 2023-08-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0006_schedule_date_schedule_mark_schedule_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
