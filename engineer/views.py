from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Task
from .forms import TaskViewForm, TaskListDisplayForm
from rest_framework import generics, serializers
from rest_framework.permissions import IsAdminUser

class  TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@login_required
def task_list_view(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        if task_id:
            try:
                task = Task.objects.get(id=task_id)
                form = TaskListDisplayForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    # Redirect to preserve GET params
                    from django.shortcuts import redirect
                    return redirect(request.get_full_path())
            except Task.DoesNotExist:
                pass  # Handle error if needed
    
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
