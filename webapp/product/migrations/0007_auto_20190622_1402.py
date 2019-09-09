# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190622_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboarddetails',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='dashboarddetails',
            name='product_type',
        ),
        migrations.AddField(
            model_name='brandname',
            name='dashboard_details',
            field=models.ForeignKey(blank=True, to='product.DashboardDetails', null=True),
        ),
        migrations.AddField(
            model_name='producttype',
            name='dashboard_details',
            field=models.ForeignKey(blank=True, to='product.DashboardDetails', null=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='dashboard_image1',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='dashboard_image2',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='dashboard_image3',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='dashboard_image4',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='dashboard_image5',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='other_image',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AlterField(
            model_name='dashboarddetails',
            name='referral_image',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
    ]
