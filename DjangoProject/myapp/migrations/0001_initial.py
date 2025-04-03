# Generated by Django 5.1.7 on 2025-03-30 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
