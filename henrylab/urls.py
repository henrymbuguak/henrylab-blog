from  django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact_page, name='contact_page'),
    url(r'^contact/success/$', TemplateView.as_view(template_name='henrylab/success.html')),
    url(r'^service/$', TemplateView.as_view(template_name='henrylab/service.html')),
    
] 