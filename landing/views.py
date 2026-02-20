# Create your views here.
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'landing/index.html')



# landing/views.py
def contacto_view(request):
    if request.method == 'POST':
        # ... toda la lógica premium que armamos antes ...
        return redirect('success') # Redirige al nombre de la URL de éxito
    return redirect('home')

def success_view(request):
    return render(request, 'landing/success.html')
    

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import LeadContacto

def contacto_view(request):
    if request.method == 'POST':
        # 1. Recopilar datos básicos
        nombre = request.POST.get('nombre')
        email_cliente = request.POST.get('email')
        local = request.POST.get('local')
        mensaje = request.POST.get('mensaje')
        redes_raw = request.POST.get('redes', '').strip() # Captura el 'name="redes"' del HTML

        redes_url = ""
        es_instagram = False

        # 2. Lógica de validación de enlace
        if redes_raw:
            if redes_raw.startswith('@'):
                username = redes_raw.replace('@', '')
                redes_url = f"https://www.instagram.com/{username}/"
                es_instagram = True
            elif redes_raw.startswith('http'):
                redes_url = redes_raw
            else:
                redes_url = f"https://www.instagram.com/{redes_raw}/"
                es_instagram = True

        # 3. Crear el Lead UNICA VEZ (Seguridad UX)
        lead = LeadContacto.objects.create(
            nombre=nombre,
            email=email_cliente,
            local=local,
            redes_sociales=redes_url if redes_url else redes_raw,
            mensaje=mensaje
        )

        # 4. Definir Contexto Unificado
        # Importante: los nombres aquí deben ser IGUALES a los del HTML del correo
        context = {
            'lead': lead, 
            'nombre': nombre,
            'redes_url': redes_url, # Esta es la que busca tu template
            'es_instagram': es_instagram 
        }

        # 5. Renderizar y Enviar Correos
        html_agencia = render_to_string('landing/emails/admin_notification.html', context)
        html_cliente = render_to_string('landing/emails/client_welcome.html', context)

        # --- ENVÍO A LA AGENCIA ---
        email_admin = EmailMultiAlternatives(
            subject=f"🚀 Nuevo Proyecto: {local}",
            body=f"Nuevo lead de {nombre}",
            to=['tomasriveroscc@gmail.com']
        )
        email_admin.attach_alternative(html_agencia, "text/html")
        email_admin.send(fail_silently=False)

        # --- ENVÍO AL CLIENTE ---
        email_confirmacion = EmailMultiAlternatives(
            subject="Recibimos tu propuesta | White Dog Studios",
            body=f"Hola {nombre}, estamos analizando tu local.",
            to=[email_cliente]
        )
        email_confirmacion.attach_alternative(html_cliente, "text/html")
        email_confirmacion.send(fail_silently=False)

        return redirect('success')
    return redirect('home')
    if request.method == 'POST':
        # 1. Recopilar datos
        nombre = request.POST.get('nombre')
        email_cliente = request.POST.get('email')
        local = request.POST.get('local')
        redes = request.POST.get('redes')
        mensaje = request.POST.get('mensaje')


        # 1. PRIMERO DEFINIMOS LA VARIABLE
        redes_raw = request.POST.get('redes', '').strip()
        redes_url = ""
        es_instagram = False

        # Lógica de validación de enlace
        if redes_raw:
            if redes_raw.startswith('@'):
                # Caso: @usuario -> https://instagram.com/usuario
                username = redes_raw.replace('@', '')
                redes_url = f"https://www.instagram.com/{username}/"
                is_instagram = True # Flag para el correo personalizado



            elif redes_raw.startswith('http'):
                # Caso: Ya es un link (web o ig completo)
                redes_url = redes_raw
            else:
                # Caso: usuario (sin @) -> asumimos Instagram por defecto
                redes_url = f"https://www.instagram.com/{redes_raw}/"

        
        # Crear el Lead en la base de datos
        lead = LeadContacto.objects.create(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            local=request.POST.get('local'),
            redes_sociales=redes_url if redes_url else redes_raw,
            mensaje=request.POST.get('mensaje')
        )

        # Pasamos el link procesado al contexto del correo
        context = {
            'lead': lead, 
            'nombre': lead.nombre,
            'redes_display': redes_url if redes_url else "No proporcionado",
            'es_instagram': es_instagram # Para la respuesta especial
        }

        # Renderizar ambos correos (Asegúrate de pasar 'context' a ambos)
        html_agencia = render_to_string('landing/emails/admin_notification.html', context)
        html_cliente = render_to_string('landing/emails/client_welcome.html', context)

        # 2. Guardar en Base de Datos (Seguridad UX)
        nuevo_lead = LeadContacto.objects.create(
            nombre=nombre, email=email_cliente, local=local, redes_sociales=redes, mensaje=mensaje
        )

        # --- CORREO 1: PARA LA AGENCIA (DATOS TÉCNICOS) ---
        html_agencia = render_to_string('landing/emails/admin_notification.html', {'lead': nuevo_lead})
        email_admin = EmailMultiAlternatives(
            subject=f"🚀 Nuevo Proyecto: {local}",
            body=f"Nuevo lead de {nombre}",
            to=['tomasriveroscc@gmail.com'] # Tu correo de trabajo
        )
        email_admin.attach_alternative(html_agencia, "text/html")
        email_admin.send(fail_silently=False)

        # --- CORREO 2: PARA EL CLIENTE (AUTO-REPLY PREMIUM) ---
        html_cliente = render_to_string('landing/emails/client_welcome.html', {'nombre': nombre})
        email_confirmacion = EmailMultiAlternatives(
            subject="Recibimos tu propuesta | White Dog Studios",
            body=f"Hola {nombre}, estamos analizando tu local.",
            to=[email_cliente] # Correo que el cliente puso en el form
        )
        email_confirmacion.attach_alternative(html_cliente, "text/html")
        email_confirmacion.send(fail_silently=False)

        return redirect('success')
    return redirect('home')