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
            name='Sounds',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.UUID('3e6f13d0-aa22-4c1e-bb20-6ba701bde7b9'), editable=False, primary_key=True, serialize=False)),
                ('salle_id', models.CharField(blank=True, max_length=255, null=True)),
                ('sound', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
