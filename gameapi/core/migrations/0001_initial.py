# Generated by Django 3.2.4 on 2021-06-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, default=None, max_length=60, null=True, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
