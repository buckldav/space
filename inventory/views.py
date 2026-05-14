from django.shortcuts import render, get_list_or_404, redirect
from inventory.models import InventoryItem
# Create your views here.

def inventory(request):

    inventoryitems = InventoryItem.objects.all()

    # for i in inventoryitems:
        # i.form = InventoryItem
    stuff = {"inventoryitems": inventoryitems}

    return render(request, template_name="pages/inventory.html", context=stuff)
