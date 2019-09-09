# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20190601_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='product.ProductColor', null=True, blank=True),
        ),
    ]
