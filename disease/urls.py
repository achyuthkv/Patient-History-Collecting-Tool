from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .import views
urlpatterns = [

 	url(r'^symptom',views.symptom,name='symptom'),
 	url(r'^question',views.question_page,name='question_page'),
    url(r'^check/(?P<qid>\d+)/$', views.check, name='check')

 	]
