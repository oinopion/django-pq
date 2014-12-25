# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlowStore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('enqueued_at', models.DateTimeField(null=True, blank=True)),
                ('ended_at', models.DateTimeField(null=True, blank=True)),
                ('expired_at', models.DateTimeField(null=True, verbose_name=b'expires', blank=True)),
                ('status', models.PositiveIntegerField(blank=True, null=True, choices=[(1, b'queued'), (2, b'finished'), (3, b'failed')])),
                ('jobs', picklefield.fields.PickledObjectField(editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'flow',
                'verbose_name_plural': 'flows',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=64, null=True, blank=True)),
                ('created_at', models.DateTimeField()),
                ('origin', models.CharField(max_length=254, null=True, blank=True)),
                ('instance', picklefield.fields.PickledObjectField(null=True, editable=False, blank=True)),
                ('func_name', models.CharField(max_length=254)),
                ('args', picklefield.fields.PickledObjectField(editable=False, blank=True)),
                ('kwargs', picklefield.fields.PickledObjectField(editable=False, blank=True)),
                ('description', models.CharField(max_length=254)),
                ('result_ttl', models.IntegerField(null=True, blank=True)),
                ('status', models.PositiveIntegerField(blank=True, null=True, choices=[(0, b'scheduled'), (1, b'queued'), (2, b'finished'), (3, b'failed'), (4, b'started'), (5, b'flow')])),
                ('enqueued_at', models.DateTimeField(null=True, blank=True)),
                ('scheduled_for', models.DateTimeField()),
                ('repeat', picklefield.fields.PickledObjectField(help_text=b'Number of times to repeat. -1 for forever.', null=True, editable=False, blank=True)),
                ('interval', picklefield.fields.PickledObjectField(help_text=b'Timedelta till next job', null=True, editable=False, blank=True)),
                ('between', models.CharField(max_length=5, null=True, blank=True)),
                ('weekdays', picklefield.fields.PickledObjectField(null=True, editable=False, blank=True)),
                ('ended_at', models.DateTimeField(null=True, blank=True)),
                ('expired_at', models.DateTimeField(null=True, verbose_name=b'expires', blank=True)),
                ('result', picklefield.fields.PickledObjectField(null=True, editable=False, blank=True)),
                ('exc_info', models.TextField(null=True, blank=True)),
                ('timeout', models.PositiveIntegerField(null=True, blank=True)),
                ('meta', picklefield.fields.PickledObjectField(editable=False, blank=True)),
                ('if_failed', models.CharField(max_length=64, null=True, blank=True)),
                ('if_result', models.CharField(max_length=64, null=True, blank=True)),
                ('flow', models.ForeignKey(blank=True, to='pq.FlowStore', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('name', models.CharField(default=b'default', max_length=100, serialize=False, primary_key=True)),
                ('default_timeout', models.PositiveIntegerField(null=True, blank=True)),
                ('cleaned', models.DateTimeField(null=True, blank=True)),
                ('scheduled', models.BooleanField(default=False, help_text=b'Optimisation: scheduled tasks are slower.')),
                ('lock_expires', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 13, 17, 33, 511994, tzinfo=utc))),
                ('serial', models.BooleanField(default=False)),
                ('idempotent', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('name', models.CharField(max_length=254, serialize=False, primary_key=True)),
                ('birth', models.DateTimeField(null=True, blank=True)),
                ('expire', models.PositiveIntegerField(null=True, verbose_name=b'Polling TTL', blank=True)),
                ('queue_names', models.CharField(max_length=254, null=True, blank=True)),
                ('stop', models.BooleanField(default=False, help_text=b'Send a stop signal to the worker')),
                ('heartbeat', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='job',
            name='queue',
            field=models.ForeignKey(blank=True, to='pq.Queue', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flowstore',
            name='queue',
            field=models.ForeignKey(blank=True, to='pq.Queue', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='DequeuedJob',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.job',),
        ),
        migrations.CreateModel(
            name='FailedJob',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.job',),
        ),
        migrations.CreateModel(
            name='FailedQueue',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.queue',),
        ),
        migrations.CreateModel(
            name='FlowQueue',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.queue',),
        ),
        migrations.CreateModel(
            name='QueuedJob',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.job',),
        ),
        migrations.CreateModel(
            name='ScheduledJob',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.job',),
        ),
        migrations.CreateModel(
            name='SerialQueue',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('pq.queue',),
        ),
    ]
