from django.db import models
from django.utils.text import slugify
from django.utils import timezone
import uuid


CATEGORY_CHOICES =(
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
    
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('german', 'GERMAN'),
)

STATUS_CHOICES = (
    ('RA' , 'Recently Added'),
    ('MW' , 'Mostly watched'),
    ('TR' , 'Top Rated'),
)
# Create your models here.B







class chunks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='chunks')
    #banner = models.ImageField(upload_to='chunks_banner')
   # uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=10 )
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField( max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    chunks_trailer = models.URLField()
    
    
    
    
    


    
    
    created = models.DateTimeField(default=timezone.now)
    
    
    
    
    slug = models.SlugField(blank=True, null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super(chunks , self).save( *args , **kwargs)
    
    
    def __str__(self):
        return self.title
    
LINK_CHOICES =(
    ('D' , 'DOWNLOAD LINK'),
    ('W' , 'WATCH LINK' )
)    
 
 
   
    
class chunksLinks(models.Model):
    movie =  models.ForeignKey('chunks', related_name='chunks_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES,max_length=1)
    link = models.URLField()

    
    def _str_(self):
        return str(self.chunks)
    
    






