from django.db import models



class Post_now(models.Model):
    text = models.TextField()


class Remote_post(models.Model):
    text = models.TextField()
    time = models.DateTimeField(blank=True,auto_now=False)


