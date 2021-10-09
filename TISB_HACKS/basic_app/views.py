from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from basic_app.forms import DoctorForm, PatientForm
from basic_app.models import Doctor,Patient

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.



class DoctorListView(ListView):
    model=Doctor

class DoctorDetailView(DetailView):
    model=Doctor

# class PatientDetailView(DetailView):
#     model=Patient


class CreateDoctorView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    redirect_field_name='basic_app/doctor_detail.html'
    form_class=DoctorForm
    model=Doctor

class DoctorUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'basic_app/doctor_detail.html'

    form_class = DoctorForm
    model = Doctor

class DoctorDeleteView(LoginRequiredMixin,DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctor_list')

class PatientDetailView(LoginRequiredMixin, DetailView):
    model= Patient
    

## Functions

def add_patient_to_dotctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.doctor = doctor
            patient.save()
            return redirect('doctor_detail', pk=doctor.pk)
    else:
        form = PatientForm()
    return render(request, 'basic_app/patient_form.html', {'form': form})
