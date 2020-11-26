from django.shortcuts import render, HttpResponse, Http404
from .models import Item
user_data = {
    "surname": "PIDOR",
    "name": "Aleksei",
    "second_name": "Petrovich"
}
items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]
# Create your views here.
def main(request):
    user_format = f"{user_data['surname']} {user_data['name'][0]}.{user_data['second_name'][0]}"
    return render(request, 'index.html', context={"short_name": user_format})

def item(request, id):
    context = {}
    for item in items:
        if item["id"] == id:
            context["item"] = item
            return render(request, 'item.html', context)
    raise Http404


def item_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)
