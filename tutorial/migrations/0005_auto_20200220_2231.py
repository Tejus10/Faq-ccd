# Generated by Django 3.0.1 on 2020-02-20 17:01

from __future__ import unicode_literals

from django.db import migrations, models
import uuid


def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('tutorial', 'ques')
    for row in MyModel.objects.all():
        row.slug = uuid.uuid4()
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0004_ques_slug'),
    ]

    operations = [
    	migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
