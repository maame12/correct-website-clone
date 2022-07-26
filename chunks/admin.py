from django.contrib import admin



# Register your models here.
from .models import chunks , chunksLinks 

admin.site.register(chunks)
admin.site.register(chunksLinks)

