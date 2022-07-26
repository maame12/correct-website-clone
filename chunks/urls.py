
from django.urls import path
from .views import chunksList , chunksDetail , chunksCategory , chunksLanguage, chunksSearch, chunksYear
from chunks import views


app_name ='chunks'


urlpatterns = [
    
    
    
    
    
    
    path('', chunksList.as_view() , name='chunks_list'),
    path('category/<str:category>', chunksCategory.as_view() , name='chunks_category'),
    path('language/<str:lang>', chunksLanguage.as_view() , name='chunks_language'),
    path('search/', chunksSearch.as_view() , name='chunks_search'),
    path('<slug:slug> ', chunksDetail.as_view() , name='chunks_detail'),
    path('year/<int:year>', chunksYear.as_view() , name='chunks_year'),
    
]

