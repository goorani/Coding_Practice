# Generated by Django 5.0.4 on 2024-04-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
            ],
        ),
    ]