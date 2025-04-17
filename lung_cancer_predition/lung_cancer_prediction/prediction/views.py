import joblib
from django.shortcuts import render
from .forms import PredictionForm

# Load the trained model
model = joblib.load('lung_cancer_predictor.pkl')

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract data from form
            data = [
                int(form.cleaned_data['gender']),
                int(form.cleaned_data['age']),
                int(form.cleaned_data['smoking']),
                int(form.cleaned_data['yellow_fingers']),
                int(form.cleaned_data['anxiety']),
                int(form.cleaned_data['peer_pressure']),
                int(form.cleaned_data['chronic_disease']),
                int(form.cleaned_data['fatigue']),
                int(form.cleaned_data['allergy']),
                int(form.cleaned_data['wheezing']),
                int(form.cleaned_data['alcohol_consuming']),
                int(form.cleaned_data['coughing']),
                int(form.cleaned_data['shortness_of_breath']),
                int(form.cleaned_data['swallowing_difficulty']),
                int(form.cleaned_data['chest_pain'])
            ]
            # Make prediction
            prediction = model.predict([data])
            result = 'Yes' if prediction[0] == 1 else 'No'
            return render(request, 'result.html', {'result': result})
    else:
        form = PredictionForm()
    return render(request, 'predict.html', {'form': form})

def result(request):
    return render(request, 'result.html')