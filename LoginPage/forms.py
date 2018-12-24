from django import forms
from django.conf import settings
import requests
import json

VEHICLE_CHOICE = []

def vehicle_choice():
    """Returns the list of tesla vehicleas from the api"""
    session = requests.Session()
    response = session.get(settings.BASE_URL, headers={settings.API_KEY: settings.API_VALUE})
    json_response = json.loads(response.text)
    VEHICLE_CHOICE.append(('default', '  - Select your Tesla vehicle -'))
    for vehicle_obj in json_response['response']:
        VEHICLE_CHOICE.append((vehicle_obj['display_name'], vehicle_obj['display_name']))
    return VEHICLE_CHOICE


class LoginPage(forms.Form):
    user_id = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder':'  Your login ID for Tesla',"class": "text-field"}))
    attrs = {
        "type": "password", 
        "placeholder":"  Your Tesla password please?",
        "class": "text-field"
    }
    password = forms.CharField(widget=forms.TextInput(attrs=attrs), label="")
    vehivles = forms.ChoiceField(choices=vehicle_choice(), label="")
