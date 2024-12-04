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
    property_id = models.IntegerField(default="0")
    revivable = models.IntegerField(default="0")
    profile_image = models.TextField()
    life_current = models.IntegerField(default="0")
    life_maximum = models.IntegerField(default="0")
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

        from dateutil import parser

        from TornBuddy.handy import apiCall

        response = apiCall("user", "", "", self.api_key)
        self.name = response["name"]
        self.level = response["level"]
        self.honor = response["honor"]
        self.gender = response["gender"]
        self.property = response["property"]
        self.signup = parser.parse(response["signup"]).timestamp()
        self.awards = response["awards"]
        self.friends = response["friends"]
        self.enemies = response["enemies"]
        self.forum_posts = response["forum_posts"]
        self.karma = response["karma"]
        self.age = response["age"]
        self.role = response["role"]
        self.donator = response["donator"]
        self.torn_id = response["player_id"]
        self.property_id = response["property_id"]
        self.revivable = response["revivable"]
        self.profile_image = response["profile_image"]
        self.life_current = response["life"]["current"]
        self.life_maximum = response["life"]["maximum"]
        self.life_increment = response["life"]["increment"]
        self.life_interval = response["life"]["interval"]
        self.life_fulltime = response["life"]["fulltime"]
        self.status_description = response["status"]["description"]
        self.status_details = response["status"]["details"]
        self.status_state = response["status"]["state"]
        self.status_color = response["status"]["color"]
        self.status_until = response["status"]["until"]
        self.states_hospital_timestamp = response["states"]["hospital_timestamp"]
        self.states_jail_timestamp = response["states"]["jail_timestamp"]
        self.last_action_status = response["last_action"]["status"]
        self.last_action_timestap = response["last_action"]["timestamp"]
        self.last_action_relative = response["last_action"]["relative"]
        self.save()
        return self
