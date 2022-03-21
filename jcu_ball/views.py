from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BallReservation
from .forms import BallReservationForm
from .utils import download_csv


class BallReservationListView(generic.ListView):
    model = BallReservation
    paginate_by = 30

    def get_queryset(self):
        if self.request.GET.get('filter'):
            filter_val = self.request.GET.get('filter')
            new_queryset = BallReservation.objects.filter(full_name__icontains=filter_val)
            return new_queryset
        else:
            return BallReservation.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BallReservationListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter')
        return context

class BallReservationAddView(LoginRequiredMixin, generic.CreateView):
    model = BallReservation
    form_class = BallReservationForm
    success_url = reverse_lazy("jcu_ball:reservation_list")
    login_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BallReservationEditView(LoginRequiredMixin, generic.UpdateView):
    model = BallReservation
    form_class = BallReservationForm
    success_url = reverse_lazy("jcu_ball:reservation_list")
    login_url = reverse_lazy('accounts:login')


class BallReservationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BallReservation
    success_url = reverse_lazy("jcu_ball:reservation_list")
    login_url = reverse_lazy('accounts:login')


@login_required(login_url="accounts:login")
def export_csv(request):
    data = download_csv(request, BallReservation.objects.all())
    response = HttpResponse(data, content_type="text/csv")
    return response
