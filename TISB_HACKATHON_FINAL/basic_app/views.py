from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from basic_app.forms import DoctorForm, PatientForm, CommentForm, ReplyForm
from basic_app.models import Doctor,Patient, Comment, Reply

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import folium
from geopy.geocoders import ArcGIS
# Create your views here.


class HomePage(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'


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

def add_comment_to_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.doctor = doctor
            comment.save()
            return redirect('doctor_detail', pk=doctor.pk)
    else:
        form = CommentForm()
    return render(request, 'basic_app/comment_form.html', {'form': form})

def add_reply_to_comment(request, pk):
    # //doctor = get_object_or_404(Doctor, pk=pk)
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.save()
            return redirect('doctor_detail', pk=comment.doctor.pk)
    else:
        form = ReplyForm()
    return render(request, 'basic_app/reply_form.html', {'form': form})

def RoadMap(request,pk):

    doctor = get_object_or_404(Doctor, pk=pk)
    address = doctor.address

    arc = ArcGIS()
    x = arc.geocode(address)
    map1 = folium.Map(location = [x.latitude,x.longitude], zoom_start= 100, tiles = "Stamen Terrain")

    map1.add_child(folium.Marker(location = [x.latitude, x.longitude]))
    
    map1=map1._repr_html_()

    context={'map1':map1}

    return render(request, 'basic_app/map.html', context)
