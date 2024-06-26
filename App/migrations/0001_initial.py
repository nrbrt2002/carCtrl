# Generated by Django 5.0.2 on 2024-06-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('fixed', 'Fixed'), ('portable', 'Portable')], max_length=50)),
                ('operating_hours', models.CharField(choices=[('9:00 AM - 5:00 AM', '9:00 AM - 5:00 PM'), ('10:00 AM - 5:00 AM', '10:00 AM - 5:00 PM')], max_length=50)),
                ('number_of_slots_per_day', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
