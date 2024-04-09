from django.db import models
from django_matplotlib import MatplotlibFigureField

# Create your models here.


class Interface(models.Model):
    pet_image = models.FileField(null=False, blank=False)
    figure = MatplotlibFigureField(figure='my_figure')
    def __str__(self):
        return f"{self.id} {self.pet_image}"
    

#class MyModel(models.Model):
#    figure = MatplotlibFigureField(figure='my_figure')