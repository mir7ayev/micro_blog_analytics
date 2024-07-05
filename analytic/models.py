from django.db import models


class PostView(models.Model):
    post_id = models.IntegerField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f'Post {self.post_id} - Views {self.view_count}'


class UserVisit(models.Model):
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Registered {self.user_id} - Views {self.count}'
