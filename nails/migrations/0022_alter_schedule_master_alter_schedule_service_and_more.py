# Generated by Django 4.2.2 on 2023-09-21 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nails', '0021_remove_schedule_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master', to='nails.users'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.services'),
        ),
        migrations.AlterField(
            model_name='services',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialization', to='nails.specializations'),
        ),
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.users'),
        ),
        migrations.AlterField(
            model_name='usertoservices',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.services'),
        ),
        migrations.AlterField(
            model_name='usertoservices',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.specializations'),
        ),
        migrations.AlterField(
            model_name='usertoservices',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.users'),
        ),
        migrations.AlterField(
            model_name='usertospecialization',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nails.users'),
        ),
    ]
