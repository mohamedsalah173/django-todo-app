# Generated by Django 4.2 on 2023-04-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=50)),
                ('isFav', models.BooleanField()),
                ('iscompleted', models.BooleanField()),
            ],
        ),
    ]
