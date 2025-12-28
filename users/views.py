from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from notes.models import Note
from tasks.models import Task

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_notes'] = Note.objects.filter(user=self.request.user)[:5]
        context['pending_tasks'] = Task.objects.filter(user=self.request.user).exclude(status='completed')[:5]
        context['total_notes'] = Note.objects.filter(user=self.request.user).count()
        context['total_tasks'] = Task.objects.filter(user=self.request.user).count()
        return context

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
