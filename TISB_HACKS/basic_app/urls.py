from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index',views.DoctorListView.as_view(),name='doctor_list'),
    url(r'^doctor/(?P<pk>\d+)', views.DoctorDetailView.as_view(), name='doctor_detail'),
    url(r'^doctor/new/', views.CreateDoctorView.as_view(), name='doctor_new'),
    url(r'^doctoredit/(?P<pk>\d+)/$', views.DoctorUpdateView.as_view(), name='doctor_edit'),
    url(r'^doctorremove/(?P<pk>\d+)/$', views.DoctorDeleteView.as_view(), name='doctor_remove'),
    url(r'^doctorpatient/(?P<pk>\d+)/$', views.add_patient_to_dotctor, name='add_patient_to_dotctor'),
    url(r'^patientdetail/(?P<pk>\d+)/$',views.PatientDetailView, name='patient_detail')
]
