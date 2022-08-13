from django.urls import path
from . import views

urlpatterns = [

    path ('', views.index, name='index' ),
    path ('signup', views.signup, name='signup' ),
    path ('new_page_css', views.new_page_css, name='new_page_css'),
    path ('baabtra', views.baabtra, name='baabtra'),
    path ('bootstrap', views.bootstrap, name='bootstrap'),
    path ('newpage', views.newpage, name='newpage'),
    path ('bootstrap_grid', views.bootstrap_grid, name='bootstrap_grid'),
     
]