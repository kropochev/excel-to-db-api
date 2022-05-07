from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url('upload/', views.UploadFilesView.as_view(), name='upload'),
    url('clients/', views.ClientsViewSet.as_view(), name='clients'),
    url('bills/', views.BillsViewSet.as_view(), name='bills'),
]
