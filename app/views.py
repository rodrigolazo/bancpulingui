from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import *

from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


from .filters import PostFilter
from django.contrib import messages


def pdfs(request):
	context = {}
	return render(request, 'pdf.html', context)

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class ViewPDF(View):

	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf.html')
		return HttpResponse(pdf, content_type='application/pdf')

        

# Create your views here.

def index (request):
    posts = Post.objects.filter(active=True)
    testimonio = Testimonio.objects.filter(active=True)
    navs= NavProducto.objects.filter(active=True)
    servicio = NavServicio.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True)
    noticiaMain = NoticiaInicio.objects.filter(active=True)[0:2]

 
    
    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {'posts':posts,'testimonio':testimonio,'navs':navs,'institucion':institucion,'noticiaMain':noticiaMain,
                'num_visits':num_visits,
                'servicio':servicio}

    

    return render (request, 'index.html',context)



def quienesSomos (request):
    navs= NavProducto.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True)  
    servicio = NavServicio.objects.filter(active=True)
    context = {'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'nosotros.html',context)





def contactos (request):
    navs= NavProducto.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True) 
    servicio = NavServicio.objects.filter(active=True) 
    context = {'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'contactos.html',context)



#Crud baner

@login_required(login_url='home')
def insertBaner(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'baner/insert.html',context)

@login_required(login_url='home')
def editarBaner(request, pk):
    post =  Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'baner/insert.html',context)

@login_required(login_url='home')
def eliminarBaner(request, pk):
    post =  Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('home')    
    context = {'item':post}
    return render (request, 'baner/delete.html',context)

@login_required(login_url='home')
def listarBaner(request):
    listpost =  Post.objects.all()
    context = {'listpost':listpost }
    return render (request, 'baner/list-baner.html',context)



def postBaner(request, pk):
    post =  Post.objects.get(id=pk)
    navs= NavProducto.objects.filter(active=True)  
    servicio = NavServicio.objects.filter(active=True) 
    institucion = Institucion.objects.filter(active=True)  
    
    context = {'post':post,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'baner/post.html',context)





#Crud Noticias
def noticias(request):
    posts = Noticia.objects.filter(activate=True)
    navs= NavProducto.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True) 
    servicio = NavServicio.objects.filter(active=True)
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(posts,3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts,'navs':navs,'institucion':institucion,'myFilter':myFilter,'servicio':servicio}
    
    return render (request, 'noticias/index.html',context)

@login_required(login_url='noticias')

def insertNoticia(request):
    form = NoticiaForm()
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('noticias')    
    context = {'form':form}
    return render (request, 'noticias/insert.html',context)


@login_required(login_url='noticias')
def editarNoticia(request, pk):
    post =  Noticia.objects.get(id=pk)
    form = NoticiaForm(instance=post)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('noticias')    
    context = {'form':form}
    return render (request, 'noticias/insert.html',context)

@login_required(login_url='noticias')
def eliminarNoticia(request, pk):
    post =  Noticia.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('noticias')    
    context = {'item':post}
    return render (request, 'noticias/delete.html',context)

@login_required(login_url='noticias')
def listarNoticia(request):
    listpost =  Noticia.objects.all()
    context = {'listpost':listpost }
    return render (request, 'noticias/list-noticias.html',context)

def postNoticia(request, pk):
    post =  Noticia.objects.get(id=pk)  
    navs= NavProducto.objects.filter(active=True)
    servicio = NavServicio.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True)
    context = {'post':post,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'noticias/post-noticia.html',context)


#crud Galeria
def galeria (request):
    posts = Galeria.objects.filter(active=True)
    navs= NavProducto.objects.filter(active=True)
    servicio = NavServicio.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True) 
    context = {'posts':posts,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'galeria/galeria.html',context)

@login_required(login_url='galeria')
def insertGaleria(request):
    form = GaleriaForm()
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('galeria')    
    context = {'form':form}
    return render (request, 'galeria/create.html',context)


@login_required(login_url='galeria')
def editarGaleria(request, pk):
    post =  Galeria.objects.get(id=pk)
    form = GaleriaForm(instance=post)
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('galeria')    
    context = {'form':form}
    return render (request, 'galeria/create.html',context)

@login_required(login_url='galeria')
def eliminarGaleria(request, pk):
    post =  Galeria.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('galeria')    
    context = {'item':post}
    return render (request, 'galeria/delete.html',context)

@login_required(login_url='galeria')
def listarGaleria(request):
    listpost =  Galeria.objects.all()
    context = {'listpost':listpost }
    return render (request, 'galeria/listgalery.html',context)


#-------------CRUD Productos---------------------------------
def servicios (request):
    posts = Producto.objects.filter(active=True)
    navs= NavProducto.objects.filter(active=True) 
    servicio = NavServicio.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True) 
    context = {'posts':posts,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'productos/servicios.html',context )


@login_required(login_url='servicios')
def insertServicio(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('servicios')    
    context = {'form':form}
    return render (request, 'productos/create.html',context)


@login_required(login_url='servicios')
def editarServicio(request, pk):
    post =  Producto.objects.get(id=pk)
    form = ProductoForm(instance=post)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('servicios')    
    context = {'form':form}
    return render (request, 'productos/create.html',context)

@login_required(login_url='servicios')
def eliminarServicio(request, pk):
    post =  Producto.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('servicios')    
    context = {'item':post}
    return render (request, 'productos/delete.html',context)

@login_required(login_url='servicios')
def listarSercivio(request):
    listpost =  Producto.objects.all()
    context = {'listpost':listpost }
    return render (request, 'productos/listproduct.html',context)

def postServicio(request, pk):
    post =  Producto.objects.get(id=pk)  
    navs= NavProducto.objects.filter(active=True) 
    servicio = NavServicio.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True) 
    context = {'post':post,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'productos/post-product.html',context)


#-------------CRUD Testimonios ---------------------------------


@login_required(login_url='home')
def inserTestimonio(request):
    form = TestimonioForm()
    if request.method == 'POST':
        form = TestimonioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'testimonios/create.html',context)


@login_required(login_url='home')
def editarTestimonio(request, pk):
    post = Testimonio.objects.get(id=pk)
    form = TestimonioForm(instance=post)
    if request.method == 'POST':
        form = TestimonioForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'testimonios/create.html',context)

@login_required(login_url='home')
def eliminarTestimonio(request, pk):
    post = Testimonio.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('home')    
    context = {'item':post}
    return render (request, 'testimonios/delete.html',context)

@login_required(login_url='home')
def listarTestimonio(request):
    listpost =  Testimonio.objects.all()
    context = {'listpost':listpost }
    return render (request, 'testimonios/list-testimonio.html',context)



#-----------CRUD de Nav Producto



def postNavProducto(request,pk):
    post =  NavProducto.objects.get(id=pk) 
    navs= NavProducto.objects.filter(active=True) 
    servicio = NavServicio.objects.filter(active=True)
    institucion = Institucion.objects.filter(active=True)  
    context = {'post':post,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'navproducto/post-nav.html',context)


@login_required(login_url='home')
def inserNavProducto (request):
    form = NavProductoForm()
    if request.method == 'POST':
        form = NavProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'navproducto/create.html',context)


@login_required(login_url='home')
def editarNavProducto(request, pk):
    post = NavProducto.objects.get(id=pk)
    form = NavProductoForm(instance=post)
    if request.method == 'POST':
        form = NavProductoForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'navproducto/create.html',context)

@login_required(login_url='home')
def eliminarNavProducto(request, pk):
    post = NavProducto.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('home')    
    context = {'item':post}
    return render (request, 'navproducto/delete.html',context)

@login_required(login_url='home')
def listarNavProducto (request):
    listpost =  NavProducto.objects.all()
    navs = NavProducto.objects.filter(active=True) 
    context = {'listpost':listpost,'navs':navs}
    return render (request, 'navproducto/list-nav.html',context)


#-----------CRUD de Nav institucion

def postInstitucion(request,pk):
    post =  Institucion.objects.get(id=pk) 
    navs = NavProducto.objects.filter(active=True) 
    servicio = NavServicio.objects.filter(active=True)  
    institucion = Institucion.objects.filter(active=True)
    context = {'post':post,'navs':navs,'institucion':institucion,'servicio':servicio}
    return render (request, 'institucion/post-institucion.html',context)


@login_required(login_url='home')
def inserInstitucion (request):
    form = InstitucionForm()
    if request.method == 'POST':
        form = InstitucionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'institucion/create.html',context)


@login_required(login_url='home')
def editarInstitucion(request, pk):
    post = Institucion.objects.get(id=pk)
    form = InstitucionForm(instance=post)
    if request.method == 'POST':
        form = InstitucionForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'institucion/create.html',context)

@login_required(login_url='home')
def eliminarInstitucion(request, pk):
    post = Institucion.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('home')    
    context = {'item':post}
    return render (request, 'institucion/delete.html',context)

@login_required(login_url='home')
def listarInstitucion  (request):
    listpost =  Institucion.objects.all()
    institucion = Institucion.objects.filter(active=True) 
    context = {'listpost':listpost,'institucion':institucion}
    return render (request, 'institucion/list-intitucion.html',context)



#-----------CRUD de Nav Servicios

def postServicios(request,pk):
    post =  NavServicio.objects.get(id=pk) 
    servicio = NavServicio.objects.filter(active=True)   
    institucion = Institucion.objects.filter(active=True)
    navs = NavProducto.objects.filter(active=True)
    context = {'post':post,'servicio':servicio,'institucion':institucion,'navs':navs }
    return render (request, 'serviciosnav/post.html',context)


@login_required(login_url='home')
def inserServicios(request):
    form = NavServicioForm()
    if request.method == 'POST':
        form = NavServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'serviciosnav/create.html',context)


@login_required(login_url='home')
def editarServicios(request, pk):
    post = NavServicio.objects.get(id=pk)
    form = NavServicioForm(instance=post)
    if request.method == 'POST':
        form = NavServicioForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'serviciosnav/create.html',context)

@login_required(login_url='home')
def eliminarServicios(request, pk):
    post = NavServicio.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('home')    
    context = {'item':post}
    return render (request, 'serviciosnav/delete.html',context)

@login_required(login_url='home')
def listarServicios(request):
    listpost =  NavServicio.objects.all()
    servicio = NavServicio.objects.filter(active=True) 
    context = {'listpost':listpost,'servicio':servicio}
    return render (request, 'serviciosnav/list.html',context)


#-----------CRUD Noticias pagina Principal



def postInformacion(request,pk):
    post =  NoticiaInicio.objects.get(id=pk) 
    navs = NavProducto.objects.filter(active=True)   
    institucion = Institucion.objects.filter(active=True)
    servicio = NavServicio.objects.filter(active=True) 
    context = {'post':post,'navs':navs,'institucion':institucion,'servicio':servicio }
    return render (request, 'noticiainicio/post-noticia.html',context)


@login_required(login_url='home')
def inserInformacion (request):
    form = NoticiaMainForm()
    if request.method == 'POST':
        form = NoticiaMainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'noticiainicio/create.html',context)


@login_required(login_url='home')
def editarInformacion(request, pk):
    post = NoticiaInicio.objects.get(id=pk)
    form = NoticiaMainForm(instance=post)
    if request.method == 'POST':
        form = NoticiaMainForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('home')    
    context = {'form':form}
    return render (request, 'noticiainicio/create.html',context)

@login_required(login_url='home')
def eliminarInformacion(request, pk):
    post = NoticiaInicio.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('home')    
    context = {'item':post}
    return render (request, 'noticiainicio/delete.html',context)

@login_required(login_url='home')
def listarInformacion (request):
    listpost =  NoticiaInicio.objects.all()
    context = {'listpost':listpost}
    return render (request, 'noticiainicio/list-noticia.html',context)






#formulario de solicitud de credito

def applicationForm(request):
    navs= NavProducto.objects.filter(active=True) 
    institucion = Institucion.objects.filter(active=True)
    context = {'navs':navs,'institucion':institucion}
    return render (request, 'solicitud/solicitud.html',context)

def createRequest(request):

    socio = request.POST.get('socioN')
    deudor = request.POST.get('deudor')
    garante = request.POST.get('garante')
    numsocio = request.POST.get('numsocio')
    fecha = request.POST.get('fecha')
    monto = request.POST.get('monto')
    plazo = request.POST.get('plazo')
    destinoP = request.POST.get('destinoP')
    otroDes = request.POST.get('otroDes')
    cuotas = request.POST.get('cuotas')
    fechaPago = request.POST.get('fechaPago')
    montoPagar = request.POST.get('montoPagar')
    nombres = request.POST.get('nombres')
    cedula = request.POST.get('cedula')
    nivelA = request.POST.get('nivelA')
    correo = request.POST.get('correo')
    estadoCivil = request.POST.get('estadoCivil')
    edad = request.POST.get('edad')
    domicilio = request.POST.get('domicilio')
    canton = request.POST.get('canton')
    parroquia = request.POST.get('parroquia')
    comunidad = request.POST.get('comunidad')
    sectorBarrio = request.POST.get('sectorBarrio')
    ciudadela = request.POST.get('ciudadela')
    direccion = request.POST.get('direccion')
    numCasa = request.POST.get('numCasa')
    refDomicilio = request.POST.get('refDomicilio')
    telefono = request.POST.get('telefono')
    celular = request.POST.get('celular')
    cargaFamiliar = request.POST.get('cargaFamiliar')
    separacion = request.POST.get('separacion')
    estadoCasa = request.POST.get('estadoCasa')
    viviendaOtro = request.POST.get('viviendaOtro')
    tiempoResidencia = request.POST.get('tiempoResidencia')
    nombreEmpresa = request.POST.get('nombreEmpresa')
    dirEmpresa = request.POST.get('dirEmpresa')
    provinciaEmpresa = request.POST.get('provinciaEmpresa')
    cantonEmpresa = request.POST.get('cantonEmpresa')
    parroquiaEmpresa = request.POST.get('parroquiaEmpresa')
    telEmpresa = request.POST.get('telEmpresa')
    tiempoTrabajo = request.POST.get('tiempoTrabajo')
    cargoEmpresa = request.POST.get('cargoEmpresa')
    sueldoEmpresa = request.POST.get('sueldoEmpresa')
    nombresConyuge = request.POST.get('nombresConyuge')
    cedulaConyuge  = request.POST.get('cedulaConyuge')
    nivelConyuge = request.POST.get('nivelConyuge')
    correoConyuge = request.POST.get('correoConyuge')
    telConyuge = request.POST.get('telConyuge')
    edadConyuge = request.POST.get('edadConyuge')
    nombreEmpresaConyuge = request.POST.get('nombreEmpresaConyuge')
    dirEmpresaConyuge = request.POST.get('dirEmpresaConyuge')
    provinciaConyuge = request.POST.get('provinciaConyuge')
    cantonConyuge = request.POST.get('cantonConyuge')
    parroquiaConyuge = request.POST.get('parroquiaConyuge')
    telEmpresaConyuge = request.POST.get('telEmpresaConyuge')
    tiempoTraConyuge = request.POST.get('tiempoTraConyuge')
    cargoConyuge = request.POST.get('cargoConyuge')
    sueldoConyuge = request.POST.get('sueldoConyuge')
    nombreNegocio = request.POST.get('nombreNegocio')
    dirNegocio = request.POST.get('dirNegocio')
    provinciaNegocio = request.POST.get('provinciaNegocio')
    cantonNegocio = request.POST.get('cantonNegocio')
    parroquiaNegocio = request.POST.get('parroquiaNegocio')
    telNegocio = request.POST.get('telNegocio')
    tiempoNegocio = request.POST.get('tiempoNegocio')
    cargoNegocio = request.POST.get('cargoNegocio')
    utilidadNegocio = request.POST.get('utilidadNegocio')
    nombreFamilia1 = request.POST.get('nombreFamilia1')
    nombreFamilia2 = request.POST.get('nombreFamilia2')
    dirFamilia1 = request.POST.get('dirFamilia1')
    dirFamilia2 = request.POST.get('dirFamilia2')
    parentesco1 = request.POST.get('parentesco1')
    parentesco2 = request.POST.get('parentesco2')
    telFamilia1 = request.POST.get('telFamilia1')
    telFamilia2 = request.POST.get('telFamilia2')
    nombreBanco1 = request.POST.get('nombreBanco1')
    nombreBanco2 = request.POST.get('nombreBanco2')
    ahorros1  = request.POST.get('ahorros1')
    ahorros2  = request.POST.get('ahorros2')
    corriente1 = request.POST.get('corriente1')
    corriente2 = request.POST.get('corriente2')
    salPromedio1 = request.POST.get('salPromedio1')
    salPromedio2 = request.POST.get('salPromedio2')
    refComercial = request.POST.get('refComercial')
    dirComercial = request.POST.get('dirComercial')
    telComercial = request.POST.get('telComercial')
    compra  = request.POST.get('compra')
    efectivo = request.POST.get('efectivo')
    deudaBanco = request.POST.get('deudaBanco')
    cuentaCobrar = request.POST.get('cuentaCobrar')
    deudaCobrar = request.POST.get('deudaCobrar')
    mercaderia = request.POST.get('mercaderia')
    proveedores = request.POST.get('proveedores')
    terreno = request.POST.get('terreno')
    casaComercial = request.POST.get('casaComercial')
    casa = request.POST.get('casa')
    prestamista = request.POST.get('prestamista')
    vehiculo = request.POST.get('vehiculo')
    otrasdeudas = request.POST.get('otrasdeudas')
    bienesEnseres = request.POST.get('bienesEnseres')
    otrosActivos = request.POST.get('otrosActivos')
    sueldoMensual = request.POST.get('sueldoMensual')
    gastosAlimentos = request.POST.get('gastosAlimentos')
    utilidadMensual = request.POST.get('utilidadMensual')
    gastosServicios = request.POST.get('gastosServicios')
    salarioConyuge  = request.POST.get('salarioConyuge')
    gastoSalud = request.POST.get('gastoSalud')
    agricultorG  = request.POST.get('agricultorG')
    pagoPrestamo = request.POST.get('pagoPrestamo')
    otrosIngresos = request.POST.get('otrosIngresos')
    otrosGastos = request.POST.get('otrosGastos')
    if request.method == 'POST':
        Credito.objects.create(socio=socio,deudor=deudor,garante=garante,
                                numsocio=numsocio,fecha=fecha,monto=monto,
                                plazo=plazo,destinoP=destinoP,otroDes=otroDes,
                                cuotas=cuotas,fechaPago=fechaPago,montoPagar=montoPagar,
                                nombres=nombres,cedula=cedula,nivelA=nivelA,correo=correo,
                                estadoCivil=estadoCivil,edad=edad,domicilio=domicilio,
                                canton=canton,parroquia=parroquia,comunidad=comunidad,
                                sectorBarrio=sectorBarrio,ciudadela=ciudadela,direccion=direccion,
                                numCasa=numCasa,refDomicilio=refDomicilio,telefono=telefono,
                                celular=celular,cargaFamiliar=cargaFamiliar,separacion=separacion,
                                estadoCasa=estadoCasa,viviendaOtro=viviendaOtro,tiempoResidencia=tiempoResidencia,
                                nombreEmpresa=nombreEmpresa,dirEmpresa=dirEmpresa,provinciaEmpresa=provinciaEmpresa,
                                cantonEmpresa=cantonEmpresa,parroquiaEmpresa=parroquiaEmpresa,telEmpresa=telEmpresa,
                                tiempoTrabajo=tiempoTrabajo,cargoEmpresa=cargoEmpresa,sueldoEmpresa=sueldoEmpresa,
                                nombresConyuge=nombresConyuge,cedulaConyuge=cedulaConyuge,nivelConyuge=nivelConyuge,
                                correoConyuge=correoConyuge,telConyuge=telConyuge,edadConyuge=edadConyuge,
                                nombreEmpresaConyuge=nombreEmpresaConyuge,dirEmpresaConyuge=dirEmpresaConyuge,
                                provinciaConyuge=provinciaConyuge,cantonConyuge=cantonConyuge,parroquiaConyuge=parroquiaConyuge,
                                telEmpresaConyuge=telEmpresaConyuge,tiempoTraConyuge=tiempoTraConyuge,
                                cargoConyuge=cargoConyuge,sueldoConyuge=sueldoConyuge,nombreNegocio=nombreNegocio,
                                dirNegocio=dirNegocio,provinciaNegocio=provinciaNegocio,cantonNegocio=cantonNegocio,
                                parroquiaNegocio =parroquiaNegocio,telNegocio=telNegocio,tiempoNegocio=tiempoNegocio,
                                cargoNegocio=cargoNegocio,utilidadNegocio=utilidadNegocio,nombreFamilia1=nombreFamilia1,
                                nombreFamilia2=nombreFamilia2,dirFamilia1=dirFamilia1,dirFamilia2=dirFamilia2,
                                parentesco1=parentesco1,parentesco2=parentesco2,telFamilia1=telFamilia1,
                                telFamilia2=telFamilia2,nombreBanco1=nombreBanco1,nombreBanco2=nombreBanco2,
                                ahorros1=ahorros1,ahorros2=ahorros2,corriente1=corriente1,corriente2=corriente2,
                                salPromedio1=salPromedio1,salPromedio2=salPromedio2,refComercial=refComercial,
                                dirComercial=dirComercial,telComercial=telComercial,compra=compra,efectivo=efectivo,
                                deudaBanco =deudaBanco,cuentaCobrar=cuentaCobrar,deudaCobrar=deudaCobrar,
                                mercaderia=mercaderia,proveedores=proveedores,terreno=terreno,casaComercial=casaComercial,
                                casa=casa,prestamista=prestamista,vehiculo=vehiculo,otrasdeudas=otrasdeudas,
                                bienesEnseres=bienesEnseres,otrosActivos=otrosActivos,sueldoMensual=sueldoMensual,
                                gastosAlimentos=gastosAlimentos,utilidadMensual=utilidadMensual,gastosServicios=gastosServicios,
                                salarioConyuge=salarioConyuge,gastoSalud=gastoSalud,agricultorG=agricultorG,
                                pagoPrestamo=pagoPrestamo,otrosIngresos=otrosIngresos,otrosGastos=otrosGastos,

                                
                            )
        messages.success(request, 'Solicitud de Credito enviado con éxito.')
        return redirect ('solicitud') 

    return render (request, 'solicitud/solicitud.html')

#update formulñario de solicitud
def editSolicitud(request, pk):
    credito = Credito.objects.get(id=pk)

    socio = request.POST.get('socioN')
    deudor = request.POST.get('deudor')
    garante = request.POST.get('garante')
    numsocio = request.POST.get('numsocio')
    fecha = request.POST.get('fecha')
    monto = request.POST.get('monto')
    plazo = request.POST.get('plazo')
    destinoP = request.POST.get('destinoP')
    otroDes = request.POST.get('otroDes')
    cuotas = request.POST.get('cuotas')
    fechaPago = request.POST.get('fechaPago')
    montoPagar = request.POST.get('montoPagar')
    nombres = request.POST.get('nombres')
    cedula = request.POST.get('cedula')
    nivelA = request.POST.get('nivelA')
    correo = request.POST.get('correo')
    estadoCivil = request.POST.get('estadoCivil')
    edad = request.POST.get('edad')
    domicilio = request.POST.get('domicilio')
    canton = request.POST.get('canton')
    parroquia = request.POST.get('parroquia')
    comunidad = request.POST.get('comunidad')
    sectorBarrio = request.POST.get('sectorBarrio')
    ciudadela = request.POST.get('ciudadela')
    direccion = request.POST.get('direccion')
    numCasa = request.POST.get('numCasa')
    refDomicilio = request.POST.get('refDomicilio')
    telefono = request.POST.get('telefono')
    celular = request.POST.get('celular')
    cargaFamiliar = request.POST.get('cargaFamiliar')
    separacion = request.POST.get('separacion')
    estadoCasa = request.POST.get('estadoCasa')
    viviendaOtro = request.POST.get('viviendaOtro')
    tiempoResidencia = request.POST.get('tiempoResidencia')
    nombreEmpresa = request.POST.get('nombreEmpresa')
    dirEmpresa = request.POST.get('dirEmpresa')
    provinciaEmpresa = request.POST.get('provinciaEmpresa')
    cantonEmpresa = request.POST.get('cantonEmpresa')
    parroquiaEmpresa = request.POST.get('parroquiaEmpresa')
    telEmpresa = request.POST.get('telEmpresa')
    tiempoTrabajo = request.POST.get('tiempoTrabajo')
    cargoEmpresa = request.POST.get('cargoEmpresa')
    sueldoEmpresa = request.POST.get('sueldoEmpresa')
    nombresConyuge = request.POST.get('nombresConyuge')
    cedulaConyuge  = request.POST.get('cedulaConyuge ')
    nivelConyuge = request.POST.get('nivelConyuge')
    correoConyuge = request.POST.get('correoConyuge')
    telConyuge = request.POST.get('telConyuge')
    edadConyuge = request.POST.get('edadConyuge')
    nombreEmpresaConyuge = request.POST.get('nombreEmpresaConyuge')
    dirEmpresaConyuge = request.POST.get('dirEmpresaConyuge')
    provinciaConyuge = request.POST.get('provinciaConyuge')
    cantonConyuge = request.POST.get('cantonConyuge')
    parroquiaConyuge = request.POST.get('parroquiaConyuge')
    telEmpresaConyuge = request.POST.get('telEmpresaConyuge')
    tiempoTraConyuge = request.POST.get('tiempoTraConyuge')
    cargoConyuge = request.POST.get('cargoConyuge')
    sueldoConyuge = request.POST.get('sueldoConyuge')
    nombreNegocio = request.POST.get('nombreNegocio')
    dirNegocio = request.POST.get('dirNegocio')
    provinciaNegocio = request.POST.get('provinciaNegocio')
    cantonNegocio = request.POST.get('cantonNegocio')
    parroquiaNegocio = request.POST.get('parroquiaNegocio')
    telNegocio = request.POST.get('telNegocio')
    tiempoNegocio = request.POST.get('tiempoNegocio')
    cargoNegocio = request.POST.get('cargoNegocio')
    utilidadNegocio = request.POST.get('utilidadNegocio')
    nombreFamilia1 = request.POST.get('nombreFamilia1')
    nombreFamilia2 = request.POST.get('nombreFamilia2')
    dirFamilia1 = request.POST.get('dirFamilia1')
    dirFamilia2 = request.POST.get('dirFamilia2')
    parentesco1 = request.POST.get('parentesco1')
    parentesco2 = request.POST.get('parentesco2')
    telFamilia1 = request.POST.get('telFamilia1')
    telFamilia2 = request.POST.get('telFamilia2')
    nombreBanco1 = request.POST.get('nombreBanco1')
    nombreBanco2 = request.POST.get('nombreBanco2')
    ahorros1  = request.POST.get('ahorros1')
    ahorros2  = request.POST.get('ahorros2')
    corriente1 = request.POST.get('corriente1')
    corriente2 = request.POST.get('corriente2')
    salPromedio1 = request.POST.get('salPromedio1')
    salPromedio2 = request.POST.get('salPromedio2')
    refComercial = request.POST.get('refComercial')
    dirComercial = request.POST.get('dirComercial')
    telComercial = request.POST.get('telComercial')
    compra  = request.POST.get('compra')
    efectivo = request.POST.get('efectivo')
    deudaBanco = request.POST.get('deudaBanco')
    cuentaCobrar = request.POST.get('cuentaCobrar')
    deudaCobrar = request.POST.get('deudaCobrar')
    mercaderia = request.POST.get('mercaderia')
    proveedores = request.POST.get('proveedores')
    terreno = request.POST.get('terreno')
    casaComercial = request.POST.get('casaComercial')
    casa = request.POST.get('casa')
    prestamista = request.POST.get('prestamista')
    vehiculo = request.POST.get('vehiculo')
    otrasdeudas = request.POST.get('otrasdeudas')
    bienesEnseres = request.POST.get('bienesEnseres')
    otrosActivos = request.POST.get('otrosActivos')
    sueldoMensual = request.POST.get('sueldoMensual')
    gastosAlimentos = request.POST.get('gastosAlimentos')
    utilidadMensual = request.POST.get('utilidadMensual')
    gastosServicios = request.POST.get('gastosServicios')
    salarioConyuge  = request.POST.get('salarioConyuge')
    gastoSalud = request.POST.get('gastoSalud')
    agricultorG  = request.POST.get('agricultorG')
    pagoPrestamo = request.POST.get('pagoPrestamo')
    otrosIngresos = request.POST.get('otrosIngresos')
    otrosGastos = request.POST.get('otrosGastos')

    #suma ingresos 
    

    if request.method == 'POST':

        credito.socio = socio
        credito.deudor = deudor
        credito.garante = garante
        credito.numsocio = numsocio
        credito.fecha = fecha
        credito.monto = monto
        credito.plazo = plazo
        credito.destinoP = destinoP
        credito.otroDes = otroDes
        credito.cuotas = cuotas
        credito.fechaPago = fechaPago
        credito.montoPagar = montoPagar
        credito.nombres = nombres
        credito.cedula = cedula
        credito.nivelA = nivelA
        credito.correo = correo
        credito.estadoCivil = estadoCivil
        credito.edad = edad
        credito.domicilio = domicilio
        credito.canton = canton
        credito.parroquia = parroquia
        credito.comunidad = comunidad
        credito.sectorBarrio = sectorBarrio
        credito.ciudadela = ciudadela
        credito.direccion = direccion
        credito.numCasa = numCasa
        credito.refDomicilio = refDomicilio
        credito.telefono = telefono
        credito.celular = celular
        credito.cargaFamiliar = cargaFamiliar
        credito.separacion = separacion
        credito.estadoCasa = estadoCasa
        credito.viviendaOtro = viviendaOtro
        credito.tiempoResidencia = tiempoResidencia
        credito.nombreEmpresa = nombreEmpresa
        credito.dirEmpresa = dirEmpresa
        credito.provinciaEmpresa = provinciaEmpresa
        credito.cantonEmpresa = cantonEmpresa
        credito.parroquiaEmpresa = parroquiaEmpresa
        credito.telEmpresa = telEmpresa
        credito.tiempoTrabajo = tiempoTrabajo
        credito.cargoEmpresa = cargoEmpresa
        credito.sueldoEmpresa = sueldoEmpresa
        credito.nombresConyuge = nombresConyuge
        credito.cedulaConyuge  = cedulaConyuge
        credito.nivelConyuge = nivelConyuge
        credito.correoConyuge = correoConyuge
        credito.telConyuge = telConyuge
        credito.edadConyuge = edadConyuge
        credito.nombreEmpresaConyuge = nombreEmpresaConyuge
        credito.dirEmpresaConyuge = dirEmpresaConyuge
        credito.provinciaConyuge = provinciaConyuge 
        credito.cantonConyuge = cantonConyuge
        credito.parroquiaConyuge = parroquiaConyuge
        credito.telEmpresaConyuge = telEmpresaConyuge
        credito.tiempoTraConyuge = tiempoTraConyuge
        credito.cargoConyuge = cargoConyuge
        credito.sueldoConyuge = sueldoConyuge
        credito.nombreNegocio = nombreNegocio
        credito.dirNegocio = dirNegocio
        credito.provinciaNegocio = provinciaNegocio
        credito.cantonNegocio = cantonNegocio
        credito.parroquiaNegocio = parroquiaNegocio
        credito.telNegocio = telNegocio
        credito.tiempoNegocio = tiempoNegocio
        credito.cargoNegocio = cargoNegocio
        credito.utilidadNegocio = utilidadNegocio
        credito.nombreFamilia1 = nombreFamilia1
        credito.nombreFamilia2 = nombreFamilia2
        credito.dirFamilia1 = dirFamilia1
        credito.dirFamilia2 = dirFamilia2
        credito.parentesco1 = parentesco1
        credito.parentesco2 = parentesco2
        credito.telFamilia1 = telFamilia1
        credito.telFamilia2 = telFamilia2
        credito.nombreBanco1 = nombreBanco1
        credito.nombreBanco2 = nombreBanco2
        credito.ahorros1  = ahorros1
        credito.ahorros2  = ahorros2
        credito.corriente1 = corriente1
        credito.corriente2 = corriente2
        credito.salPromedio1 = salPromedio1
        credito.salPromedio2 = salPromedio2
        credito.refComercial = refComercial
        credito.dirComercial = dirComercial
        credito.telComercial = telComercial
        credito.compra  = compra
        credito.efectivo = efectivo
        credito.deudaBanco = deudaBanco
        credito.cuentaCobrar = cuentaCobrar
        credito.deudaCobrar = deudaCobrar
        credito.mercaderia = mercaderia
        credito.proveedores = proveedores
        credito.terreno = terreno
        credito.casaComercial = casaComercial
        credito.casa = casa
        credito.prestamista = prestamista
        credito.vehiculo = vehiculo
        credito.otrasdeudas = otrasdeudas
        credito.bienesEnseres = bienesEnseres
        credito.otrosActivos = otrosActivos
        credito.sueldoMensual = sueldoMensual
        credito.gastosAlimentos = gastosAlimentos
        credito.utilidadMensual = utilidadMensual
        credito.gastosServicios = gastosServicios
        credito.salarioConyuge  = salarioConyuge
        credito.gastoSalud = gastoSalud
        credito.agricultorG  = agricultorG
        credito.pagoPrestamo = pagoPrestamo
        credito.otrosIngresos = otrosIngresos
        credito.otrosGastos = otrosGastos
        credito.save()
        return redirect('list-solicitud')
    
    ingresos = float(credito.sueldoMensual)+float(credito.utilidadMensual)+float(credito.salarioConyuge)+float(credito.agricultorG)+float(credito.otrosIngresos)
    gastos = float(credito.gastosAlimentos)+float(credito.gastosServicios)+float(credito.gastoSalud)+float(credito.pagoPrestamo)+float(credito.otrosGastos)
    utilidadNeta = ingresos - gastos
    totalActivos = float(credito.efectivo)+float(credito.cuentaCobrar)+float(credito.mercaderia)+ float(credito.terreno)+float(credito.casa)+float(credito.vehiculo)+float(credito.bienesEnseres) + float(credito.otrosActivos)
    totalPasivos = float(credito.deudaBanco)+float(credito.deudaCobrar)+float(credito.proveedores) + float(credito.casaComercial)+float(credito.prestamista)+float(credito.otrasdeudas)
    patrimonio = totalActivos - totalPasivos
    context = {'credito':credito,'ingresos':ingresos,'gastos':gastos,'utilidadNeta':utilidadNeta,
                'totalActivos':totalActivos,'totalPasivos':totalPasivos,'patrimonio':patrimonio}
    
    return render (request, 'solicitud/update.html',context)


@login_required(login_url='home')
def deleteSolicitud(request, pk):
    post = Credito.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect ('list-solicitud')    
    context = {'item':post}
    return render (request, 'solicitud/delete.html',context)

@login_required(login_url='home')
def listSolicitud(request):
    listpost =  Credito.objects.all()
    
    context = {'listpost':listpost}
    return render (request, 'solicitud/list-solicitud.html',context)





#-----------Envio mail
def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('contacto/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
            'telefono':request.POST['telefono'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['bancpuligui@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'contacto/email_sent.html')




    