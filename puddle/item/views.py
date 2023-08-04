from django.shortcuts import render, get_object_or_404
from item.models import Item

# Create your views here.
def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[:4]
    return render(request, 'item/details.html',{
        'item': item,
        'related_items': related_items,
    })