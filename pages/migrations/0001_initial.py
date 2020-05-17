# Generated by Django 3.0.5 on 2020-05-14 19:35

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact_id', models.IntegerField()),
                ('number_of_signs', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('sign_permit', models.IntegerField()),
                ('engineering', models.IntegerField()),
                ('discount', models.FloatField()),
                ('cash_discount', models.IntegerField()),
                ('discount_total', models.IntegerField()),
                ('deposit_amount', models.IntegerField()),
                ('completion_amount', models.IntegerField()),
                ('final_total', models.IntegerField()),
                ('intial_date', models.DateField()),
                ('survey_date', models.DateField()),
                ('approval_date', models.DateField()),
                ('sign_permit_details', models.TextField()),
                ('landlord_approval_details', models.TextField()),
                ('artwork_approved', models.BooleanField(default=False)),
                ('contract_approved', models.BooleanField(default=False)),
                ('legal_description', models.TextField()),
                ('general_contractor_name', models.CharField(max_length=200)),
                ('electrician_name', models.CharField(max_length=200)),
                ('turnaround_time', models.DateField()),
                ('actual_installation', models.DateField()),
                ('production_notes', models.TextField()),
                ('installation_date', models.DateField()),
                ('date_of_completion', models.DateField()),
                ('job_description', models.TextField()),
                ('special_colors_materials', models.TextField()),
            ],
        ),
    ]
