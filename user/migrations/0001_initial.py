# Generated by Django 2.2.13 on 2020-06-21 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0005_auto_20200621_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=200)),
                ('person_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Person')),
            ],
        ),
    ]
