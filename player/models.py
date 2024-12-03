from django.db import models


# Create your models here.
class Player(models.Model):
    torn_id = models.IntegerField(unique=True)
    name = models.TextField()
    api_key = models.TextField()
    level = models.IntegerField(default="0")
    honor = models.TextField()
    gender = models.TextField()
    property = models.TextField()
    signup = models.IntegerField(null=True, default=28377016)
    awards = models.IntegerField(default="0")
    friends = models.IntegerField(default="0")
    enemies = models.IntegerField(default="0")
    forum_posts = models.IntegerField(default="0")
    karma = models.IntegerField(default="0")
    age = models.IntegerField(default="0")
    role = models.TextField()
    donator = models.IntegerField(default="0")
    player_id = models.IntegerField(default="0")
    property_id = models.IntegerField(default="0")
    revivable = models.IntegerField(default="0")
    profile_image = models.TextField()
    life_current = models.IntegerField(default="0")
    life_maxium = models.IntegerField(default="0")
    life_increment = models.IntegerField(default="0")
    life_interval = models.IntegerField(default="0")
    life_fulltime = models.IntegerField(null=True, default=28377016)
    status_description = models.TextField()
    status_details = models.TextField()
    status_state = models.TextField()
    status_color = models.TextField()
    status_until = models.IntegerField(null=True, default=28377016)
    states_hospital_timestamp = models.IntegerField(null=True, default=28377016)
    states_jail_timestamp = models.IntegerField(null=True, default=28377016)
    last_action_status = models.TextField()
    last_action_timestap = models.IntegerField(null=True, default=28377016)
    last_action_relative = models.TextField()

    def update_own_key(self):
        # TODO: Update player
        return self
