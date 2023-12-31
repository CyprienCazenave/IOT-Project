# Generated by Django 3.0.8 on 2023-07-19 08:53

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.UUID('ae551c49-5503-41c7-84aa-6def23f555ce'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('max_capacity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
