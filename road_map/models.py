from django.db import models
import uuid
import datetime


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MainBlock(models.Model):
    #quest = models.ForeignKey(MainQuest, on_delete=models.CASCADE, related_name='blocks')
    name = models.CharField(default='Block', max_length=50)

    def __str__(self):
        return self.name


#class MainQuest(models.Model):
class Level(models.Model):
    name = models.CharField(default='Quest', max_length=50)
    date_of_release = models.DateField(auto_created=True)
    position = models.IntegerField(default=0)
    crt_date = models.DateField(auto_created=True)
    
    def __str__(self):
        return self.name


class Events(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    quest = models.ForeignKey(Level, on_delete=models.CASCADE)
    block = models.ForeignKey(MainBlock, on_delete=models.CASCADE)
    name = models.CharField(default='Event', max_length=50)
    main_img = models.ImageField(upload_to='events_img', blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    crt_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now=True)
    desc = models.TextField()
    finished = models.BooleanField(default=False)
