# Generated by Django 4.2.2 on 2023-09-15 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0011_usertoservices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertospecialization',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.specializations'),
        ),
    ]
