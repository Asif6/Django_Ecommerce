

from django.urls import path
from .views.index import Index
from .views.users import Signup,Login,Logout

urlpatterns = [
    path("",Index.as_view(), name="index"),
    path("signup/",Signup.as_view(), name="signup"),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout')
]
