# Generated by Django 4.1.7 on 2023-03-20 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship_app', '0006_remove_personal_information_male_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_information',
            name='Male',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='Female',
            field=models.BooleanField(default=False),
        ),
    ]