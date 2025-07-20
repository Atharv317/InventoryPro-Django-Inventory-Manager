from django.http import HttpResponse

from .models import Item


def item_list(request):
    return HttpResponse("Working")

