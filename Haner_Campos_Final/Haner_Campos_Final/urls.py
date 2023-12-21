"""
URL configuration for Haner_Campos_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seminarioapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexs),
    path('inscritos/', views.inscrito_list_view.as_view()),
    path('inscritos/<int:pk>/', views.inscrito_detail.as_view()),
    path('instituciones/', views.institucion_list),
    path('instituciones/<int:pk>/', views.institucion_detail),
    path('listarinscritos/', views.listadoinscrios),
    path('addinscrito/', views.addinscrito),
    path('editarinscritos/<int:IN_id>', views.modificarinscrito, name='modificarinscrito'),
    path('eliminarinscritos/<int:IN_id>', views.eliminarinscrito, name='eliminarinscritos'),
    path('listarinstituciones/', views.listadoinstituciones),
    path('addinstitucion/', views.addinstitucion),
    path('editarinstituciones/<int:IN_id>', views.modificarinstitucion, name='modificarinscrito'),
    path('eliminarinstituciones/<int:IN_id>', views.eliminarinstitucion, name='eliminarinscritos'),
]
