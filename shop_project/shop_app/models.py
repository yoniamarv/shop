from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=264)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  description = models.TextField()
  shoes = models.ImageField(default='static/images/image.jpeg', upload_to='static/images/shoes/')

  def __str__(self):
    return self.name

  def __repr__(self):
    return "<Product {}>".format(self.name)


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

class Comment(models.Model):
  username = models.CharField(max_length=264)
  text = models.TextField()
  date = models.DateField()
  product = models.ForeignKey(Product , on_delete=models.CASCADE)

  def __str__(self):
    return self.username

  def __repr__(self):
    return "<Comment {}>".format(self.username)

class Maillot(models.Model):
  name = models.CharField(max_length=264)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  description = models.TextField()
  maillot_picture = models.ImageField(default='static/images/maillot.jpg', upload_to='static/images/maillot_pictures/')

  def __str__(self):
    return self.name

  def __repr__(self):
    return "<Maillot {}>".format(self.name)
