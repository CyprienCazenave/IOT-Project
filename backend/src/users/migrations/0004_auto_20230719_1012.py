# Generated by Django 3.0.8 on 2023-07-19 10:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230719_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f786dda4-7f3b-457d-92bc-47ee202f7334'), editable=False, primary_key=True, serialize=False),
        ),
    ]
