from django.conf.urls import url
from django.views.generic import TemplateView

from app.views import ProblemList, UserList

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='app/index.html')),
    url(r'^problems/$', ProblemList.as_view(), name='problems'),
    url(r'^users/$', UserList.as_view(), name='rank'),
]
