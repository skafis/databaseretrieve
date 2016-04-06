from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.show_list, name='show_list'),
    # url(r'^list/\d+/$', views.detail_view, name="details")
    ]