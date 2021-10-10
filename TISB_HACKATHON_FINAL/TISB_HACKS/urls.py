"""TISB_HACKS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""  
from django.conf.urls import url,include
from django.contrib import admin

from django.contrib.auth import views
from blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/logout/$',views.logout,name='logout',kwargs={"next_page":'/list'}),
    url(r'',include('basic_app.urls')),
    url(r'^index/$',blog_views.PostListView.as_view(),name='post_list'),
    url(r'^comments/$',blog_views.CommentListView.as_view(), name='comment_list'),
    url(r'^post/(?P<pk>\d+)$', blog_views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', blog_views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', blog_views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', blog_views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', blog_views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', blog_views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', blog_views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)$', blog_views.CommentDetailView.as_view(), name='comment_detail_view'),
]
