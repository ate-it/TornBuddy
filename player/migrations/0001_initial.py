# Generated by Django 5.1.3 on 2024-12-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("torn_id", models.IntegerField(unique=True)),
                ("name", models.TextField()),
                ("api_key", models.TextField()),
                ("level", models.IntegerField(default="0")),
                ("honor", models.TextField()),
                ("gender", models.TextField()),
                ("property", models.TextField()),
                ("signup", models.IntegerField(default=28377016, null=True)),
                ("awards", models.IntegerField(default="0")),
                ("friends", models.IntegerField(default="0")),
                ("enemies", models.IntegerField(default="0")),
                ("forum_posts", models.IntegerField(default="0")),
                ("karma", models.IntegerField(default="0")),
                ("age", models.IntegerField(default="0")),
                ("role", models.TextField()),
                ("donator", models.IntegerField(default="0")),
                ("property_id", models.IntegerField(default="0")),
                ("revivable", models.IntegerField(default="0")),
                ("profile_image", models.TextField()),
                ("life_current", models.IntegerField(default="0")),
                ("life_maximum", models.IntegerField(default="0")),
                ("life_increment", models.IntegerField(default="0")),
                ("life_interval", models.IntegerField(default="0")),
                ("life_fulltime", models.IntegerField(default=28377016, null=True)),
                ("status_description", models.TextField()),
                ("status_details", models.TextField()),
                ("status_state", models.TextField()),
                ("status_color", models.TextField()),
                ("status_until", models.IntegerField(default=28377016, null=True)),
                (
                    "states_hospital_timestamp",
                    models.IntegerField(default=28377016, null=True),
                ),
                (
                    "states_jail_timestamp",
                    models.IntegerField(default=28377016, null=True),
                ),
                ("last_action_status", models.TextField()),
                (
                    "last_action_timestap",
                    models.IntegerField(default=28377016, null=True),
                ),
                ("last_action_relative", models.TextField()),
            ],
        ),
    ]
