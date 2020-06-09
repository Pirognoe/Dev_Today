from django.db import models


class Post(models.Model):
    """This class is created to operate with posts"""

    title = models.CharField(max_length=255)
    link = models.URLField()
    creation_date = models.DateTimeField()
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """This class represents the comments corresponding to particular Post"""

    post = models.ForeignKey('Post', related_name='posts', on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    content = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return (self.author_name + '-' + str(self.creation_date))
