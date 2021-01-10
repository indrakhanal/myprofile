# Generated by Django 3.0.4 on 2020-03-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('subject', models.CharField(blank=True, max_length=40, null=True)),
                ('message', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]