# Generated by Django 5.1.3 on 2024-11-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('user_role', models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('customer', 'Customer')], default='Customer', max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('date_joined', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]