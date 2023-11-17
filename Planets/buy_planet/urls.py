from django.urls import path
from . import views
from .views import show_by_category

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('planets/', views.show_planets, name='planets'),
    path('check/', views.check),
    path('planet/<int:planet_id>/', views.show_planet, name='planet'),
    path('bought/', views.buy_object, name='buy'),
    path('o_no/', views.no, name='no'),
    path('cat/<int:cat_id>/', show_by_category, name='categs')
]
