# Generated by Django 4.1.2 on 2022-10-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=250)),
                ('github', models.CharField(max_length=250)),
                ('deploy', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
