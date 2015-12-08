# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accuracyallcol',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(null=True, max_length=255)),
                ('prediction', models.IntegerField(null=True)),
                ('original', models.IntegerField(null=True)),
                ('counttrue', models.IntegerField(null=True)),
                ('counttotal', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='accuracyexceptbig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(null=True, max_length=255)),
                ('prediction', models.IntegerField(null=True)),
                ('original', models.IntegerField(null=True)),
                ('counttrue', models.IntegerField(null=True)),
                ('counttotal', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='accuracyonlybig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(null=True, max_length=255)),
                ('prediction', models.IntegerField(null=True)),
                ('original', models.IntegerField(null=True)),
                ('counttrue', models.IntegerField(null=True)),
                ('counttotal', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='predictallcol',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(null=True, max_length=255)),
                ('prediction', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='predictexceptbig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(null=True, max_length=255)),
                ('prediction', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='predictonlybig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(null=True, max_length=255)),
                ('prediction', models.IntegerField(null=True)),
            ],
        ),
    ]
