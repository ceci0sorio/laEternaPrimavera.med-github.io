from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregarPaciente/', views.agregarPaciente),
    path('registrarPaciente/', views.registrarPaciente),
    path('editarPaciente/<codigo>', views.editarPaciente),
    path('edicionPaciente/', views.edicionPaciente),
    path('eliminarPaciente/<codigo>', views.eliminarPaciente),

    path('agregarEmpleado/', views.agregarEmpleado),
    path('registrarEmpleado/', views.registrarEmpleado),
    path('editarEmpleado/<codigo>', views.editarEmpleado),
    path('edicionEmpleado/', views.edicionEmpleado),
    path('eliminarEmpleado/<codigo>', views.eliminarEmpleado),

    path('agregarConsulta/', views.agregarConsulta),
    path('registrarConsulta/', views.registrarConsulta),
    path('editarConsulta/<codigo>', views.editarConsulta),
    path('edicionConsulta/', views.edicionConsulta),
    path('eliminarConsulta/<codigo>', views.eliminarConsulta)
    ]
