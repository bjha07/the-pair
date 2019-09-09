# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, choices=[(b'IT', b'IT'), (b'Operations', b'Operations')])),
                ('added_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_code', models.CharField(max_length=20, null=True, blank=True)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60, null=True, blank=True)),
                ('user_type', models.CharField(default=b'Admin', max_length=50, blank=True, choices=[(b'Manager', b'Manager '), (b'CS Team', b'CS Team'), (b'Admin', b'Admin'), (b'Client', b'Client')])),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('address1', models.CharField(max_length=200, null=True, blank=True)),
                ('address2', models.CharField(max_length=200, null=True, blank=True)),
                ('address3', models.CharField(max_length=200, null=True, blank=True)),
                ('mobile_no', models.CharField(max_length=60)),
                ('login_active', models.IntegerField(default=0)),
                ('staff_status', models.IntegerField(default=0)),
                ('department', models.ForeignKey(to='authentication.Department')),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
