from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum

# Create your views here.
def home(request):
   widget_list = Widget.objects.all()
   widget_form = WidgetForm()
   total = Widget.objects.aggregate(Sum('quantity'))['quantity__sum']
   return render(request, 'home.html', {'widget_list': widget_list, 'widget_form': widget_form, 'total': total})

def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
      form.save()
   #  new_widget.save()
  return redirect('home')

def delete_widget(request, widget_id):
   Widget.objects.get(id=widget_id).delete()
   return redirect('home')