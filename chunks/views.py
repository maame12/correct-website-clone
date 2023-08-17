##from typing_extensions import self

from django.shortcuts import  render , redirect 
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import ListView , DetailView
from django.views.generic.dates import YearArchiveView
from .models import chunks , chunksLinks 
from .forms import  CustomUserCreationForm


def LoginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password )
        print('USER:', user)
        
        if user is not None:
            login(request, user)
            return redirect("home")
    
    return render(request, 'chunks/login_register.html', {'page':page})

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            
            user = authenticate(request, username=user.username, password=request.POST['password1'] )
            
            if user is not None:
                login(request, user)
                return redirect("home")
            
            
    context = {'form':form, 'page':page}
    return render(request, 'chunks/login_register.html', context)







class HomeView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'chunks/home.html'
    model = chunks
    
    def get_context_data(self , **kwargs):
        context = super(HomeView , self).get_context_data(**kwargs)
        context['top_rated'] = chunks.objects.filter(status='TR')
        context['most_watched'] = chunks.objects.filter(status='MW')
        context['recently_added'] = chunks.objects.filter(status='RA') 
        return context
    
    
    
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
        #return(HomeView,self).dispatch(*args, **kwargs)
    
      

class chunksDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    redirect_field_name = "login"
    model = chunks
    template_name = 'chunks/chunks_detail.html'
    
    #context_object_name = ''
    #template_name = ".html"
    
    
    
    
    
    
def get_object(self):
    object = super(chunksDetail , self).get_object()
    object.views_count += 1
    object.save()
    return object







def get_context_data(self, **kwargs):
    context = super(chunksDetail , self).get_context_data(**kwargs)
    context["links"] = chunksLinks.objects.filter(chunks=self.get_object())
    context['related_movies'] = chunks.objects.filter(category=self.get_object().category)
    return context



class chunksList(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = "login"
    model = chunks
    template_name = 'chunks/chunks_list.html'
    #context_object_name = ''
    #template_name = ".html"
    paginate_by: 2





class chunksCategory(ListView):
    model = chunks
    paginate_by: 2
    
    
    
    def get_queryset(self):
       self.category = self.kwargs['category']
       movies = chunks.objects.filter(category=self.category)
       return movies
       
       
       
    def get_context_data(self, **kwargs):
        context = super(chunksCategory , self).get_context_data(**kwargs)
        context['chunks_category'] = self.category
        return context
    
    
class chunksLanguage(ListView):
    model = chunks
    paginate_by = 2

    def get_queryset(self):
          self.language = self.kwargs['lang']
          return chunks.objects.filter(language=self.language)

    def get_context_data(self , **kwargs):
            context = super(chunksLanguage , self).get_context_data(**kwargs)
            context['chunks_language'] = self.language
            return context


class chunksSearch(ListView):
    model = chunks
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        
        else:
            object_list = self.model.objects.none()

        return object_list
    
class chunksYear(LoginRequiredMixin, YearArchiveView):
    login_url = 'login'
    redirect_field_name = "login"
    model = chunks
    template_name = 'chunks/chunks_archive_year.html'
    
    queryset = chunks.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True

    print(queryset)
    
    
    




