# Generated by Django 4.1.7 on 2023-03-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=200)),
                ('DateOfBirth', models.DateField()),
                ('Address', models.TextField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.CharField(max_length=50)),
            ],
        ),
    ]
