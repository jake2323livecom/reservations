from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import PicnicReservation
from .forms import PicnicReservationForm
from .utils import download_csv

# Create your views here.

class PicnicReservationListView(generic.ListView):
    model = PicnicReservation
    paginate_by = 30

    def get_queryset(self):
        if self.request.GET.get('filter'):
            filter_val = self.request.GET.get('filter')
            new_queryset = PicnicReservation.objects.filter(full_name__icontains=filter_val)
            return new_queryset
        else:
            return PicnicReservation.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PicnicReservationListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter')
        return context

class PicnicReservationAddView(LoginRequiredMixin, generic.CreateView):
    model = PicnicReservation
    form_class = PicnicReservationForm
    success_url = reverse_lazy("summer_picnic:reservation_list")
    login_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PicnicReservationEditView(LoginRequiredMixin, generic.UpdateView):
    model = PicnicReservation
    form_class = PicnicReservationForm
    success_url = reverse_lazy("summer_picnic:reservation_list")
    login_url = reverse_lazy('accounts:login')

class PicnicReservationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PicnicReservation
    success_url = reverse_lazy("summer_picnic:reservation_list")
    login_url = reverse_lazy('accounts:login')

@login_required(login_url="accounts:login")
def export_csv(request):
    data = download_csv(request, PicnicReservation.objects.all())
    response = HttpResponse(data, content_type="text/csv")
    return response

