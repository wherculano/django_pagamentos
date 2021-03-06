# Generated by Django 3.2.8 on 2021-10-17 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('referred_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.client')),
            ],
        ),
    ]
