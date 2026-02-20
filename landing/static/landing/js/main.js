



document.addEventListener('DOMContentLoaded', () => {
    const counters = document.querySelectorAll('.counter');
    
    counters.forEach(el => {
        const base = parseFloat(el.getAttribute('data-base'));
        el.innerText = base;

        // ACELERADO: Actualización cada 1.2 segundos (antes 2.5s)
        setInterval(() => {
            // DINAMISMO: Subimos la variación al 12% (antes 2%)
            const variation = base * 0.12; 
            const offset = (Math.random() * variation * 2) - variation;
            const target = base + offset;
            
            const startValue = parseFloat(el.innerText) || base;
            
            // SNAPPY: Animación más rápida de 800ms (antes 1500ms)
            animateStep(el, startValue, target, 800);
        }, 1200); 
    });

    function animateStep(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            
            // Easing: Usamos una curva para que el movimiento sea más "elástico"
            const easeOutQuad = t => t * (2 - t);
            const current = easeOutQuad(progress) * (end - start) + start;
            
            const baseAttr = parseFloat(obj.getAttribute('data-base'));

            // Formateo dinámico
            obj.innerText = baseAttr < 20 ? current.toFixed(1) : Math.floor(current);
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }


//SECCION DISEÑO
    
document.querySelectorAll('.reveal-slide-up').forEach((el, index) => {
    // Añadimos un pequeño retraso manual basado en el índice para el efecto "stagger"
    el.style.transitionDelay = `${index * 0.1}s`;
    revealObserver.observe(el);
});



    
    
});
    // 2. OBSERVADORES DE APARICIÓN (Intersection Observer)
    const observerOptions = { threshold: 0.1 };

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    // Aplicamos a las secciones con .reveal y al texto parallax
    document.querySelectorAll('.reveal, .reveal-text').forEach(el => {
        revealObserver.observe(el);
    });

    // Inicializar iconos de Lucide al cargar
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }


/**
 * GESTIÓN DE AUDIO SELECTIVO PARA REELS
 */
function toggleSound(videoId, btn) {
    const targetVideo = document.getElementById(videoId);
    const allVideos = document.querySelectorAll('.reel-video');
    const icon = btn.querySelector('.sound-icon');

    if (!targetVideo.muted) {
        targetVideo.muted = true;
        btn.classList.remove('bg-brand-red');
        icon.setAttribute('data-lucide', 'volume-x');
    } else {
        // Silenciamos el resto para que no se mezclen los audios
        allVideos.forEach(v => v.muted = true);
        
        targetVideo.muted = false;
        btn.classList.add('bg-brand-red');
        icon.setAttribute('data-lucide', 'volume-2');
    }
    
    // Forzamos a Lucide a redibujar el icono cambiado
    lucide.createIcons();
}

/**
 * LÓGICA DE GALERÍA (LIGHTBOX)
 */
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');

function openLightbox(src) {
    if (lightbox && lightboxImg) {
        document.body.style.overflow = 'hidden';
        lightboxImg.src = src;
        lightbox.classList.remove('hidden');
        lightbox.classList.add('flex');
    }
}

function closeLightbox() {
    if (lightbox) {
        document.body.style.overflow = 'auto';
        lightbox.classList.add('hidden');
        lightbox.classList.remove('flex');
    }
}

// Cerrar con Escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
});


// EL SOCIO QUE SI ESCUCHA:





///FORM----------------
document.addEventListener('DOMContentLoaded', () => {
    // ... tu código existente ...

    /**
     * GESTIÓN DE INPUTS PREMIUM
     * Mantiene la etiqueta arriba si hay contenido
     */
    const formInputs = document.querySelectorAll('.input-group input, .input-group textarea');

    function checkInputContent(input) {
        if (input.value.trim() !== '') {
            input.classList.add('has-content');
        } else {
            input.classList.remove('has-content');
        }
    }

    formInputs.forEach(input => {
        // Verificar al cargar por si hay autocompletado
        checkInputContent(input);

        // Verificar cuando el usuario escribe o sale del input
        input.addEventListener('blur', () => checkInputContent(input));
        input.addEventListener('input', () => checkInputContent(input));
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // ... (tu código anterior de los inputs) ...

    /**
     * ANIMACIÓN DE CARGA DEL FORMULARIO
     */
    const form = document.getElementById('premium-form'); // Asegúrate que tu <form> tenga este ID
    const btnSubmit = document.getElementById('btn-submit');
    const btnContent = document.getElementById('btn-content');
    const btnLoading = document.getElementById('btn-loading');
    const btnBg = document.getElementById('btn-bg');

    if (form && btnSubmit) {
        form.addEventListener('submit', function(e) {
            // No prevenimos el default (e.preventDefault()) porque queremos que el formulario se envíe.
            // Solo activamos la animación visualmente.

            // 1. Desactivar el botón para evitar doble envío
            btnSubmit.disabled = true;
            btnSubmit.classList.add('cursor-not-allowed');
            
            // 2. Ocultar contenido normal con efecto fade-out
            btnContent.style.opacity = '0';
            btnContent.style.transform = 'translateY(-10px)';
            
            // 3. Mostrar spinner de carga con efecto fade-in
            btnLoading.classList.remove('opacity-0', 'pointer-events-none');
            
            // 4. Forzar el fondo rojo para que se vea el spinner blanco
            btnBg.style.transform = 'translateY(0)';

            //5 validacion
            btnContent.querySelector('span').innerText = 'Validando Proyecto...';
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
  // Capturamos los elementos del DOM
  const radios = document.querySelectorAll('input[name="tipo_enlace"]');
  const prefijo = document.getElementById('prefijo_visual');
  const input = document.getElementById('campo_usuario');

  // Función que se ejecuta al cambiar la selección
  function actualizarCampo(evento) {
    const tipoSeleccionado = evento.target.value;

    if (tipoSeleccionado === 'instagram') {
      // Mostrar formato Instagram
      prefijo.style.display = 'flex';
      prefijo.textContent = '@';
      input.placeholder = 'usuario_restaurante';
    } else if (tipoSeleccionado === 'link') {
      // Mostrar formato Enlace Web
      prefijo.style.display = 'none';
      input.placeholder = 'https://www.ejemplo.com/menu';
    }
    
    // Limpiamos el texto que el usuario haya escrito previamente por error
    input.value = ''; 
  }

  // Le asignamos el "escuchador" a cada radio button
  radios.forEach(function(radio) {
    radio.addEventListener('change', actualizarCampo);
  });
});