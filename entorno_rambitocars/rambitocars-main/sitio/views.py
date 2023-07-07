from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'sitio/index.html', data)

def catalogo(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'sitio/catalogo.html', data)

def comentarios(request):
    return render(request, 'sitio/comentarios.html')

def contacto(request):
    return render(request, 'sitio/contacto.html')


def compra_supra(request):
    return render(request, 'sitio/compra/compra_supra.html')

def compra_subaru(request):
    return render(request, 'sitio/compra/compra_subaru.html')

def compra_nissan(request):
    return render(request, 'sitio/compra/compra_nissan.html')

def compra_350z(request):
    return render(request, 'sitio/compra/compra_350z.html')

def metodo_pago(request):
    return render(request, 'sitio/compra/metodo_pago.html')

def compra_realizada(request):
    return render(request, 'sitio/compra/compra_realizada.html')

def loginadmin(request):
    return render(request, 'sitio/admin/loginadmin.html')

def baseadmin(request):
    return render(request, 'sitio/admin/baseadmin.html')

def registroadmin(request):
    return render(request, 'sitio/admin/registroadmin.html')

def contraseñaadmin(request):
    return render(request, 'sitio/admin/contraseñaadmin.html')

def productoadmin(request):
    return render(request, 'sitio/admin/productoadmin.html')

def clienteadmin(request):
    return render(request, 'sitio/admin/clienteadmin.html')

def pedidosadmin(request):
    return render(request, 'sitio/admin/pedidosadmin.html')

def login(request):
    return render(request, 'sitio/usuario/login.html')

def registro(request):
    return render(request, 'sitio/usuario/registro.html')

def home(request):
    cursosListados = Producto.objects.all()
    messages.success(request, '¡Autos listados!')
    return render(request, "sitio/prueba/gestionCursos.html", {"cursos": cursosListados})


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Producto.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Auto registrado!')
    return render(request,"sitio/admin/baseadmin.html")


def edicionProducto(request, codigo):
    curso = Producto.objects.get(codigo=codigo)
    return render(request, "sitio/prueba/edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Producto.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Auto actualizado!')

    return render(request,"sitio/admin/baseadmin.html")


def eliminarCurso(request, codigo):
    curso = Producto.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Auto eliminado!')

    return render(request, "sitio/admin/baseadmin.html")





def Persona(request):
    PersonaListada = Producto.objects.all()
    messages.success(request, '¡Personas Listadas!')
    return render(request, "sitio/registro/gestionPersona.html", {"cursos": PersonaListada})


def registrarPersona(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Producto.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Persona registrada!')
    return render(request,"sitio/admin/baseadmin.html")


def edicionPersona(request, codigo):
    curso = Producto.objects.get(codigo=codigo)
    return render(request, "sitio/registro/edicionPersona.html", {"curso": curso})


def editarPersona(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Producto.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Persona actualizado!')

    return render(request,"sitio/admin/baseadmin.html")


def eliminarPersona(request, codigo):
    curso = Producto.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Persona eliminado!')

    return render(request, "sitio/admin/baseadmin.html")