from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = 'snacks/snack_list.html'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snacks/snack_detail.html'

class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snacks/snack_form.html'
    fields = ['title', 'purchaser', 'description']
    success_url = reverse_lazy('snack_list')

class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snacks/snack_form.html'
    fields = ['title', 'purchaser', 'description']
    success_url = reverse_lazy('snack_list')

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snacks/snack_confirm_delete.html'
    success_url = reverse_lazy('snack_list')
