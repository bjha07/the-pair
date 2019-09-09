# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.ForeignKey(blank=True, to='product.BrandName', null=True),
        ),
    ]
