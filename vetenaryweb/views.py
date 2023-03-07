from django.shortcuts import render
from .models import Disease
from .models import FeedBack
def index(request):
    return render(request, 'index.html')

def checkup(request):
    return render(request, 'checkup.html')

def animal(request):
    return render(request, 'animal.html')

def notification(request):
    return render(request, 'notification.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        feed=FeedBack.objects.create(name=name, email=email,subject=subject,message=message)
        feed.save()
        return render(request, 'feedback.html',{"message":"feedback sent successfully"})
    return render(request, 'feedback.html')


def cowinterview(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        fmd_symptoms = set(['1', '2', '3', '4', '5', '6'])
        anthrax_symptoms = set(['7', '8', '9', '10', '11', '12', '13'])
        fmd_selected = set(symptoms).issuperset(fmd_symptoms) or len(set(symptoms).intersection(fmd_symptoms)) >= 3
        anthrax_selected = set(symptoms).issuperset(anthrax_symptoms) or len(set(symptoms).intersection(anthrax_symptoms)) >= 3
        if fmd_selected and anthrax_selected:
            disease = 'unknown'
            disease=Disease.objects.get(animal="unknown")
        elif fmd_selected:
            disease = 'FMD disease'
            disease=Disease.objects.get(animal="cow",diseaseid=1)
        elif anthrax_selected:
            disease = 'anthrax'
            disease=Disease.objects.get(animal="cow",diseaseid=2)
        else:
            disease = 'unknown'
            disease=Disease.objects.get(animal="unknown")
        return render(request, 'result.html', {'disease': disease})
    else:
        return render(request, 'cowinterview.html')
def goatinterview(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        fmd_symptoms = set(['1', '2', '3', '4', '5', '6'])
        anthrax_symptoms = set(['7', '8', '9', '10', '11'])
        fmd_selected = set(symptoms).issuperset(fmd_symptoms) or len(set(symptoms).intersection(fmd_symptoms)) >= 3
        anthrax_selected = set(symptoms).issuperset(anthrax_symptoms) or len(set(symptoms).intersection(anthrax_symptoms)) >= 3
        if fmd_selected and anthrax_selected:
            disease = 'unknown'
            disease=Disease.objects.get(animal="unknown")
        elif fmd_selected:
            disease = 'FMD disease'
            disease=Disease.objects.get(animal="goat",diseaseid=1)
        elif anthrax_selected:
            disease = 'anthrax'
            disease=Disease.objects.get(animal="goat",diseaseid=2)
        else:
            disease = 'unknown'
            disease=Disease.objects.get(animal="unknown")
        return render(request, 'result.html', {'disease': disease})
    else:
        return render(request, 'goatinterview.html')
def sheepinterview(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        fmd_symptoms = set(['1', '2', '3', '4', '5', '6','7','8'])
        anthrax_symptoms = set(['9', '10', '11','12','13'])
        fmd_selected = set(symptoms).issuperset(fmd_symptoms) or len(set(symptoms).intersection(fmd_symptoms)) >= 3
        anthrax_selected = set(symptoms).issuperset(anthrax_symptoms) or len(set(symptoms).intersection(anthrax_symptoms)) >= 3
        if fmd_selected and anthrax_selected:
            disease = 'unknown'
            disease=Disease.objects.get(animal="unknown")
        elif fmd_selected:
            disease = 'FMD disease'
            disease=Disease.objects.get(animal="sheep",diseaseid=1)
        elif anthrax_selected:
            disease = 'anthrax'
            disease=Disease.objects.get(animal="sheep",diseaseid=2)
        else:
            disease = 'unknown'
            disease=Disease.objects.get(animal="unknown")
        return render(request, 'result.html', {'disease': disease})
    else:
        return render(request, 'sheepinterview.html')
def chickeninterview(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        newcastle_symptoms = set(['1', '2', '3', '4', '5', '6'])
        coccidiosis_symptoms = set(['7','8','9', '10', '11','12','13','14'])
        newcastle_selected = set(symptoms).issuperset(newcastle_symptoms) or len(set(symptoms).intersection(newcastle_symptoms)) >= 3
        coccidiosis_selected = set(symptoms).issuperset(coccidiosis_symptoms) or len(set(symptoms).intersection(coccidiosis_symptoms)) >= 3
        if newcastle_selected and coccidiosis_selected:
            disease=Disease.objects.get(animal="unknown")
        elif newcastle_selected:
            disease=Disease.objects.get(animal="chicken",diseaseid=1)
        elif coccidiosis_selected:
            disease=Disease.objects.get(animal="chicken",diseaseid=2)
        else:
            disease=Disease.objects.get(animal="unknown")
        return render(request, 'result.html', {'disease': disease})
    else:
        return render(request, 'chickeninterview.html')

def turkeyinterview(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        newcastle_symptoms = set(['1', '2', '3', '4', '5', '6'])
        coccidiosis_symptoms = set(['6','7', '8', '9','10'])
        newcastle_selected = set(symptoms).issuperset(newcastle_symptoms) or len(set(symptoms).intersection(newcastle_symptoms)) >= 3
        coccidiosis_selected = set(symptoms).issuperset(coccidiosis_symptoms) or len(set(symptoms).intersection(coccidiosis_symptoms)) >= 3
        if newcastle_selected and coccidiosis_selected:
            disease=Disease.objects.get(animal="unknown")
        elif newcastle_selected:
            disease=Disease.objects.get(animal="turkey",diseaseid=1)
        elif coccidiosis_selected:
            disease=Disease.objects.get(animal="turkey",diseaseid=2)
        else:
            disease=Disease.objects.get(animal="unknown")
        return render(request, 'result.html', {'disease': disease})
    else:
        return render(request, 'turkeyinterview.html')

