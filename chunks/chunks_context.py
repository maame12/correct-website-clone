import chunk
from .models import chunks


def slider_chunks(request):
    chunk = chunks.objects.all().order_by('created')[0:3]
    # movies = Movie.objects.last()
    return {'slider_chunks' : chunks}