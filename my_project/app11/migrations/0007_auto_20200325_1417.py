# Generated by Django 3.0.4 on 2020-03-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0006_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_sub_title', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill_sub_title',
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_title',
            field=models.CharField(blank=True, default=0, max_length=50, null=True),
        ),
    ]
