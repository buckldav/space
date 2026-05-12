from django.shortcuts import render, get_object_or_404, redirect
from tactical.models import Phasers
from .forms import PhaserDirectionForm


# Create your views here
def tactical(request):
    # get from db
    phasers = Phasers.objects.all()
    # attach a form instance to each phaser for rendering in-template
    for p in phasers:
        p.form = PhaserDirectionForm(instance=p)
    stuff = {"phasers": phasers}

    return render(request, template_name="pages/tactical.html", context=stuff)


def phaser_update(request, pk):
    phaser = get_object_or_404(Phasers, pk=pk)
    if request.method == "POST":
        form = PhaserDirectionForm(request.POST, instance=phaser)
        if form.is_valid():
            form.save()
    # redirect back to the tactical page
    return redirect("/tactical")