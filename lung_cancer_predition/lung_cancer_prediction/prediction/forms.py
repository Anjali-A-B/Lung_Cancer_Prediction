from django import forms

class PredictionForm(forms.Form):
    GENDER_CHOICES = [('0', 'Female'), ('1', 'Male')]
    BINARY_CHOICES = [('1', 'No'), ('2', 'Yes')]

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    age = forms.IntegerField(max_value=100)
    smoking = forms.ChoiceField(choices=BINARY_CHOICES)
    yellow_fingers = forms.ChoiceField(choices=BINARY_CHOICES)
    anxiety = forms.ChoiceField(choices=BINARY_CHOICES)
    peer_pressure = forms.ChoiceField(choices=BINARY_CHOICES)
    chronic_disease = forms.ChoiceField(choices=BINARY_CHOICES)
    fatigue = forms.ChoiceField(choices=BINARY_CHOICES)
    allergy = forms.ChoiceField(choices=BINARY_CHOICES)
    wheezing = forms.ChoiceField(choices=BINARY_CHOICES)
    alcohol_consuming = forms.ChoiceField(choices=BINARY_CHOICES)
    coughing = forms.ChoiceField(choices=BINARY_CHOICES)
    shortness_of_breath = forms.ChoiceField(choices=BINARY_CHOICES)
    swallowing_difficulty = forms.ChoiceField(choices=BINARY_CHOICES)
    chest_pain = forms.ChoiceField(choices=BINARY_CHOICES)
