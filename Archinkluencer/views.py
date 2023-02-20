from django.template import loader
from .models import ModelDataIFC
from . models import WallsWc
import subprocess
from subprocess import run, PIPE
# Create your views here.
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3


# Python program to explain os.listdir() method

# importing os module
import os





def Archinkluencer(request):

    if request.method == 'POST' and not request.POST.get('wallname') and not request.POST.get('algo') :
        print("received data width: ", request.POST['itemNameW'])#hier übergebe ich die Daten
        ModelDataIFC.objects.create(name = request.POST['itemNameW'])
        print("received data length: ", request.POST['itemNameL'])  # hier übergebe ich die Daten
        ModelDataIFC.objects.create(length=request.POST['itemNameL'])
        print("received data door: ", request.POST['itemNameD'])  # hier übergebe ich die Daten
        ModelDataIFC.objects.create(doorpos=request.POST['itemNameD'])


    if request.POST.get('wallname') :
        savevalue1 = ModelDataIFC()
        savevalue1.wallname = request.POST.get('wallname')
        savevalue1.save()
        print("received data wallname: ", savevalue1.wallname)
        messages.success(request, "sie haben folgende Wand gewählt: " + savevalue1.wallname)
        #return render(request, "archinkluencerNew.html")

        savevaluealgo = ModelDataIFC()
        savevaluealgo.algo = request.POST.get('algo')
        #print("received data algo: ", savevaluealgo.algo)


    subprocess.run(["python", "//Users//ameliehofer//PycharmProjects//djangoProject//scripts//main.py"], shell=False, stdout=PIPE )
    #print("run python")

    all_items = ModelDataIFC.objects.all()
    template = loader.get_template('indexMain.html')
    context = {'all_items': all_items}

    #os.system("python3 /Users/ameliehofer/PycharmProjects/App_Arch/App_Arch/main.py")
    return HttpResponse(template.render(context, request))





"""

    #return render(request, 'archinkluencer.html', {'all_items':all_items})

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def run(request):
    if request.method == 'GET':
        wallselections = request.GET['WallSelect']
        print(wallselections)

        return HttpResponse("Completed."+ wallselections )

def index(request):
   return render(request, "ArchinkluencerNew.html", {})



def WallsSel(request):
    if request.method == 'GET':
        print("received data wall wc: ", request.GET['wallNamewc'])  # hier übergebe ich die Daten
        WallsWc.objects.create(name=request.GET['wallNamewc'])
        print("received data wall sink: ", request.GET['wallNamesink'])  # hier übergebe ich die Daten
        WallsWc.objects.create(name=request.GET['wallNamesink'])


        import subprocess
        subprocess.run(["python", "/Users/ameliehofer/PycharmProjects/App_Arch/viewer/main.py"])

        all_selections = WallsWc.objects.all()
        template = loader.get_template('archinkluencerNew.html')
        context = {'all_selections': all_selections}

        return HttpResponse(template.render(context, request))

        #return HttpResponse("Completed."+ wallselections )"""


"""
def print_http_response(f):
    "" Wraps a python function that prints to the console, and
    returns those results as a HttpResponse (HTML)""

    class WritableObject:
        def __init__(self):
            self.content = []

        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content])

    return new_f"""
