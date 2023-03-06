from django.shortcuts import render
from .models import Symptoms
from .models import Disease
def index(request):
    return render(request, 'index.html')

def checkup(request):
    return render(request, 'checkup.html')

def animal(request):
    return render(request, 'animal.html')

def cowinterview(request,animal,step,choice):
    if step == "0":
        symptom=Symptoms.objects.get(animal=animal,step="0")
    elif step == "1" and choice == "1":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    elif step =="1" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step="2")
    elif step =="3" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step ="4")
    elif step == "2" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=2)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=4)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "0":
        result=Disease.objects.get(animal=animal, diseaseid=5)
        return render(request,"result.html",{'result':result})
    elif step == "2" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    return render(request, 'cowinterview.html',{'symptom': symptom})
def goatinterview(request,animal,step,choice):
    if step == "0":
        symptom=Symptoms.objects.get(animal=animal,step="0")
    elif step == "1" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step =="1" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step="2")
    elif step =="3" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step ="3")
    elif step == "2" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=2)
        return render(request,"result.html",{'result':result})
    elif step == "4" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=3)
        return render(request,"result.html",{'result':result})
    elif step == "4" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="4")
    elif step == "5" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="5")
    elif step == "5" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=6)
        return render(request,"result.html",{'result':result})
    elif step == "6" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=4)
        return render(request,"result.html",{'result':result})
    return render(request, 'goatinterview.html',{'symptom': symptom})

def sheepinterview(request,animal,step,choice):
    print(animal)
    if step == "0":
        symptom=Symptoms.objects.get(animal=animal,step="0")
    elif step == "1" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step =="1" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    elif step =="2" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step ="2")
    elif step == "2" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=2)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=3)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=4)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "0":
        result=Disease.objects.get(animal=animal, diseaseid=5)
        return render(request,"result.html",{'result':result})
    elif step == "2" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    return render(request, 'sheepinterview.html',{'symptom': symptom})

def chickeninterview(request,animal,step,choice):
    if step == "0":
        symptom=Symptoms.objects.get(animal=animal,step="0")
    elif step == "1" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step =="1" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    elif step =="3" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step ="4")
    elif step == "2" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=2)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=3)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=4)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step ="3")
    elif step == "2" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="2")
    return render(request, 'chickeninterview.html',{'symptom': symptom})

def rabbitinterview(request,animal,step,choice):
    if step == "0":
        symptom=Symptoms.objects.get(animal=animal,step="0")
    elif step == "1" and choice == "1":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    elif step =="1" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step="2")
    elif step =="3" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step ="4")
    elif step == "2" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=2)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=4)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "0":
        result=Disease.objects.get(animal=animal, diseaseid=5)
        return render(request,"result.html",{'result':result})
    elif step == "2" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    return render(request, 'rabbitinterview.html',{'symptom': symptom})

def turkeyinterview(request,animal,step,choice):
    if step == "0":
        symptom=Symptoms.objects.get(animal=animal,step="0")
    elif step == "1" and choice == "1":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    elif step =="1" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step="2")
    elif step =="3" and choice =="0":
        symptom=Symptoms.objects.get(animal=animal,step ="4")
    elif step == "2" and choice == "1":
        result=Disease.objects.get(animal=animal,diseaseid=1)
        return render(request,"result.html",{'result':result})
    elif step == "3" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=2)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "1":
        result=Disease.objects.get(animal=animal, diseaseid=4)
        return render(request,"result.html",{'result':result})
    elif step == "5" and choice == "0":
        result=Disease.objects.get(animal=animal, diseaseid=5)
        return render(request,"result.html",{'result':result})
    elif step == "2" and choice == "0":
        symptom=Symptoms.objects.get(animal=animal,step="1")
    return render(request, 'turkeyinterview.html',{'symptom': symptom})

