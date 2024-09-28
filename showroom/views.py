from django.shortcuts import render, redirect
from .models import Car_Detail, Brand
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .forms import CommentForm

# Create your views here.

def home(request, brand_slug=None):
    data = Car_Detail.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug= brand_slug)
        data = Car_Detail.objects.filter( brand = brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'cars': data, 'brands': brands})



def user_comments(request, id):
    car = Car_Detail.objects.get(pk=id)
    comments = car.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'comment_form': comment_form})

@login_required
def buy_car(request, id):
    car = Car_Detail.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car=car)
    return redirect('profile')