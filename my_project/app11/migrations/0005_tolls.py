# Generated by Django 3.0.4 on 2020-03-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tolls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.IntegerField(max_length=15, unique=True)),
                ('t_name', models.CharField(max_length=50)),
                ('t_percent', models.IntegerField(max_length=20)),
            ],
        ),
    ]
