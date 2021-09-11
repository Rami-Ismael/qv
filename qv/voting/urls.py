
from django.urls.conf import path
from voting import views

urlpatterns  = [
    path("",views.blank)
]