from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=264)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  description = models.TextField()
  image = models.ImageField(default='static/images/image.png', upload_to='static/images/')

  def __str__(self):
    return self.name

  # def __repr__(self):
  #   return "<Product {}>".format(self.name)


class Customer(models.Model):
  first_name = models.CharField(max_length=264)
  last_name = models.CharField(max_length=264)
  email = models.EmailField(max_length=264)
  password = models.CharField(max_length=264)
  profile_picture = models.ImageField(default='static/images/profile.jpg', upload_to='static/images/profile_pictures/')

  def __str__(self):
    return self.email

  def __repr__(self):
    return "<Customer {}>".format(self.email)