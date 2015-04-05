# encoding=utf-8
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from istream.stream.models import Publisher
from django.shortcuts import get_object_or_404


@csrf_exempt
def on_publish(request):
    publisher = get_object_or_404(Publisher, name=request.POST["name"])
    print(publisher)
    return HttpResponse("200 OK", status=200)


