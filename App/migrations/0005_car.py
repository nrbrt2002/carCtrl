# Generated by Django 5.0.6 on 2024-06-19 11:05

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_owner_options_owner_groups_owner_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=50)),
                ('make', models.TextField(max_length=50)),
                ('plate', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='Plate number needd to be formated like AAA 000 A', regex='^[A-Z]{3} [0-9]{3} [A-Z]$')])),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
