from django.shortcuts import render
from oxfordiiipetapp.forms import InterfaceForm
from oxfordiiipetapp.models import Interface
from oxfordiiipetapp.predict import predict
import os 


# Create your views here.


def classify(request):

    if request.method == "POST":
        classifierform = InterfaceForm(request.POST, request.FILES)
        
        if classifierform.is_valid():
            classifierform.save()
            if Interface.objects.all():
                pets = Interface.objects.all()
                pet_data = []
                for pet in pets:
                    pet_data.append({"pet": pet})

            prediction, predicted_labels = predict(pet_data[-1]["pet"].pet_image.name)
            #img = my_figure(pet_data[-1]["pet"].pet_image.name)
            img_name = pet_data[-1]["pet"].pet_image
            os.remove(pet_data[-1]["pet"].pet_image.name)
            

        
    else:
        prediction, predicted_labels = None, None
        classifierform = InterfaceForm()
        img_name = None
        
        

    return render(request, "oxfordiiipetapp/Classifier.html", {"classifierform": classifierform, "prediction": prediction, "predicted_labels": predicted_labels})


def classes(request):
    nums = [1, 2, 3 ,4, 5]
    class_names = ['Abyssinian', 'Bengal', 'Birman', 'Bombay', 'BritishShorthair',
                                 'EgyptianMau', 'MaineCoon', 'Persian', 'Ragdoll', 'RussianBlue',
                                 'Siamese', 'Sphynx', 'americanbulldog', 'americanpitbullterrier',
                                 'bassethound', 'beagle', 'boxer', 'chihuahua', 'englishcockerspaniel',
                                 'englishsetter', 'germanshorthaired', 'greatpyrenees', 'havanese',
                                 'japanesechin', 'keeshond', 'leonberger', 'miniaturepinscher',
                                 'newfoundland', 'pomeranian', 'pug', 'saintbernard', 'samoyed',
                                 'scottishterrier', 'shibainu', 'staffordshirebullterrier',
                                 'wheatenterrier', 'yorkshireterrier']
    
    return render(request, "oxfordiiipetapp/ModelClasses.html", {"class_names": class_names, "nums": nums})

