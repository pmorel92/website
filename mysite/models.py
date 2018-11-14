from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=200)
    date_finished = models.DateField()
    role = models.CharField(max_length=200)
    video_url = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title

class Official_Bio(models.Model):
    bio = models.TextField()

class Nodanews_Description(models.Model):
    description = models.TextField()    

class Agency(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Meeting(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=500, default=' ')
    date = models.DateField(default='2018-07-31')    
    agency = models.ForeignKey(
        'Agency',
        on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
    