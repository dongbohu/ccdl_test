# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('source_type', models.CharField(max_length=256)),
                ('size_in_bytes', models.IntegerField()),
                ('download_url', models.CharField(max_length=4096)),
                ('raw_format', models.CharField(max_length=256, null=True)),
                ('processed_format', models.CharField(max_length=256, null=True)),
                ('pipeline_required', models.CharField(max_length=256)),
                ('platform_accession_code', models.CharField(max_length=32)),
                ('experiment_accession_code', models.CharField(max_length=32)),
                ('experiment_title', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
                ('last_uploaded_date', models.DateField()),
                ('name', models.CharField(max_length=1024)),
                ('internal_location', models.CharField(max_length=256, null=True)),
                ('organism_id', models.IntegerField()),
                ('organism_name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'batches',
            },
        ),
        migrations.CreateModel(
            name='BatchKeyValue',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('key', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('batch', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='data_refinery_common.Batch')),
            ],
            options={
                'db_table': 'batch_key_values',
            },
        ),
        migrations.CreateModel(
            name='DownloaderJob',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('success', models.NullBooleanField()),
                ('num_retries', models.IntegerField(default=0)),
                ('retried', models.BooleanField(default=False)),
                ('worker_id', models.CharField(max_length=256, null=True)),
                ('downloader_task', models.CharField(max_length=256)),
                ('batches', models.ManyToManyField(to='data_refinery_common.Batch')),
            ],
            options={
                'db_table': 'downloader_jobs',
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=256)),
                ('taxonomy_id', models.IntegerField()),
                ('is_scientific_name', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'organisms',
            },
        ),
        migrations.CreateModel(
            name='ProcessorJob',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('success', models.NullBooleanField()),
                ('num_retries', models.IntegerField(default=0)),
                ('retried', models.BooleanField(default=False)),
                ('worker_id', models.CharField(max_length=256, null=True)),
                ('pipeline_applied', models.CharField(max_length=256)),
                ('batches', models.ManyToManyField(to='data_refinery_common.Batch')),
            ],
            options={
                'db_table': 'processor_jobs',
            },
        ),
        migrations.CreateModel(
            name='SurveyJob',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('source_type', models.CharField(max_length=256)),
                ('success', models.NullBooleanField()),
                ('replication_started_at', models.DateTimeField(null=True)),
                ('replication_ended_at', models.DateTimeField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'survey_jobs',
            },
        ),
        migrations.CreateModel(
            name='SurveyJobKeyValue',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('key', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=256)),
                ('survey_job', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='data_refinery_common.SurveyJob')),
            ],
            options={
                'db_table': 'survey_job_key_values',
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='survey_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    to='data_refinery_common.SurveyJob'),
        ),
    ]
