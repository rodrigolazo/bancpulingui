from django.urls import path
from . import views
urlpatterns =[


    path ('',views.index, name='home'),
   
    path ('quienes-somos/',views.quienesSomos, name='quienes-somos'),
    
    
    path ('contactos/',views.contactos, name='contactos'),
    path ('noticias/',views.noticias, name='noticias'),

    #Cruds baner
    path ('insertar-baner/',views.insertBaner ,name='insertar-baner'),
    path ('editar-baner/<str:pk>',views.editarBaner ,name='editar-baner'),
    path ('eliminar-baner/<str:pk>',views.eliminarBaner ,name='eliminar-baner'),
    path ('post-baner/<str:pk>',views.postBaner ,name='post-baner'),
    path ('listar-baner/',views.listarBaner ,name='listar-baner'),

    #crud noticias
    path ('insertar-noticia/',views.insertNoticia ,name='insertar-noticia'),
    path ('editar-noticia/<str:pk>',views.editarNoticia ,name='editar-noticia'),
    path ('eliminar-noticia/<str:pk>',views.eliminarNoticia ,name='eliminar-noticia'),
    path ('post-noticia/<str:pk>',views.postNoticia ,name='post-noticia'),
    path ('listar-noticias/',views.listarNoticia ,name='listar-noticias'),

    #------------------------- no estan ----------------------------------
    #crud galeria
    path ('galeria/',views.galeria, name='galeria'),
    path ('insertar-galeria/',views.insertGaleria ,name='insertar-galeria'),
    path ('editar-galeria/<str:pk>',views.editarGaleria ,name='editar-galeria'),
    path ('eliminar-galeria/<str:pk>',views.eliminarGaleria ,name='eliminar-galeria'),
    path ('listar-galeria/',views.listarGaleria ,name='listar-galeria'),

    #crud productos
    path ('productos/',views.servicios, name='servicios'),
    path ('insertar-sercivio/',views.insertServicio ,name='insertar-sercivio'),
    path ('editar-sercivio/<str:pk>',views.editarServicio ,name='editar-sercivio'),
    path ('eliminar-sercivio/<str:pk>',views.eliminarServicio ,name='eliminar-sercivio'),
    path ('listar-sercivio/',views.listarSercivio ,name='listar-sercivio'),
    path ('post-sercivio/<str:pk>',views.postServicio ,name='post-sercivio'),

    #crud testimonios
    path ('insertar-testimonio/',views.inserTestimonio ,name='insertar-testimonio'),
    path ('editar-testimonio/<str:pk>',views.editarTestimonio ,name='editar-testimonio'),
    path ('eliminar-testimonio/<str:pk>',views.eliminarTestimonio ,name='eliminar-testimonio'),
    path ('listar-testimonio/',views.listarTestimonio ,name='listar-testimonio'),


    #crud nav producto
    path ('produc/<str:pk>',views.postNavProducto ,name='nav-producto'),
    path ('insertar-producto/',views.inserNavProducto ,name='navp-insertar'),
    path ('editar-producto/<str:pk>',views.editarNavProducto ,name='navp-editar'),
    path ('eliminar-producto/<str:pk>',views.eliminarNavProducto,name='navp-eliminar'),
    path ('listar-producto/',views.listarNavProducto ,name='navp-listar'),

    #crud nav institucion 
    path ('institucion/<str:pk>',views.postInstitucion ,name='post-institucion'),
    path ('insertar-institucion/',views.inserInstitucion ,name='institucion-insertar'),
    path ('editar-institucion/<str:pk>',views.editarInstitucion ,name='institucion-editar'),
    path ('eliminar-institucion/<str:pk>',views.eliminarInstitucion,name='institucion-eliminar'),
    path ('listar-institucion/',views.listarInstitucion ,name='institucion-listar'),

    #crud Noticias del inicio
    path ('informacion/<str:pk>',views.postInformacion ,name='post-informacion'),
    path ('insertar-informacion/',views.inserInformacion ,name='informacion-insertar'),
    path ('editar-informacion/<str:pk>',views.editarInformacion ,name='informacion-editar'),
    path ('eliminar-informacion/<str:pk>',views.eliminarInformacion,name='informacion-eliminar'),
    path ('listar-informacion/',views.listarInformacion ,name='informacion-listar'),

    #crud nav servicios
    path ('servicios/<str:pk>',views.postServicios ,name='servicios-post'),
    path ('insertar-servicios/',views.inserServicios ,name='servicios-insertar'),
    path ('editar-servicios/<str:pk>',views.editarServicios ,name='servicios-editar'),
    path ('eliminar-servicios/<str:pk>',views.eliminarServicios,name='servicios-eliminar'),
    path ('listar-servicios/',views.listarServicios ,name='servicios-listar'),


    #---------------------esta parte medio medio
    #Insertar solicitud
    path ('solicitud-formulario/',views.applicationForm ,name='solicitud'),
    path ('envio/',views.createRequest ,name='envio-solicitud'),
    path ('editar-solicitud/<str:pk>/',views.editSolicitud ,name='edit-solicitud'),
    path ('eliminar-solicitud/<str:pk>',views.deleteSolicitud ,name='eliminar-solicitud'),
    path ('list-solicitud/',views.listSolicitud ,name='list-solicitud'),

    #path ('post-solicitud/<str:pk>',views.postSolicitud ,name='post-solicitud'),
    

    #----contacto por email
    path('send_email/', views.sendEmail, name="send_email"),


    #pdf 
     path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
     path ('pdf/',views.pdfs ,name='pdf'),


]