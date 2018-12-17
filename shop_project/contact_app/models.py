from django.db import models

class Contact(models.Model):
  subject = models.CharField(max_length=264)
  email = models.EmailField()
  text = models.TextField()
  

  def __str__(self):
    return self.subject

  def __repr__(self):
    return "<Contact {}>".format(self.subject)

