# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='refferal_code',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='user_type',
            field=models.CharField(default=b'User', max_length=50, blank=True, choices=[(b'Manager', b'Manager '), (b'CS Team', b'CS Team'), (b'Admin', b'Admin'), (b'User', b'User')]),
        ),
    ]
