# Generated by Django 3.0.5 on 2020-05-18 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_project_intial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='actual_installation',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='approval_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_of_completion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='installation_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='intial_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='survey_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='turnaround_time',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]