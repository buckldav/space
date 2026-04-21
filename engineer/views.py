from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Task
from .forms import TaskViewForm, TaskListDisplayForm


@login_required
def task_list_view(request):
    filter_form = TaskViewForm(request.GET or None)
    tasks = Task.objects.all()
    
    if filter_form.is_valid():
        status_filter = filter_form.cleaned_data.get('status_filter')
        search_query = filter_form.cleaned_data.get('search')
        
        if status_filter == 'completed':
            tasks = tasks.filter(completed=True)
        elif status_filter == 'pending':
            tasks = tasks.filter(completed=False)
        
        if search_query:
            tasks = tasks.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
    
    tasks_with_forms = [
        {
            'task': task,
            'form': TaskListDisplayForm(instance=task),
        }
        for task in tasks
    ]
    
    context = {
        'filter_form': filter_form,
        'tasks': tasks_with_forms,
        'task_count': tasks.count(),
    }
    
    return render(request, 'engineer/task_list.html', context)
