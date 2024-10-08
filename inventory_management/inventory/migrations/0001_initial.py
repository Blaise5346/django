# Generated by Django 5.1 on 2024-08-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.TextField()),
                ('entry_date', models.DateField()),
                ('taken_date', models.DateField(blank=True, null=True)),
                ('item_came_from', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
