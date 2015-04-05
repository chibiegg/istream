# encoding=utf-8
from istream.stream.models import Publisher
from django.shortcuts import render, get_object_or_404




def publishers(request):
    publishers = Publisher.objects.all()

    context = {
               "publishers":publishers,
               }
    return render(request, "stream/publishers.html", context)


def publisher(request, id):
    publisher = get_object_or_404(Publisher, id=id)

    context = {
               "publisher":publisher,
               }
    return render(request, "stream/publisher.html", context)

