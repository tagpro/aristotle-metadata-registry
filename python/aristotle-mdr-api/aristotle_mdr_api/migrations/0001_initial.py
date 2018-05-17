# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-17 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='AristotleToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.Token')),
                ('permissions', jsonfield.fields.JSONField()),
            ],
            bases=('authtoken.token',),
        ),
    ]
