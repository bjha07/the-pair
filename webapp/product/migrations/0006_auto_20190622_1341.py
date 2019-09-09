# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190601_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('dashboard_image1', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('dashboard_image2', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('dashboard_image3', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('dashboard_image4', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('dashboard_image5', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('referral_image', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('other_image', models.FileField(null=True, upload_to=b'dashboard_images', blank=True)),
                ('other', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('image', models.FileField(null=True, upload_to=b'dashboard', blank=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='brandname',
            name='image',
            field=models.FileField(null=True, upload_to=b'dashboard', blank=True),
        ),
        migrations.AddField(
            model_name='dashboarddetails',
            name='brand_name',
            field=models.ForeignKey(blank=True, to='product.BrandName', null=True),
        ),
        migrations.AddField(
            model_name='dashboarddetails',
            name='product_type',
            field=models.ForeignKey(blank=True, to='product.ProductType', null=True),
        ),
    ]
