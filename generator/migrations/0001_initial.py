# Generated by Django 4.0.1 on 2022-01-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=100)),
                ('INN', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=100)),
                ('citizenship', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
            ],
        ),
    ]
