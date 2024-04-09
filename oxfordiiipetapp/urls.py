from oxfordiiipetapp import views
from django.urls import path


urlpatterns = [
    path("Classifier", views.classify, name="Classifier"),  
    path("ModelClasses", views.classes, name="ModelClasses"), 
]
