from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.title
      # return '%s %s' % (self.title, self.body)

class Friend(models.Model):
  name = models.CharField(max_length=100)

class Belonging(models.Model):
  name = models.CharField(max_length=100)

class Borrowed(models.Model):
  what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
  to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
  when = models.DateTimeField(auto_now_add=True)
  returned = models.DateTimeField(null=True, blank=True)