from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import MyModel
from django.views import View
from .forms import MyForm

# from .forms import AddSnippetsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView




class FileUploadCreate(CreateView):
    model = MyModel
    template_name = 'file_upload/file_upload_create_form.html'
    # form_class = MyForm
    fields = ['tahun','upload']
    
    success_url = '.././' 

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)