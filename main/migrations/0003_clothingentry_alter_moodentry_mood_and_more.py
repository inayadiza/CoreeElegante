# Generated by Django 5.1.1 on 2024-09-17 06:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_moodentry_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_item', models.CharField(max_length=255)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='mood',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='moodentry',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]