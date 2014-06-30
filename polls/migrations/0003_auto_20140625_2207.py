# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20140625_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question', default=1, to_field='id'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
    ]
