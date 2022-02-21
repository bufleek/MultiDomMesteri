# Generated by Django 4.0 on 2022-02-20 20:00

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', accounts.models.Email(max_length=255, unique=True, verbose_name='email address')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('INDIVIDUAL', 'INDIVIDUAL'), ('COMPANY', 'COMPANY')], default='INDIVIDUAL', max_length=25)),
                ('team', models.CharField(choices=[('1-3', '1-3'), ('3-5', '3-5'), ('5-10', '5-10')], default='1-3', max_length=25)),
                ('experience', models.IntegerField(null=True)),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('company_name', models.CharField(blank=True, max_length=64)),
                ('about', models.TextField(blank=True, max_length=265)),
                ('address', models.TextField(blank=True, max_length=265)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('mobile', models.CharField(blank=True, max_length=64)),
                ('profile_picture', models.ImageField(blank=True, upload_to=accounts.models.upload_profile_picture)),
                ('price_estimate', models.BooleanField(default=False)),
                ('cleaning', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_suggested', models.BooleanField(default=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.role')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(blank=True, upload_to=accounts.models.upload_project_picture)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='services',
            field=models.ManyToManyField(to='accounts.Service'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]
