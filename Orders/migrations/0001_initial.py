# Generated by Django 3.2.5 on 2022-07-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=100)),
            ],
        ),
    ]