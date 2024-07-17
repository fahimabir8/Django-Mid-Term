from django.shortcuts import render,redirect
from .models import Car,Purchase
from django.views.generic import DetailView
from .forms import CommentForm
from brand.models import Brand
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.
def home(request, brand_slug=None):
    cars = Car.objects.all()
    
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand=brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'cars': cars, 'brands': brands} )


class details(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car 
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = CommentForm()
            
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
@method_decorator(login_required, name='dispatch')
class buycar(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'profile.html'
    
    def post(self, request, *args, **kwargs):
        car = self.get_object()
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            Purchase.objects.create(user=request.user, car=car)
            return redirect('profile')  
        else:
            return redirect('details', id=car.id) 