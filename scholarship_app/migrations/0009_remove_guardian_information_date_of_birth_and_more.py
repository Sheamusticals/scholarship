# Generated by Django 4.1.7 on 2023-03-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship_app', '0008_remove_personal_information_female_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian_information',
            name='Date_Of_Birth',
        ),
        migrations.AddField(
            model_name='guardian_information',
            name='Guardian',
            field=models.CharField(choices=[('father', 'Father'), ('mother', 'Mother')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='Address',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='Date_Of_Birth',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='First_Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
