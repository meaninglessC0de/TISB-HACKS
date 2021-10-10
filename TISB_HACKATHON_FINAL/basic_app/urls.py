from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about',views.AboutView.as_view(), name='about_us'),
    url(r'^map/(?P<pk>\d+)$',views.RoadMap, name='map'),
    url(r'^list',views.DoctorListView.as_view(),name='doctor_list'),
    url(r'^doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor_detail'),
    url(r'^doctorcomment/(?P<pk>\d+)/$', views.add_comment_to_doctor, name='add_comment_to_doctor'),
    url(r'^doctorreply/(?P<pk>\d+)/$', views.add_reply_to_comment, name='add_reply_to_comment'),
    url(r'^doctor/new/', views.CreateDoctorView.as_view(), name='doctor_new'),
    url(r'^doctoredit/(?P<pk>\d+)/$', views.DoctorUpdateView.as_view(), name='doctor_edit'),
    url(r'^doctorremove/(?P<pk>\d+)/$', views.DoctorDeleteView.as_view(), name='doctor_remove'),
    url(r'^doctorpatient/(?P<pk>\d+)/$', views.add_patient_to_dotctor, name='add_patient_to_dotctor'),
    url(r'^patient_detail_view/(?P<pk>\d+)/$',views.PatientDetailView.as_view(), name='patient_detail_view'),
    url(r'^$',views.HomePage.as_view(), name='home_page'),
]
