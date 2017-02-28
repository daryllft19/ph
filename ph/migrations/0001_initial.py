# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=100)),
                ('is_serviceable', models.BooleanField(default=True)),
                ('cluster', models.ForeignKey(to='ph.Cluster')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('x1', models.FloatField()),
                ('x2', models.FloatField()),
                ('y1', models.FloatField()),
                ('y2', models.FloatField()),
                ('z1', models.FloatField()),
                ('z2', models.FloatField()),
                ('arrival_date', models.DateTimeField(auto_now_add=True)),
                ('is_fragile', models.BooleanField(default=False)),
                ('location', models.ForeignKey(to='ph.Location')),
            ],
        ),
    ]
