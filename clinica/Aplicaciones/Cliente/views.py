from django.shortcuts import render, redirect
from .models import Paciente, Empleados, Consultas

# Create your views here.

#PAGINA PRINCIPAL
def home(request):
    return render(request, "base.html")

#DATOS DEL PACIENTE
def agregarPaciente(request):
    return render(request, "agregarPacientes.html")

def registrarPaciente(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']

    pacientes = Paciente.objects.create(codigo=codigo, nombre=nombre, sexo=sexo)
    return redirect('/')

def editarPaciente(request, codigo):
    pacientes = Paciente.objects.get(codigo=codigo)
    return render(request, "edicionPaciente.html", {"Pacientes": pacientes})

def edicionPaciente(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']

    paciente = Paciente.objects.get(codigo=codigo)
    paciente.nombre=nombre
    paciente.sexo=sexo
    paciente.save()
    return redirect('/')

def eliminarPaciente(request, codigo):
    paciente = Paciente.objects.get(codigo=codigo)
    paciente.delete()
    return redirect('/')

#DATOS DEL EMPLEADO
def agregarEmpleado(request):
    return render(request, "agregarEmpleado.html")

def registrarEmpleado(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    edad = request.POST['txtedad']
    profesion = request.POST['txtprofesion']

    empleados = Empleados.objects.create(codigo=codigo, nombre=nombre, sexo=sexo, edad=edad, profesion=profesion)
    return redirect('/')

def editarEmpleado(request, codigo):
    empleados =Empleados.objects.get(codigo=codigo)
    return render(request, "edicionPaciente.html", {"Empleados": empleados})

def edicionEmpleado(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    edad = request.POST['txtedad']
    profesion = request.POST['txtprofesion']

    empleado = Empleados.objects.get(codigo=codigo)
    empleado.nombre=nombre
    empleado.sexo=sexo
    empleado.edad=edad
    empleado.profesion=profesion
    empleado.save()
    return redirect('/')

def eliminarEmpleado(request, codigo):
    empleado = Empleados.objects.get(codigo=codigo)
    empleado.delete()
    return redirect('/')

#DATOS DEL EMPLEADO
def agregarConsulta(request):
    return render(request, "agregarConsulta.html")

def registrarConsulta(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    edad = request.POST['txtedad']
    especialidad = request.POST['txtespecialidad']
    motivo = request.POST['txtmotivo']

    consultas = Consultas.objects.create(codigo=codigo, nombre=nombre, sexo=sexo, edad=edad, especialidad=especialidad, motivo=motivo)
    return redirect('/')

def editarConsulta(request, codigo):
    consultas =Consultas.objects.get(codigo=codigo)
    return render(request, "edicionConsulta.html", {"Consultas": consultas})

def edicionConsulta(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    sexo = request.POST['txtsexo']
    edad = request.POST['txtedad']
    especialidad = request.POST['txtespecialidad']
    motivo = request.POST['txtmotivo']

    consulta = Consultas.objects.get(codigo=codigo)
    consulta.nombre=nombre
    consulta.sexo=sexo
    consulta.edad=edad
    consulta.especialidad=especialidad
    consulta.motivo=motivo
    consulta.save()
    return redirect('/')

def eliminarConsulta(request, codigo):
    consulta = Consultas.objects.get(codigo=codigo)
    consulta.delete()
    return redirect('/')
       