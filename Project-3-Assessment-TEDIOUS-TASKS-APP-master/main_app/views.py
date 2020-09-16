from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Task


# Create your views here.
def index(request):

    if request.method == 'POST':
        description = request.POST.get("description", "")
        time = request.POST.get("time", "")
        person = request.POST.get("person", "")
        name = request.POST.get("name", "")

        task = Task(description=description, time=time, person=person)
        task.save()
        return HttpResponseRedirect('/main_app')


    tasks = Task.objects.all()
    template = loader.get_template('main_app/index.html')
    context = {
        'tasks': tasks,
    }
    return HttpResponse(template.render(context, request))