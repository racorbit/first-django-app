# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(to='polls.Choice'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
    ]
