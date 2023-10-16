# Generated by Django 4.2.2 on 2023-09-16 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0018_servicestoshedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='SheduleStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nails.services'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nails.shedulestatus'),
        ),
    ]
