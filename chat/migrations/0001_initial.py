# Generated by Django 2.1.4 on 2018-12-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('sex', models.TextField()),
                ('birth', models.DateField(auto_now_add=True)),
                ('smoker', models.BooleanField(default=False)),
                ('answerIndex', models.IntegerField(default=1)),
            ],
        ),
    ]
