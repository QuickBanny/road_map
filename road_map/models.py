from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MainQuest(models.Model):
    name = models.CharField(default='Quest', max_length=50)
    crt_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.name


class MainBlock(models.Model):
    quest = models.ForeignKey(MainQuest, on_delete=models.CASCADE, related_name='blocks')
    name = models.CharField(default='Block', max_length=50)

    def __str__(self):
        return self.name


class Events(models.Model):
    block = models.ForeignKey(MainBlock, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(default='Event', max_length=50)
    main_img = models.ImageField(upload_to='events_img')
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #status = models.ForeignKey(Status, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    crt_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now=True)
    desc = models.TextField()