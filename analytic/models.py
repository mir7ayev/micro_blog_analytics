from django.db import models


class PostView(models.Model):
    post_id = models.IntegerField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Post {self.post_id} - Views {self.view_count}'


class PostViewByUser(models.Model):
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Registered {self.user_id} - Views {self.count}'


class PostViewByGender(models.Model):
    post_id = models.IntegerField()
    gender = models.CharField(max_length=120)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Post {self.post_id} - Gender {self.gender}'


class PostViewByAge(models.Model):
    post_id = models.IntegerField()
    age = models.IntegerField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Post {self.post_id} - Age {self.age}'


class PostViewByCountry(models.Model):
    post_id = models.IntegerField()
    country = models.CharField(max_length=120)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Post {self.post_id} - Country {self.country}'
