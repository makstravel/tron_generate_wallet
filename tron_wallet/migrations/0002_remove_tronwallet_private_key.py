# Generated by Django 5.1.6 on 2025-03-08 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tron_wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tronwallet',
            name='private_key',
        ),
    ]
