# Generated by Django 2.2.13 on 2020-06-21 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20200621_1234'),
        ('individual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='person_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Person'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='lose_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 21, 3, 49, 467284)),
        ),
    ]
