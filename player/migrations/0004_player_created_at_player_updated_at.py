# Generated by Django 5.1.3 on 2024-12-09 11:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0003_alter_player_api_key_alter_player_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="player",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
