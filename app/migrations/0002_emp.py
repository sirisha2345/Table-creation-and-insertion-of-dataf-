# Generated by Django 4.2.7 on 2024-01-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('empno', models.IntegerField()),
                ('empid', models.IntegerField()),
                ('emploc', models.CharField(max_length=100)),
            ],
        ),
    ]
