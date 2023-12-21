from django.shortcuts import redirect, render

from seminarioapi.forms import InscritoForm, InstitucionForm
from .serializers import InscritoSerializer, InstitucionSerializer
from .models import Inscrito, Institucion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#class base view imports
from rest_framework.views import APIView
from django.http import Http404

class inscrito_list_view(APIView):
    def get(self, request, format=None):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class inscrito_detail(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        inscrito = self.get_object(pk)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        inscrito = self.get_object(pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detail(request, pk):
    try:
        instituciones = Institucion.objects.get(pk=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitucionSerializer(instituciones)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InstitucionSerializer(instituciones, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        instituciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def listadoinscrios(request):
    inscritos = Inscrito.objects.all()
    return render(request, 'inscritos.html', {'inscritos': inscritos})

def addinscrito(request):
    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarInscritos')
    else:
        form = InscritoForm()
    return render(request, 'addinscritos.html', {'form': form})

def modificarinscrito(request, IN_id):
    Inscritos = Inscrito.objects.get(id = IN_id)
    form = InscritoForm(instance=Inscritos)

    if (request.method == 'POST'):
        form = InscritoForm(request.POST, instance=Inscritos)
        if (form.is_valid()):
            form.save()
            return redirect('/listarinscritos')

    data = {'form': form}
    return render (request, 'addinscritos.html', data)

def eliminarinscrito(request, IN_id):
    Inscritos = Inscrito.objects.get(id = IN_id)
    Inscritos.delete()
    return redirect('/listarinscritos')

def listadoinstituciones(request):
    instituciones = Institucion.objects.all()
    return render(request, 'instituciones.html', {'instituciones': instituciones})

def addinstitucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarinstituciones')
    else:
        form = InstitucionForm()
    return render(request, 'addinstitucion.html', {'form': form})

def modificarinstitucion(request, IN_id):
    Instituciones = Institucion.objects.get(id = IN_id)
    form = InstitucionForm(instance=Instituciones)

    if (request.method == 'POST'):
        form = InstitucionForm(request.POST, instance=Instituciones)
        if (form.is_valid()):
            form.save()
            return redirect('/listarinstituciones')

    data = {'form': form}
    return render (request, 'addinstitucion.html', data)

def eliminarinstitucion(request, IN_id):
    Instituciones = Institucion.objects.get(id = IN_id)
    Instituciones.delete()
    return redirect('/listarinstituciones')

def indexs(request):
    return render(request, 'index.html')