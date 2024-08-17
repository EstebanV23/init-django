from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apptask.models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def init(request):
    return render(request, 'index.html')

def tasks(request):
    tasks = Task.objects.all().order_by('id').reverse()
    projects = Project.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks,
        'projects': projects
    })

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f"<h1>Task <small>{task.title}</small</h1><p>{task.description}</p>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def update_task(request, id):
    try:
        if request.POST.get('indNew') in ('true', 'True', '1'):
            raise Task.DoesNotExist
        task = Task.objects.get(id=id)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        print('Task updated')
    except Task.DoesNotExist:
        print('Task not found')
        task = Task()
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.project = Project.objects.get(id=request.POST.get('project'))
        task.save()
        print('Task created')
    finally:
        return redirect('/apptask/task')

def check_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.completed = request.POST.get('completed')
        task.save()
        return JsonResponse({
            "success": True,
            "message": "Task updated"
        }, safe=False)
    except Task.DoesNotExist:
        return JsonResponse({
            "success": False,
            "message": "Task not found"
        }, safe=False)
