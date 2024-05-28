from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model= City
        fields= ['name']
        widgets= {'name':TextInput(attrs={'id':'add_city','placeholder':'Add a city!'})}