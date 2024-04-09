import torch 
import torchvision
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 


class_names = ['Abyssinian', 'Bengal', 'Birman', 'Bombay', 'BritishShorthair',
                                 'EgyptianMau', 'MaineCoon', 'Persian', 'Ragdoll', 'RussianBlue',
                                 'Siamese', 'Sphynx', 'americanbulldog', 'americanpitbullterrier',
                                 'bassethound', 'beagle', 'boxer', 'chihuahua', 'englishcockerspaniel',
                                 'englishsetter', 'germanshorthaired', 'greatpyrenees', 'havanese',
                                 'japanesechin', 'keeshond', 'leonberger', 'miniaturepinscher',
                                 'newfoundland', 'pomeranian', 'pug', 'saintbernard', 'samoyed',
                                 'scottishterrier', 'shibainu', 'staffordshirebullterrier',
                                 'wheatenterrier', 'yorkshireterrier']


def create_model():

    weights = torchvision.models.ViT_B_16_Weights.IMAGENET1K_SWAG_E2E_V1
    model = torchvision.models.vit_b_16(weights=weights)
    test_transform = weights.transforms()

    model.heads = torch.nn.Sequential(
        torch.nn.Linear(in_features=768, out_features=len(class_names))
    )

    for param in model.parameters():
        param.requires_grad = False

    for param in model.heads.parameters():
        param.requires_grad = True

    return model, test_transform

def predict(img_path: str):
    model, test_transform = create_model()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.load_state_dict(torch.load(map_location=torch.device(device), f="vit-16-b_oxfordiiipet.pth"))
    model.to(device)



    model.eval()
    with torch.inference_mode():
        img = Image.open(img_path)
        transformed_img = test_transform(img)
        transformed_img = transformed_img.permute(1, 2, 0)
        plt.imshow(transformed_img)
        transformed_img = transformed_img.unsqueeze(dim=0)
        labels = model(transformed_img.permute(0, 3 , 1, 2))
        label = torch.argmax(torch.softmax(model(transformed_img.permute(0, 3, 1, 2)), dim=1), dim=1)
        prediction = class_names[label]
        predicted_labels = labels.argsort(descending=True)[:,:5]
        preds = []
        for i in range(5):
            preds.append(class_names[predicted_labels[:,i]])


        plt.title(f"Predicted Label: {class_names[label]}", color="g")

    return prediction, preds
