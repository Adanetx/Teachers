from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Teacher(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  sex = models.CharField(max_length=50)
  favorite_course = models.CharField(max_length=100)
  education = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"In our collage '{self.name}' is '{self.age}' years old, '{self.sex}', whose favorite course is '{self.favorite_course}', has '{self.education}' highest level of educaton."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'name': self.name,
        'age': self.age,
        'sex': self.sex,
        'favorite_course': self.favorite_course,
        'education': self.education
    }
