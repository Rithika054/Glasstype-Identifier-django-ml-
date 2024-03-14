import joblib
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def result(request):
    # Load the scikit-learn model
    try:
        r = joblib.load('classification_model.sav')
    except FileNotFoundError:
        return HttpResponse("Model file not found. Please check the file path.")

    # Get the input data from the request
    input_data = [float(request.GET.get(key, 0.0)) for key in ['RI', 'Na', 'Mg', 'AI', 'Si', 'K', 'Ca', 'Ba', 'Fe']]

    # Check if all required features are provided
    if len(input_data) != 9:
        return HttpResponse("Please provide values for all features.")

    # Make prediction
    try:
        ans = r.predict([input_data])
    except ValueError:
        return HttpResponse("Error occurred during prediction. Please check the input data.")

    return render(request, "result.html", {'ans': ans[0], 'lis': input_data})
