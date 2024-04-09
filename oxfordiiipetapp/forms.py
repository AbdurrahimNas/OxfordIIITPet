
from django import forms
from oxfordiiipetapp.models import Interface


class InterfaceForm(forms.ModelForm):


    class Meta:
        model = Interface
        fields = "__all__"


