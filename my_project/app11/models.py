from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=60)
    about = models.TextField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name


class Project(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=80, null=True, blank=True)
    p_image = models.ImageField(upload_to='profile/')
    p_description = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.p_name


class Gallery(models.Model):
    g_id = models.IntegerField(primary_key=True)
    g_image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return str(self.g_id) + ',' + str('gallery image')


class Contact(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    subject = models.CharField(max_length=40, null=True, blank=True)
    message = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.subject)


class Tolls(models.Model):
    t_id = models.IntegerField(unique=True)
    t_name = models.CharField(max_length=50)
    t_percent = models.IntegerField()

    def __str__(self):
        return str(self.t_id) + '. ' + str(self.t_name)


class Skill(models.Model):
    skill_title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.skill_title


class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title
