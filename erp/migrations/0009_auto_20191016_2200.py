# Generated by Django 2.2.4 on 2019-10-17 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_pagos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagos',
            old_name='informes_text',
            new_name='pagos_text',
        ),
    ]