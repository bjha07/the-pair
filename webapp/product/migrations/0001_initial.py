# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190525_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('name_referral_by', models.CharField(max_length=50, null=True, blank=True)),
                ('name_referral_to', models.CharField(max_length=50, null=True, blank=True)),
                ('code_referral_by', models.CharField(max_length=50, null=True, blank=True)),
                ('code_referral_to', models.CharField(max_length=50, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalletMoney',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('value', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=100, null=True, blank=True)),
                ('employee_code', models.ForeignKey(related_name='walletmoney', blank=True, to='authentication.EmployeeMaster', null=True)),
                ('referralemployee', models.ForeignKey(blank=True, to='product.ReferralEmployee', null=True)),
            ],
        ),
    ]
