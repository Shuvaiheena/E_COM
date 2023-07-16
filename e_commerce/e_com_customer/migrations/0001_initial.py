# Generated by Django 4.2.3 on 2023-07-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=25, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('activestate', models.IntegerField(blank=True, default=0, null=True)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('customer_age', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer_details',
                'managed': False,
            },
        ),
    ]