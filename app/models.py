from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Tag(models.Model):
	name = models.CharField('Categorias',max_length=200)

	def __str__(self):
		return self.name


class Post(models.Model):
	headline = models.CharField('Nombre',max_length=200)
	sub_headline = models.CharField('Descripccion',max_length=200, null=True, blank=True)
	thumbnail = models.ImageField('Imagen',null=True, blank=True, upload_to="info", default="placeholder.png")
	body = RichTextUploadingField('Contenido',null=True, blank=True)#uso de una libreria
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
    

	#slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.headline


class Info(models.Model):
	nombre = models.CharField(max_length=200, null=True, blank=True)
	imagen = models.ImageField(null=True,blank=True, upload_to="prueba")

	def __str__(self):
		return self.nombre 


#noticias

class Noticia(models.Model):
    name = models.CharField('Autor',max_length=200)
    description = models.CharField('Descripcion',max_length=200,null=True,blank=True)
    body = RichTextUploadingField('Contenido', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField('Activar',default=False)
    novedad = RichTextUploadingField('Novedades', null=True, blank=True)
    Tag = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.name


#Galeria

class Galeria(models.Model):
	name = models.CharField('Nombre',max_length=200)
	description = models.CharField('Descripcion', max_length=200, null=True,blank=True)
	image = models.ImageField('Imagen',null=True, blank=True, upload_to='galeria', default='placeholder.png')
	date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField('Activar',default=False)

	def __str__(self):
		return self.name

class Producto(models.Model):
	name = models.CharField('Servicios',max_length=200)
	description = models.CharField('Descripcion', max_length=200, null=True, blank=True)
	image = models.ImageField('Imagen',null=True,blank=True, upload_to='productos', default='banco.png')
	body = RichTextUploadingField('Contenido', null=True, blank=True)
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField('Activar', default=False)

	def __str__(self):
		return self.name


class Testimonio(models.Model):
	name = models.CharField('Nombres',max_length=200)
	description = models.CharField('Testimonio', max_length=500, null=True, blank=True)
	image = models.ImageField('Imagen',null=True,blank=True, upload_to='testimonios', default='placeholder.png')
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField('Activar', default=False)

	def __str__(self):
		return self.name


	
	

# navproducto

class NavProducto(models.Model):
	name = models.CharField('Nombre', max_length=200)
	image = models.ImageField('Imagen',null=True,blank=True,upload_to='nav-producto',default='placeholder.png')
	date = models.DateField(auto_now_add=True)
	body = RichTextUploadingField('Contenido', null=True,blank=True)
	active = models.BooleanField('Activar',default=False)
	

	def __str__(self):
		return self.name

#nav servisio
class NavServicio(models.Model):
	name = models.CharField('Nombre', max_length=200)
	image = models.ImageField('Imagen',null=True,blank=True,upload_to='nav-servicio',default='placeholder.png')
	date = models.DateField(auto_now_add=True)
	body = RichTextUploadingField('Contenido', null=True,blank=True)
	active = models.BooleanField('Activar',default=False)
	

	def __str__(self):
		return self.name

# nav instirucion
class Institucion(models.Model):
	name = models.CharField('Nombres',max_length=200)
	body = RichTextUploadingField('Contenido', null=True,blank=True)
	image = models.ImageField('Imagen',null=True,blank=True, upload_to='institucion', default='placeholder.png')
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField('Activar', default=False)

	def __str__(self):
		return self.name

class NoticiaInicio(models.Model):
	name = models.CharField('Nombres',max_length=200)
	description = models.CharField('Descripcion', max_length=200, null=True, blank=True)
	body = RichTextUploadingField('Contenido', null=True,blank=True)
	image = models.ImageField('Imagen',null=True,blank=True, upload_to='noticia-inicio', default='placeholder.png')
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField('Activar', default=False)

	def __str__(self):
		return self.name


		
class Credito(models.Model):
	socio = models.CharField(max_length=10, null=True,blank=True)
	deudor = models.BooleanField(null=True, blank=True)
	garante = models.BooleanField(null=True, blank=True)
	numsocio = models.CharField(max_length=10, null=True, blank=True)
	fecha = models.CharField(max_length=40, null=True, blank=True)
	monto = models.CharField(max_length=50, null=True, blank=True)
	plazo = models.CharField(max_length=50, null=True, blank=True)
	destinoP = models.CharField(max_length=50, null=True, blank=True)
	otroDes = models.CharField(max_length=50, null=True, blank=True)
	cuotas = models.CharField(max_length=50, null=True, blank=True)
	fechaPago = models.CharField(max_length=40, null=True, blank=True)
	montoPagar = models.CharField(max_length=50, null=True, blank=True)
	nombres = models.CharField(max_length=120, null=True, blank=True)
	cedula = models.CharField(max_length=15, null=True, blank=True)
	nivelA = models.CharField(max_length=50, null=True, blank=True)
	correo = models.CharField(max_length=50, null=True, blank=True)
	estadoCivil = models.CharField(max_length=50, null=True, blank=True)
	edad = models.CharField(max_length=40, null=True, blank=True)
	domicilio = models.CharField(max_length=100, null=True, blank=True)
	canton = models.CharField(max_length=100, null=True, blank=True)
	parroquia = models.CharField(max_length=100, null=True, blank=True)
	comunidad = models.CharField(max_length=100, null=True, blank=True)
	sectorBarrio = models.CharField(max_length=100, null=True, blank=True)
	ciudadela = models.CharField(max_length=40, null=True, blank=True)
	direccion = models.CharField(max_length=120, null=True, blank=True)
	numCasa = models.CharField(max_length=25, null=True, blank=True)
	refDomicilio = models.CharField(max_length=100, null=True, blank=True)
	telefono = models.CharField(max_length=30, null=True, blank=True)
	celular = models.CharField(max_length=15, null=True, blank=True)
	cargaFamiliar = models.CharField(max_length=10, null=True, blank=True)
	separacion = models.CharField(max_length=20, null=True, blank=True)
	estadoCasa = models.CharField(max_length=20, null=True, blank=True)
	viviendaOtro = models.CharField(max_length=50, null=True, blank=True)
	tiempoResidencia = models.CharField(max_length=50, null=True, blank=True)
	nombreEmpresa = models.CharField(max_length=100, null=True, blank=True)
	dirEmpresa = models.CharField(max_length=100, null=True, blank=True)
	provinciaEmpresa = models.CharField(max_length=100, null=True, blank=True)
	cantonEmpresa = models.CharField(max_length=100, null=True, blank=True)
	parroquiaEmpresa = models.CharField(max_length=100, null=True, blank=True)
	telEmpresa = models.CharField(max_length=20, null=True, blank=True)
	tiempoTrabajo = models.CharField(max_length=50, null=True, blank=True)
	cargoEmpresa = models.CharField(max_length=50, null=True, blank=True)
	sueldoEmpresa = models.CharField(max_length=50, null=True, blank=True)
	nombresConyuge = models.CharField(max_length=50, null=True, blank=True)
	cedulaConyuge = models.CharField(max_length=15, null=True, blank=True)
	nivelConyuge = models.CharField(max_length=50, null=True, blank=True)
	correoConyuge = models.CharField(max_length=50, null=True, blank=True)
	telConyuge = models.CharField(max_length=50, null=True, blank=True)
	edadConyuge = models.CharField(max_length=50, null=True, blank=True)
	nombreEmpresaConyuge = models.CharField(max_length=50, null=True, blank=True)
	dirEmpresaConyuge = models.CharField(max_length=100, null=True, blank=True)
	provinciaConyuge = models.CharField(max_length=50, null=True, blank=True)
	cantonConyuge = models.CharField(max_length=100, null=True, blank=True)
	parroquiaConyuge = models.CharField(max_length=100, null=True, blank=True)
	telEmpresaConyuge = models.CharField(max_length=100, null=True, blank=True)
	tiempoTraConyuge = models.CharField(max_length=100, null=True, blank=True)
	cargoConyuge = models.CharField(max_length=100, null=True, blank=True)
	sueldoConyuge = models.CharField(max_length=100, null=True, blank=True)
	nombreNegocio = models.CharField(max_length=100, null=True, blank=True)
	dirNegocio = models.CharField(max_length=100, null=True, blank=True)
	provinciaNegocio = models.CharField(max_length=100, null=True, blank=True)
	cantonNegocio = models.CharField(max_length=100, null=True, blank=True)
	parroquiaNegocio = models.CharField(max_length=100, null=True, blank=True)
	telNegocio = models.CharField(max_length=50, null=True, blank=True)
	tiempoNegocio = models.CharField(max_length=50, null=True, blank=True)
	cargoNegocio = models.CharField(max_length=50, null=True, blank=True)
	utilidadNegocio = models.CharField(max_length=50, null=True, blank=True)
	nombreFamilia1 = models.CharField(max_length=100, null=True, blank=True)
	nombreFamilia2 = models.CharField(max_length=100, null=True, blank=True)
	dirFamilia1 = models.CharField(max_length=100, null=True, blank=True)
	dirFamilia2 = models.CharField(max_length=100, null=True, blank=True)
	parentesco1 = models.CharField(max_length=100, null=True, blank=True)
	parentesco2 = models.CharField(max_length=100, null=True, blank=True)
	telFamilia1 = models.CharField(max_length=100, null=True, blank=True)
	telFamilia2 = models.CharField(max_length=100, null=True, blank=True)
	nombreBanco1 = models.CharField(max_length=100, null=True, blank=True)
	nombreBanco2 = models.CharField(max_length=100, null=True, blank=True)
	ahorros1 = models.CharField(max_length=50, null=True, blank=True)
	ahorros2 = models.CharField(max_length=50, null=True, blank=True)
	corriente1 = models.CharField(max_length=50, null=True, blank=True)
	corriente2 = models.CharField(max_length=50, null=True, blank=True)
	salPromedio1 = models.CharField(max_length=50, null=True, blank=True)
	salPromedio2 = models.CharField(max_length=50, null=True, blank=True)
	refComercial = models.CharField(max_length=100, null=True, blank=True)
	dirComercial = models.CharField(max_length=100, null=True, blank=True)
	telComercial = models.CharField(max_length=100, null=True, blank=True)
	compra = models.CharField(max_length=100, null=True, blank=True)
	efectivo = models.CharField(max_length=50, null=True, blank=True)
	deudaBanco = models.CharField(max_length=50, null=True, blank=True)
	cuentaCobrar = models.CharField(max_length=50, null=True, blank=True)
	deudaCobrar = models.CharField(max_length=50, null=True, blank=True)
	mercaderia = models.CharField(max_length=50, null=True, blank=True)
	proveedores = models.CharField(max_length=50, null=True, blank=True)
	terreno = models.CharField(max_length=50, null=True, blank=True)
	casaComercial = models.CharField(max_length=50, null=True, blank=True)
	casa = models.CharField(max_length=50, null=True, blank=True)
	prestamista = models.CharField(max_length=50, null=True, blank=True)
	vehiculo = models.CharField(max_length=50, null=True, blank=True)
	otrasdeudas = models.CharField(max_length=50, null=True, blank=True)
	bienesEnseres = models.CharField(max_length=50, null=True, blank=True)
	otrosActivos = models.CharField(max_length=50, null=True, blank=True)
	sueldoMensual = models.CharField(max_length=50, null=True, blank=True)
	gastosAlimentos = models.CharField(max_length=50, null=True, blank=True)
	utilidadMensual = models.CharField(max_length=50, null=True, blank=True)
	gastosServicios = models.CharField(max_length=50, null=True, blank=True)
	salarioConyuge = models.CharField(max_length=50, null=True, blank=True)
	gastoSalud = models.CharField(max_length=50, null=True, blank=True)
	agricultorG = models.CharField(max_length=50, null=True, blank=True)
	pagoPrestamo = models.CharField(max_length=50, null=True, blank=True)
	otrosIngresos = models.CharField(max_length=50, null=True, blank=True)
	otrosGastos = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.nombres

		








	







	








































	

