from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from .models import EntryModel
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = EntryModel

    def get_context_data(self, **kwargs):
        all_data = EntryModel.objects.all()
        context = {
            'all_entries': all_data
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)

class AddEntryView(TemplateView):
    template_name = 'add_entry.html'

    def post(self, request, *args, **kwargs):
        print(request.POST.keys())
        if request.method == 'POST':
            name = request.POST.get('name', '') 
            text = request.POST.get('text', '')
            email = request.POST.get('email', '')
            gender = request.POST.get('gender', '')
            age = request.POST.get('age', '')
            dob = request.POST.get('date_of_birth', '')
            EntryModel.objects.create(name=name, text=text, email=email, gender=gender, age=age, date_of_birth=dob)
            return redirect(reverse('home_url'))
        return self.get(request, *args, **kwargs)
    
class UpdateEntryView(UpdateView):
    template_name = 'edit_entry.html'
    model = EntryModel
    fields = '__all__'
    success_url = '/home'

    def get(self, request, *args, **kwargs):
        print('entering')
        data = EntryModel.objects.filter(name=kwargs['pk']).first()
        context = {
            'data': data
        }
        kwargs.update(context)
        return super().get(request, *args, **kwargs)
    
class DeleteEntryView(DeleteView):
    template_name = 'delete_entry.html'
    model = EntryModel
    success_url = '/home'


