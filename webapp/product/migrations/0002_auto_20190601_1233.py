# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferDiscount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('discount', models.IntegerField(default=0, null=True, blank=True)),
                ('price', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('code', models.CharField(max_length=50, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('color', models.CharField(max_length=50, null=True, blank=True)),
                ('model_name', models.CharField(max_length=100, null=True, blank=True)),
                ('warranty', models.CharField(max_length=50, null=True, blank=True)),
                ('ideal_for', models.CharField(default=b'MEN', max_length=50, blank=True, choices=[(b'MEN', b'MEN'), (b'WOMEN', b'WOMEN')])),
                ('description', models.CharField(max_length=500, null=True, blank=True)),
                ('product_type', models.CharField(default=b'SPORT', max_length=50, blank=True, choices=[(b'SPORT', b'SPORT'), (b'CASUAL', b'CASUAL')])),
                ('orignal_price', models.IntegerField(default=0, null=True, blank=True)),
                ('actual_price', models.IntegerField(default=0, null=True, blank=True)),
                ('discount', models.IntegerField(default=0, null=True, blank=True)),
                ('product_image', models.CharField(max_length=200, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('offer_discount', models.ForeignKey(blank=True, to='product.OfferDiscount', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('image1', models.CharField(max_length=200, null=True, blank=True)),
                ('image2', models.CharField(max_length=200, null=True, blank=True)),
                ('image3', models.CharField(max_length=200, null=True, blank=True)),
                ('image4', models.CharField(max_length=200, null=True, blank=True)),
                ('image5', models.CharField(max_length=200, null=True, blank=True)),
                ('product', models.ForeignKey(blank=True, to='product.Product', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('size_from', models.IntegerField(default=0, null=True, blank=True)),
                ('size_to', models.IntegerField(default=0, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.ForeignKey(blank=True, to='product.ProductSize', null=True),
        ),
    ]
