from django.urls import path

from tt.views import addd, addp


urlpatterns = [
    path('addp', addp),
    path('addd', addd),
]