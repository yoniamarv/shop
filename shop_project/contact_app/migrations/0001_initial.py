# Generated by Django 2.1.3 on 2018-12-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264)),
                ('text', models.TextField(max_length=264)),
            ],
        ),
    ]
