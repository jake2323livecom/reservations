from django.shortcuts import render, redirect
from django.views import generic
from jcu_ball.models import BallReservation
from summer_picnic.models import PicnicReservation

def home(request):
    return render(request, 'home.html', {})

class Testing(generic.ListView):
    model = BallReservation
    paginate_by = 12
    template_name = 'testing.html'