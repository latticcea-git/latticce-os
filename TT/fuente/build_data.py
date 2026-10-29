import json, os
OUT = os.path.dirname(os.path.abspath(__file__))
B = "https://latticce.com/book/"

def L(label, url, publico=True):
    return {"label": label, "url": url, "publico": publico}

def P(**k):
    base = dict(id="", nombre="", tipo="", estado="", nodo="", nodos="", etapa="", inicio=None, inicio_q="falta",
                def_n=None, pend_n=None, definido="", pendiente="", pruebas=[], presencia="", links=[],
                c_publico=None, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=None,
                limite="", siguiente="", fuente="")
    base.update(k)
    return base

proyectos = [
  P(id="frutisa", nombre="Frutisa", tipo="Cliente", estado="Cliente activo", nodo="Design", nodos="Design, Agency",
    etapa="q2", inicio="2026-06-01", inicio_q="aprox", def_n=4, pend_n=5,
    definido="Brand Pet 3D oficial; paleta; sistema visual; lineamientos del personaje",
    pendiente="Packaging; sitio web; campañas; material POP; animaciones",
    pruebas=["Caso público en el Book: Identidad + Brand Pet", "PDF Casos de branding (interno, 20 láminas)", "Piloto documentado de CHACHA APP (en curso)"],
    presencia="Caso publicado en latticce.com/book", links=[L("Caso en el Book", B+"frutisa-branding-sitio-web/")],
    c_publico=True, c_contenido=None, c_permiso=None, c_comercial=True, c_cruce=True,
    limite="Web y extensiones pendientes; no presentarlo como sitio terminado.",
    siguiente="Terminar el caso piloto de CHACHA APP (objetivo actual del proyecto interno).",
    fuente="KOBOS · 06 Clientes/Frutisa · 01 Estrategia/Trayectoria"),
  P(id="shakti", nombre="Shakti Yoga Estudio", tipo="Cliente", estado="Cliente activo", nodo="Agency", nodos="Agency, Design",
    etapa="q2", inicio="2026-05-01", inicio_q="aprox", def_n=9, pend_n=6,
    definido="Branding; lineamientos visuales; moodboard; home; arquitectura del sitio; flujo de navegación; UX principal; wireframes; brief maestro",
    pendiente="Desarrollo completo; implementación; optimización móvil; SEO; automatizaciones; CMS",
    pruebas=["Caso público en el Book: identidad visual", "Brand kit SYE", "Arquitectura UX/UI aprobada", "Perfil y portada de Facebook preparados (sin publicar)", "1 campaña de Meta Ads con gasto en 2026"],
    presencia="Caso publicado en latticce.com/book", links=[L("Caso en el Book", B+"shakti-yoga-estudio/")],
    c_publico=True, c_contenido=None, c_permiso=None, c_comercial=True, c_cruce=True,
    limite="No marcar implementación terminada.",
    siguiente="Finalizar el desarrollo y documentarlo como caso de éxito (prioridad 5/5).",
    fuente="KOBOS · 06 Clientes/Shakti Yoga Estudio · Clientes actuales"),
  P(id="deshii", nombre="DESHii", tipo="Cliente", estado="Cliente activo", nodo="Design", nodos="Design, Agency, Studio",
    etapa="q3", inicio="2026-08-07", inicio_q="aprox", def_n=7, pend_n=4,
    definido="Logo; mood visual; menús; tarjetas bancarias; sistema de pedidos; material para WhatsApp; promocionales",
    pendiente="Packaging; sitio web; fotografía profesional; material para puntos de venta",
    pruebas=["Sistema de pedidos realizado", "Piezas de branding y material comercial"],
    presencia="Sin página pública", links=[],
    c_publico=False, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=True,
    limite="Branding en proceso; confirmar permiso antes de mostrarlo.",
    siguiente="Elegir el pendiente de mayor impacto comercial (foto o web: venta cruzada con Studio y Agency).",
    fuente="KOBOS · 06 Clientes/DESHii"),
  P(id="soma", nombre="SOMA", tipo="Cliente", estado="Cliente activo", nodo="Design", nodos="Design",
    etapa="q3", inicio="2026-08-07", inicio_q="aprox", def_n=4, pend_n=3,
    definido="Moodboard; variantes de logotipo; paleta; aplicaciones",
    pendiente="Manual de marca; redes sociales; sitio web",
    pruebas=["Variantes de logotipo y aplicaciones"], presencia="Sin página pública", links=[],
    c_publico=False, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=True,
    limite="Identidad en desarrollo.", siguiente="Cerrar manual de marca y abrir redes o sitio (Agency).",
    fuente="KOBOS · 06 Clientes/SOMA"),
  P(id="okame", nombre="OKAME", tipo="Cliente", estado="Ejecutado", nodo="Design", nodos="Design",
    etapa="q3", inicio=None, inicio_q="falta", def_n=None, pend_n=None,
    definido="Identidad visual (Nails + Beauty Studio)", pendiente="",
    pruebas=["Caso público en el Book: identidad visual", "PDF Casos de branding (interno)"],
    presencia="Caso publicado en latticce.com/book; sin expediente en KOBOS", links=[L("Caso en el Book", B+"okame/")],
    c_publico=True, c_contenido=None, c_permiso=None, c_comercial=True, c_cruce=None,
    limite="KOBOS no tiene expediente ni permiso registrado.", siguiente="Crear expediente en KOBOS y confirmar permiso de uso público.",
    fuente="Book UROBOROS · memoria del proyecto"),
  P(id="jeremy", nombre="Inglés con Jeremy", tipo="Cliente", estado="Ejecutado", nodo="Agency", nodos="Agency",
    etapa="q2", inicio=None, inicio_q="falta", def_n=None, pend_n=None,
    definido="Arquitectura educativa y multimedia; ecosistema digital", pendiente="",
    pruebas=["Caso público en el Book: ecosistema digital"],
    presencia="Caso publicado en latticce.com/book", links=[L("Caso en el Book", B+"ingles-con-jeremy-sitio-web/")],
    c_publico=True, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="KOBOS pide confirmar estado y permiso antes de uso público, y el caso ya está publicado.",
    siguiente="Confirmar permiso o retirarlo del Book.", fuente="KOBOS · Trayectoria · Book UROBOROS"),
  P(id="cvp", nombre="CVP", tipo="Cliente", estado="Ejecutado", nodo="Design", nodos="Design, Agency",
    etapa="q2", inicio=None, inicio_q="falta", definido="Identidad; medio local; contenido",
    pruebas=[], presencia="Sin página pública", links=[],
    c_publico=False, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="Confirmar estado y permiso antes de uso público.", siguiente="Abrir expediente con estado, piezas y permiso.",
    fuente="KOBOS · Trayectoria"),
  P(id="floripondios", nombre="Floripondios", tipo="Producción propia", estado="Ejecutado", nodo="Studio", nodos="Studio, Sound, Films",
    etapa="q2", inicio="2026-04-15", inicio_q="aprox",
    definido="Narrativa y producción; sonido directo; sincronización; edición; postproducción con especialista externo",
    pruebas=["Postproducción documentada", "Antecedente técnico de Sound (captura, sincronización y mezcla)"],
    presencia="Sin página pública", links=[],
    c_publico=False, c_contenido=None, c_permiso=None, c_comercial=False, c_cruce=None,
    limite="No declarar distribución, estreno o resultado comercial sin evidencia.",
    siguiente="Decidir si se vuelve pieza de Films (página en latticce.com/films) o caso de Sound.",
    fuente="KOBOS · Trayectoria · LATTICCE Sound"),
  P(id="conciertos", nombre="Conciertos (Studio Music)", tipo="Experiencia", estado="Ejecutado", nodo="Studio", nodos="Studio",
    etapa="q2", inicio="2026-05-01", inicio_q="aprox",
    definido="Cobertura, selección, edición y publicación de conciertos",
    pruebas=["9 coberturas publicadas en el Book", "Artículo del blog: cubrir un concierto sin borrar al público", "Studio: 35,578 visualizaciones en 28 días (oct)"],
    presencia="9 casos públicos en el Book", links=[L("Enjambre", B+"enjambre-estadio-gnp/"), L("José Madero", B+"pepe-madero-pulso-gnp/"), L("Sofía Stainer", B+"sofia-stainer-foro-la-paz/"), L("GRTSCH", B+"grtsch-xxi-monomita/"), L("Book completo", B)],
    c_publico=True, c_contenido=True, c_permiso=None, c_comercial=True, c_cruce=None,
    limite="No contabilizar como facturación LATTICCE sin expediente.",
    siguiente="Convertir la red musical en prospectos de videoclip (tandas de 3).", fuente="KOBOS · Trayectoria · Book UROBOROS"),
  P(id="videoclips", nombre="Videoclips (Essential / Classic)", tipo="Producto", estado="Producto construido", nodo="Studio", nodos="Studio, Sound, Films",
    etapa="q3", inicio="2026-08-01", inicio_q="aprox",
    definido="Clips, Live Sessions, retratos, portadas, verticales y BTS",
    pruebas=["3 videoclips en el Book (ALEJATE, PECULIAR, HECHO PARA TI)", "Mismas piezas en latticce.com/films/cinema"],
    presencia="3 casos públicos + Films", links=[L("ALEJATE", B+"alejate-los-chicklets/"), L("PECULIAR", B+"peculiar-karell/"), L("HECHO PARA TI", B+"hecho-para-ti-jimena-hermida/"), L("Films · cinema", "https://latticce.com/films/cinema/")],
    c_publico=True, c_contenido=True, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="Producto propuesto: no afirmar ventas recurrentes.", siguiente="Bloque y CTA de videoclip en latticce.com/studio (auditoría 24-oct).",
    fuente="KOBOS · Ventas Studio · Auditoría web Studio"),
  P(id="retrato", nombre="Retrato Express y sesiones", tipo="Producto", estado="Producto construido", nodo="Studio", nodos="Studio",
    etapa="q3", inicio="2026-08-01", inicio_q="aprox",
    definido="Retrato en exteriores y locaciones CDMX",
    pruebas=["5 sesiones en el Book"], presencia="5 sesiones públicas",
    links=[L("Pablito Navajas", B+"pablito-navajas-retrato-exterior/"), L("Susana Cuervo", B+"susana-cuervo-cafe/"), L("Folclore mexicano", B+"folclore-mexicano/")],
    c_publico=True, c_contenido=True, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="Precio por formalizar.", siguiente="Bloque y CTA de Retrato Express en el sitio.", fuente="KOBOS · Ventas Studio · Book"),
  P(id="bodas", nombre="Bodas y eventos (Time)", tipo="Producto", estado="Producto construido", nodo="Time", nodos="Time, Studio",
    etapa="q2", inicio="2026-04-01", inicio_q="aprox",
    definido="Paquetes para bodas, XV y eventos; sistema de recomendados",
    pruebas=["6 memorias en el Book de Time", "7 artículos del blog de Time"], presencia="6 casos públicos",
    links=[L("Una memoria de boda", B+"boda-memoria-completa/"), L("Sesión de novios", B+"sesion-de-novios/"), L("latticce.com/time", "https://latticce.com/time/")],
    c_publico=True, c_contenido=True, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="El catálogo no prueba ventas por modalidad.", siguiente="Book y PDF para parejas y recomendadores (faltan según Ventas Time).",
    fuente="KOBOS · LATTICCE Time · Ventas Time"),
  P(id="abyali", nombre="Aby y Ali 360", tipo="Experiencia", estado="Ejecutado", nodo="Studio", nodos="Studio, Time",
    etapa="q2", inicio="2026-05-15", inicio_q="aprox",
    definido="Captura 360; edición; preparación de archivos; entrega pesada vía OneDrive 1 TB",
    pruebas=["Cliente satisfecho según registro histórico", "Imágenes preparadas en el sitio (sin página)"],
    presencia="Sin página pública", links=[],
    c_publico=False, c_contenido=None, c_permiso=False, c_comercial=None, c_cruce=None,
    limite="Requiere permiso y material final para caso público.", siguiente="Pedir permiso y testimonio; publicar caso 360.",
    fuente="KOBOS · Trayectoria"),
  P(id="food", nombre="LATTICCE Food (piloto)", tipo="Piloto", estado="Piloto", nodo="Studio", nodos="Studio",
    etapa="q2", inicio="2026-06-15", inicio_q="aprox",
    definido="Foto y video gastronómico; identidad Food; propuestas Due Fratelli; protocolo visual",
    pendiente="Paquetes mensuales; carrusel panorámico; fichas de prospecto",
    pruebas=["2 piezas Due Fratelli en el Book", "@latticce_food siguió 27 cuentas", "CRM Food: 50 cafés"],
    presencia="2 casos públicos (Due Fratelli)", links=[L("Due Fratelli · Food styling", B+"due-fratelli-food-styling/"), L("Due Fratelli · Food film", B+"due-fratelli-food-film/")],
    c_publico=True, c_contenido=True, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="Piloto: no llamarlo caso de éxito ni entrega final.", siguiente="Registrar las 27 cuentas como prospectos con cadencia.",
    fuente="KOBOS · LATTICCE Food · Trayectoria"),
  P(id="rodadas", nombre="Rodadas (360 + dron)", tipo="Producto", estado="Producto construido", nodo="Studio", nodos="Studio",
    etapa="q3", inicio=None, inicio_q="falta", definido="Fotografía, video, Insta360 y dron", pruebas=[], presencia="Sin página pública", links=[],
    c_publico=False, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="Registrar venta y entrega por caso.", siguiente="Primera rodada documentada como caso.", fuente="KOBOS · Trayectoria"),
  P(id="seferan", nombre="SEFERAN — SFA Packaging", tipo="Prospecto", estado="Prospecto / oportunidad", nodo="Studio", nodos="Studio",
    etapa="q3", inicio="2026-08-11", inicio_q="exacta",
    definido="Necesidad detectada; 3 paquetes diseñados", pendiente="Mostrar comparativa; enviar; registrar fecha; seguimiento; anticipo",
    pruebas=["Cotizaciones en PDF (interno)"], presencia="Sin presencia pública", links=[],
    c_publico=False, c_contenido=False, c_permiso=None, c_comercial=True, c_cruce=None,
    limite="No es producción ejecutada: prospecto hasta anticipo.", siguiente="Enviar cotización y registrar la fecha de envío.",
    fuente="KOBOS · 12 Prospectos/SEFERAN"),
  P(id="somekicks", nombre="Somekicks", tipo="Prospecto", estado="Prospecto / oportunidad", nodo="Agency", nodos="Agency",
    etapa="q3", inicio="2026-09-08", inicio_q="exacta", definido="Diagnóstico y propuestas preparadas", pruebas=["Propuestas preparadas (interno)"],
    presencia="Sin presencia pública", links=[], c_publico=False, c_contenido=False, c_permiso=None, c_comercial=True, c_cruce=None,
    limite="Sin envío ni respuesta registrados.", siguiente="Registrar si se envió y su resultado.", fuente="Dashboard 2026 · lotes"),
  P(id="gps", nombre="GPS / flota", tipo="Prospecto", estado="Prospecto / oportunidad", nodo="Agency", nodos="Agency",
    etapa="q3", inicio="2026-09-30", inicio_q="exacta", definido="Discovery de monitoreo vehicular", pruebas=[], presencia="Sin presencia pública", links=[],
    c_publico=False, c_contenido=False, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="No es ingreso ni proyecto cerrado.", siguiente="Ficha de oportunidad tecnológica con siguiente compromiso.", fuente="KOBOS · Trayectoria"),
  P(id="tennis", nombre="Tennis", tipo="Prospecto", estado="Prospecto / oportunidad", nodo="Agency", nodos="Agency, Studio",
    etapa="oct", inicio=None, inicio_q="falta", definido="Referido interno Studio → Agency para automatización", pruebas=[], presencia="Sin presencia pública", links=[],
    c_publico=False, c_contenido=False, c_permiso=None, c_comercial=None, c_cruce=True,
    limite="Requiere clasificación y diagnóstico.", siguiente="Clasificar y agendar diagnóstico.", fuente="KOBOS · Trayectoria"),
  P(id="prospeccion", nombre="Prospección 2026", tipo="Proyecto interno", estado="Piloto", nodo="LATTICCE", nodos="Studio, Design, Agency",
    etapa="q3", inicio="2026-08-30", inicio_q="exacta", definido="7 lotes registrados; Misión 001 Querétaro; protocolo de primer contacto",
    pendiente="Respuestas, diagnósticos y cierres", pruebas=["161 prospectos registrados", "13 contactos confirmados", "0 cierres atribuibles"],
    presencia="Interna", links=[L("Reporte 2026", "https://claude.ai/artifact/Hv9TAceueAQmfZfckUuuJK", False)],
    c_publico=False, c_contenido=False, c_permiso=None, c_comercial=True, c_cruce=None,
    limite="No acredita la Primera Expedición Comercial.", siguiente="Tandas de 3 con registro el mismo día (ventana al 10 de diciembre).",
    fuente="Dashboard 2026 · Cierre comercial 2026"),
  P(id="uroboros", nombre="UROBOROS · latticce.com", tipo="Proyecto interno", estado="En desarrollo", nodo="Agency", nodos="Studio, Sound, Design, Agency, Time, Films",
    etapa="q3", inicio="2026-08-17", inicio_q="exacta", definido="Sitio público con 6 nodos, Book, blog, 3 servicios de Agency y Films cinema",
    pendiente="Imágenes reales en Studio; analítica; QA y precios de servicios; plataforma integral",
    pruebas=["49 páginas del Book", "45 artículos del blog", "Auditoría web Studio (24-oct)"],
    presencia="Sitio público", links=[L("latticce.com", "https://latticce.com/"), L("Book", B), L("Blog", "https://latticce.com/blog/"), L("Auditoría Studio", "https://claude.ai/artifact/8uvXFprb5KaAY3fbcCaSFk", False)],
    c_publico=True, c_contenido=True, c_permiso=None, c_comercial=True, c_cruce=True,
    limite="Distinguir local, preparado, publicado y verificado.", siguiente="Reemplazar imágenes generadas y medir contactos.",
    fuente="KOBOS · Proyecto UROBOROS · sitemap latticce.com"),
  P(id="chacha", nombre="CHACHA APP", tipo="Proyecto interno", estado="En desarrollo", nodo="Agency", nodos="Agency",
    etapa="q2", inicio=None, inicio_q="falta", definido="Protocolo de 16 fases; Cerebro CHACHA; sistema de producción",
    pendiente="Completar pipeline; validar OpenClaw y prompts; terminar caso Frutisa", pruebas=["Piloto Frutisa", "Caso estratégico Shakti"],
    presencia="Interna", links=[], c_publico=False, c_contenido=False, c_permiso=None, c_comercial=True, c_cruce=True,
    limite="No es un cliente ni un producto a la venta.", siguiente="Terminar el caso piloto Frutisa.", fuente="KOBOS · CHACHA APP"),
  P(id="kobos", nombre="KOBOS", tipo="Herramienta", estado="Activo", nodo="LATTICCE", nodos="Todos",
    etapa="oct", inicio="2026-10-21", inicio_q="aprox", definido="Memoria, trazabilidad y contexto (127 notas)", pruebas=["Trayectoria LATTICCE (28-oct)"],
    presencia="Interna", links=[], c_publico=False, c_contenido=False, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="No reemplaza validación humana ni expedientes.", siguiente="Expedientes de OKAME, CVP, Aby y Ali y Floripondios.", fuente="KOBOS"),
  P(id="cloudex", nombre="LATTICCE OS · CLOUDEX", tipo="Herramienta", estado="Activo", nodo="LATTICCE", nodos="Todos",
    etapa="oct", inicio="2026-10-01", inicio_q="aprox", definido="Coordinación de Jira, KOBOS, Codex, Claude y agentes", pruebas=["Agentes: Vendedor Lattente, Producción"],
    presencia="Interna", links=[], c_publico=False, c_contenido=False, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="Automatizar administración, no autoridad.", siguiente="Automatizar solo lo repetitivo confirmado (24–30 nov).", fuente="KOBOS · CLOUDEX"),
  P(id="calculadora", nombre="Calculadora / tabulador", tipo="Herramienta", estado="Activo", nodo="Studio", nodos="Studio",
    etapa="q3", inicio="2026-08-15", inicio_q="exacta", definido="Cotizador, horas y renta de equipo", pruebas=["Codex/TABULADOR"],
    presencia="Interna", links=[], c_publico=False, c_contenido=False, c_permiso=None, c_comercial=True, c_cruce=None,
    limite="No cotiza ni aprueba por sí sola.", siguiente="Capacitar a quien cotiza.", fuente="KOBOS · Trayectoria"),
  P(id="mol3", nombre="MOL3", tipo="Piloto", estado="Piloto", nodo="Agency", nodos="Agency",
    etapa="oct", inicio=None, inicio_q="falta", definido="Personalización Eleventa; prueba RAE/software", pruebas=[], presencia="Interna", links=[],
    c_publico=False, c_contenido=False, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="No declarar método validado ni producto terminado.", siguiente="Documentar requisitos, pruebas y aprendizaje.", fuente="KOBOS · Trayectoria"),
  P(id="marca", nombre="Sistema de marca LATTICCE", tipo="Proyecto interno", estado="Activo", nodo="LATTICCE", nodos="Todos",
    etapa="2025", inicio="2026-03-27", inicio_q="exacta", definido="Manual 2026; logos por nodo; sistema cromático; voz; Logo Match Cut; brochures por nodo; deck 2027",
    pruebas=["Manual de marca 2026", "Brochures Design, Agency y Sound", "Deck LATTICCE 2027"], presencia="Aplicada en el sitio",
    links=[L("Deck 2027", "https://claude.ai/artifact/7ftYMKQrGvYt7njuQejjbK", False)],
    c_publico=True, c_contenido=True, c_permiso=True, c_comercial=True, c_cruce=None,
    limite="Logos oficiales nunca generados con IA.", siguiente="Kit de ventas mínimo (3–9 nov).", fuente="KOBOS · 03 Identidad"),
  P(id="sinttergia", nombre="SINTTERGIA LATTENTTE", tipo="Autoral", estado="Activo", nodo="LATTICCE", nodos="Comunidad",
    etapa="2025", inicio=None, inicio_q="falta", definido="Comunidad de práctica; sesiones; archivo de conocimiento",
    pendiente="Núcleo de 3–5 personas constantes; sesiones semanales", pruebas=["Canales de comunidad activos"],
    presencia="Instagram, Facebook y WhatsApp propios", links=[L("Instagram", "https://www.instagram.com/sinttergia____lattentte/"), L("Facebook", "https://www.facebook.com/profile.php?id=61589840495010")],
    c_publico=True, c_contenido=None, c_permiso=True, c_comercial=False, c_cruce=None,
    limite="No es nodo comercial de LATTICCE.", siguiente="Consolidar el núcleo y el ritmo semanal.", fuente="KOBOS · 05 Sinttergia Lattentte"),
  P(id="oraculo", nombre="Oráculo Digital", tipo="Autoral", estado="Activo", nodo="LATTICCE", nodos="Design",
    etapa="oct", inicio=None, inicio_q="falta", definido="Lectura, prompt, dirección visual e iteración", pruebas=[], presencia="Sin dato", links=[],
    c_publico=None, c_contenido=None, c_permiso=None, c_comercial=None, c_cruce=None,
    limite="No declarar volumen sin inventario verificable.", siguiente="Inventario de piezas.", fuente="KOBOS · Trayectoria"),
]

book = []
import re
REAL = ["alejate-los-chicklets|ALEJATE|Studio|Videoclip", "peculiar-karell|PECULIAR|Studio|Videoclip", "hecho-para-ti-jimena-hermida|HECHO PARA TI|Studio|Videoclip",
        "due-fratelli-food-styling|Due Fratelli|Studio|Food styling", "due-fratelli-food-film|Due Fratelli / Food Film|Studio|Food film",
        "sofia-stainer-foro-la-paz|Sofía Stainer|Studio|Concierto", "frine-round-one|Friné|Studio|Concierto", "grtsch-xxi-monomita|GRTSCH|Studio|Concierto",
        "diana-meril-ambar|Diana Meril|Studio|Concierto", "la-bande-son-imaginaire|La Bande-Son Imaginaire|Studio|Concierto", "pepe-madero-pulso-gnp|José Madero|Studio|Concierto",
        "enjambre-estadio-gnp|Enjambre|Studio|Concierto", "maria-daniela-y-su-sonido-lasser|María Daniela y Su Sonido Lasser|Studio|Concierto", "surfistas-del-sistema|Surfistas del Sistema|Studio|Concierto",
        "dani-milka-lavanderia|Dani Mikal|Studio|Sesión", "folclore-mexicano|Folclore mexicano|Studio|Sesión", "pablito-navajas-retrato-exterior|Pablito Navajas|Studio|Sesión",
        "pablito-navajas-traperos|Pablito Navajas + Blackman|Studio|Sesión", "susana-cuervo-cafe|Susana Cuervo|Studio|Sesión",
        "boda-memoria-completa|Una memoria de boda|Time|Bodas", "preparativos-de-boda|Antes de la ceremonia|Time|Bodas", "celebracion-de-boda|La celebración|Time|Bodas",
        "sesion-de-novios|Sesión de novios|Time|Sesión de novios", "sesion-de-pareja-en-naturaleza|Sesión junto al agua|Time|Sesión de pareja", "retratos-familiares-time|Retratos familiares|Time|Familia",
        "okame|OKAME|Design|Identidad visual", "shakti-yoga-estudio|Shakti Yoga Estudio|Design|Identidad visual", "frutisa-branding-sitio-web|Frutisa|Design|Identidad + Brand Pet",
        "ingles-con-jeremy-sitio-web|Inglés con Jeremy|Agency|Ecosistema digital"]
MUESTRA = ["voces-para-un-branding|Voces para un Branding|Sound|Sonic branding", "archivo-nocturno|Archivo nocturno|Agency|Campañas", "sistema-cero|Sistema Cero|Agency|Ecosistemas digitales",
           "frecuencia-mineral|Frecuencia mineral|Sound|Instalación sonora", "sesion-umbral|Sesión Umbral|Sound|Producción musical", "materia-01|Materia 01|Design|Identidad", "archivo-naranja|Archivo naranja|Design|Editorial"]
for tipo, lst in (("Proyecto real", REAL), ("Muestra o concepto", MUESTRA)):
    for s in lst:
        slug, t, n, c = s.split("|")
        book.append({"slug": slug, "titulo": t, "nodo": n, "categoria": c, "tipo": tipo, "url": B + slug + "/"})

blog_raw = """como-elegir-que-fotografias-merecen-permanecer time 2026-11-27
antes-de-invertir-en-pauta-revisa-si-tu-mensaje-esta-preparado agency 2026-11-24
que-debe-hacer-cada-red-social-dentro-de-tu-estrategia agency 2026-11-21
como-elegir-una-tipografia-por-lo-que-hace design 2026-11-18
como-grabar-ambientes-que-describan-un-lugar sound 2026-11-15
como-iluminar-un-retrato-con-una-sola-fuente studio 2026-11-12
como-construir-tension-visual-sin-mover-la-camara films 2026-11-10
como-construir-un-dj-set-que-cuente-una-historia sound 2026-11-09
como-crear-tension-cinematografica-utilizando-solo-sonido sound 2026-11-06
el-color-empieza-antes-del-etalonaje films 2026-10-22
como-leer-una-locacion-antes-de-iluminarla studio 2026-10-24
como-elegir-un-microfono-sin-empezar-por-la-marca sound 2026-10-27
disenar-para-una-pantalla-no-es-encoger-una-pagina design 2026-10-29
una-marca-se-construye-con-decisiones-repetidas agency 2026-10-31
lo-que-una-fotografia-no-dice-cuando-la-miras-sola time 2026-11-03
que-cambia-cuando-cambias-de-optica films 2026-10-08
que-llevar-a-un-rodaje-sin-llevar-de-mas studio 2026-10-10
como-preparar-una-sesion-de-grabacion-que-no-pierda-energia sound 2026-10-13
la-reticula-no-ordena-por-ti design 2026-10-15
un-brief-no-es-un-formulario agency 2026-10-17
como-editar-un-album-para-que-el-dia-conserve-su-ritmo time 2026-10-20
como-preparar-un-scouting-de-locacion-cinematografica films 2026-09-24
como-dirigir-a-una-persona-que-no-es-modelo studio 2026-09-26
como-grabar-una-entrevista-en-una-locacion-dificil sound 2026-09-29
conocias-esta-tecnica-risografia design 2026-10-01
la-pagina-de-inicio-no-tiene-que-contarlo-todo agency 2026-10-03
cinco-fotografos-de-boda-mexicanos time 2026-10-06
el-espacio-tambien-dirige films 2026-09-21
exponer-para-la-luz-que-cambia studio 2026-09-18
la-mezcla-empieza-en-la-distancia sound 2026-09-15
el-color-como-sistema-de-orientacion design 2026-09-11
la-atencion-no-se-compra-se-construye agency 2026-09-08
una-noche-no-cabe-en-una-imagen time 2026-09-04
poner-en-escena-es-construir-relaciones films 2026-08-30
cubrir-un-concierto-sin-borrar-al-publico studio 2026-08-26
lo-que-el-publico-devuelve-al-escenario sound 2026-08-21
disenar-una-secuencia-no-una-coleccion design 2026-08-16
una-idea-debe-sobrevivir-al-formato agency 2026-08-10
editar-memoria-es-conservar-relaciones time 2026-08-03
conocias-esta-tecnica-linograbado-reduccion design 2026-09-20
conecta-mejor-el-secreto-de-un-buen-ecommerce agency 2026-09-19
antes-de-pedir-presupuesto-audiovisual films 2026-09-17
como-grabar-una-voz sound 2026-09-14
como-editar-un-piano sound 2026-09-12
cinco-wedding-planners-mexico time 2026-09-10"""
blog = []
for line in blog_raw.splitlines():
    slug, n, f = line.split()
    blog.append({"slug": slug, "nodo": n.capitalize(), "fecha": f, "url": "https://latticce.com/blog/" + slug + "/"})

etapas = [
  {"id": "2025", "orden": 1, "periodo": "2025", "inicio": "2025-01-01", "fin": "2025-12-31", "nombre": "Descubrimiento", "pregunta": "¿Qué es LATTICCE?", "cadena": "Capacidades → identidad → visión", "estado": "Cerrada"},
  {"id": "q1", "orden": 2, "periodo": "Q1 2026", "inicio": "2026-01-01", "fin": "2026-03-31", "nombre": "Arquitectura", "pregunta": "¿Cómo se organiza?", "cadena": "Nodos → personas → servicios → contratos", "estado": "Cerrada"},
  {"id": "q2", "orden": 3, "periodo": "Q2 2026", "inicio": "2026-04-01", "fin": "2026-06-30", "nombre": "Experimentación", "pregunta": "¿Podemos hacerlo?", "cadena": "Floripondios → bodas → clientes → Frutisa → web → audio → producción → Jira", "estado": "Cerrada"},
  {"id": "q3", "orden": 4, "periodo": "Q3 2026", "inicio": "2026-07-01", "fin": "2026-09-30", "nombre": "Productización", "pregunta": "¿Podemos venderlo claramente?", "cadena": "Paquetes → precios → Time → Studio → Agency → CRM → contenido → Traductor de Mercados", "estado": "Cerrada"},
  {"id": "oct", "orden": 5, "periodo": "Octubre 2026", "inicio": "2026-10-01", "fin": "2026-10-27", "nombre": "Sistematización", "pregunta": "¿Puede funcionar sin depender de una sola persona?", "cadena": "LATTICCE OS → UROBOROS → Codex → Claude → KOBOS → CLOUDEX → equipo → agentes → documentación", "estado": "Cerrada"},
  {"id": "val", "orden": 6, "periodo": "Nov–dic 2026", "inicio": "2026-10-28", "fin": "2026-12-10", "nombre": "Validación", "pregunta": "¿Podemos provocar el resultado?", "cadena": "Mercado elegido → prospecto verificable → contacto humano → conversación → diagnóstico → propuesta → anticipo → producción → caso → venta cruzada → aprendizaje", "estado": "En curso"},
  {"id": "2027", "orden": 7, "periodo": "2027", "inicio": "2026-12-11", "fin": "2027-12-31", "nombre": "Escala informada", "pregunta": "¿El ciclo se repite con evidencia?", "cadena": "Repetir lo que funcionó → venta cruzada → recurrencia → escalar lo probado", "estado": "Siguiente"},
]

madurez = [{"dimension": d, "pct": p} for d, p in [
  ("Visión / dirección", 100), ("Identidad", 90), ("Servicios / productos", 90), ("Capacidad técnica + red", 85), ("Infraestructura operativa", 80),
  ("Documentación / OS / KOBOS", 80), ("Experiencia real / portafolio", 75), ("Web / presencia", 70), ("Equipo autónomo", 60), ("Contenido sistemático", 55),
  ("Prospección sistemática", 40), ("Ventas predecibles", 20), ("Recurrencia medible", 10)]]

def node(n, color, rol, oferta, resp, ig, fb, web, vis, alc, inter, conv, food=False):
    return {"nodo": n, "color": color, "rol": rol, "oferta": oferta, "responsable": resp, "instagram": ig, "facebook": fb, "web": web,
            "visualizaciones_28d": vis, "alcance_ig_28d": alc, "interacciones_28d": inter, "conversaciones_28d": conv}
nodos = [
  node("Studio", "#EAB43F", "Producción visual: foto, video, videoclips, conciertos; línea Food.", "Productos definidos (videoclip, Retrato Express); precios por formalizar",
       "Coordinación provisional en Dirección general; Hernán, referente técnico", "https://www.instagram.com/___latticce___/", "https://www.facebook.com/profile.php?id=61594764417597", "https://latticce.com/studio/", 35578, 8100, 2500, 0),
  node("Sound", "#7643AE", "Voz, música, mezcla, diseño e identidad sonora.", "Precios y paquetes por formalizar",
       "Coordinación provisional en Dirección general; Alejandro en formación", "https://www.instagram.com/latticce.sound/", "https://www.facebook.com/profile.php?id=61588752884212", "https://latticce.com/sound/", 525, 53, 13, 0),
  node("Design", "#FE5C14", "Sistemas visuales: branding, campañas, 3D, motion.", "Precios y paquetes por formalizar",
       "Responsable por definir", "https://www.instagram.com/latticce.design/", "https://www.facebook.com/profile.php?id=61589128948498", "https://latticce.com/design/", 587, 200, 37, 0),
  node("Agency", "#72E7FF", "Estrategia digital, web, RRSS, Ads, IA y automatización.", "3 servicios publicados en el sitio; precios por formalizar",
       "Daniel Mondragón, referente técnico; coordinación por proyecto", "https://www.instagram.com/latticce.agency/", "https://www.facebook.com/profile.php?id=61589054697841", "https://latticce.com/agency/", 310, 14, 14, 0),
  node("Time", "#EAE4D8", "Memoria cinematográfica: bodas, XV y eventos.", "5 paquetes definidos",
       "Liderazgo por consolidar", "https://www.instagram.com/latticce.time/", None, "https://latticce.com/time/", None, None, None, None),
  node("Films", "#F2F1EC", "Narrativa y cine autoral; en desarrollo.", "Oferta proyectada",
       "Responsable por definir", "https://www.instagram.com/latticce.films/", "https://www.facebook.com/latticce.films", "https://latticce.com/films/", None, None, None, None),
]

capacidad = [
  {"area": "Producción audiovisual", "relacion": "Studio, Hernán y equipo por proyecto", "estado": "Operativa; asignar por disponibilidad"},
  {"area": "360", "relacion": "Equipo propio + cámara adicional de Dani", "estado": "Disponible por confirmar en cada cobertura"},
  {"area": "Sound", "relacion": "Alejandro, Home Studio, TASCAM + Sennheiser de campo", "estado": "Infraestructura funcional; disponibilidad limitada"},
  {"area": "Producción musical", "relacion": "Rex, contacto con experiencia externa", "estado": "Colaboración potencial"},
  {"area": "Postproducción especializada", "relacion": "Especialista de Floripondios", "estado": "Colaborador puntual"},
  {"area": "Software / QA", "relacion": "Daniel y Agency", "estado": "Por proyecto y disponibilidad"},
  {"area": "Diseño", "relacion": "Capacidad interna; incorporaciones en evaluación", "estado": "Autonomía por consolidar"},
  {"area": "Producción física", "relacion": "Ángel / ADN, impresión y textil", "estado": "Proveedor externo; cotizar por proyecto"},
  {"area": "Ventas / prospección", "relacion": "Participantes autorizados; KOBOS como soporte", "estado": "Contacto y decisión humanos"},
]

def H(fecha, q, area, nodo, hito, detalle, evidencia, estado="acreditado", proyecto="", url=""):
    return {"fecha": fecha, "fecha_q": q, "area": area, "nodo": nodo, "hito": hito, "detalle": detalle, "evidencia": evidencia, "estado": estado, "proyecto": proyecto, "url": url}

DET = {
 "Manual de marca": "Manual de 63 hojas (Affinity, fuente Kinetic) y versión esencial de 10 hojas.",
 "Logos por nodo": "Logotipos e isotipo TT de los 6 nodos en SVG y PNG.",
 "Primeras publicaciones": "Arranque de @latticce.design: 7 publicaciones entre mayo y julio.",
 "Voz LATTICCE": "Grabaciones de voz: fundacionales, lore y piezas modulares.",
 "Cartera registrada": "Shakti, Frutisa, DESHii y SOMA con prioridad y estado en KOBOS.",
 "Sistema comercial": "Embudo único y funciones comerciales por nodo.",
 "SEFERAN": "Prospecto referido para video empresarial; tres paquetes diseñados, envío sin fecha registrada.",
 "Modelo financiero": "Estructura financiera por nodo (sin cifras en este tablero).",
 "Brand kit de Shakti": "Kit de marca de Shakti Yoga Estudio en Codex/DISEÑOS.",
 "Tabulador": "Cotizador interno de horas, servicios y renta de equipo.",
 "Arranca el sitio": "Primer commit del sitio UROBOROS (Next.js).",
 "Publicadas experiencias": "Páginas de Studio, Sound y Design en latticce.com.",
 "CRM piloto": "Lote de 44 prospectos musicales investigados; ningún mensaje enviado.",
 "75 comunidades": "Grupos y comunidades de CDMX y Edomex mapeados para difusión.",
 "CRM Design": "50 prospectos de Design en 5 nichos con scoring.",
 "4 DM": "4 mensajes directos confirmados desde Design; sin respuesta registrada.",
 "Somekicks": "Diagnóstico y propuestas preparadas; sin envío ni resultado registrado.",
 "Protocolo de primer": "Guion y reglas del primer contacto comercial.",
 "Discovery GPS": "Exploración de una solución de monitoreo vehicular para Agency.",
 "Blog editorial": "Blog con filtro por nodo y bases de SEO; hoy 45 artículos en el sitemap.",
 "Casos reales publicados": "Casos de conciertos, videoclips y clientes en el Book público.",
 "Agency publicada": "latticce.com/agency con 3 servicios: Contenido RRSS, Ecosistemas UI–UX y Distribución Ads.",
 "Shakti: ajustes": "Versión 7 del sitio y portada de Facebook preparadas.",
 "LATTICCE Food": "Identidad Food y propuestas visuales para Due Fratelli.",
 "CRM Food": "50 cafés registrados en estado Nuevo.",
 "Rediseño": "Último commit del sitio: rediseño de la experiencia Design.",
 "Equipo actualizado": "Directorio vigente del equipo en KOBOS (CRH).",
 "KOBOS consolidado": "Bóveda ordenada y primer agente comercial (Vendedor Lattente).",
 "Misión 001": "Prospección en Facebook en Querétaro: 8 comentarios ligeros, sin respuesta.",
 "Video Logo": "Video de 15 s del logo con pista propia.",
 "Brochure Design": "Brochure comercial de Design, 31 láminas.",
 "Brochure UI": "Brochure de Agency y ficha del nodo.",
 "Casos de branding": "PDF de 20 láminas: Frutisa, Shakti y OKAME.",
 "Sistema cromático": "Colores oficiales por nodo y manual esencial.",
 "Metricool": "Metricool conectado a Design y 3 publicaciones preparadas.",
 "Plan cierre": "Directriz de trabajo del 28 de octubre al 10 de diciembre.",
}
old = json.load(open(os.path.join(OUT, "..", "dash", "hitos.json")))
link = {"Cartera registrada": "", "SEFERAN": "seferan", "Brand kit de Shakti": "shakti", "Tabulador": "calculadora", "Arranca el sitio": "uroboros",
        "Publicadas experiencias": "uroboros", "CRM piloto": "prospeccion", "75 comunidades": "prospeccion", "CRM Design": "prospeccion", "4 DM": "prospeccion",
        "Somekicks": "somekicks", "Discovery GPS": "gps", "Blog editorial": "uroboros", "Casos reales publicados": "uroboros", "Agency publicada": "uroboros",
        "Shakti: ajustes": "shakti", "LATTICCE Food": "food", "CRM Food": "food", "Rediseño": "uroboros", "KOBOS consolidado": "kobos", "Misión 001": "prospeccion",
        "Manual de marca": "marca", "Logos por nodo": "marca", "Voz LATTICCE": "marca", "Video Logo": "marca", "Brochure Design": "marca", "Brochure UI": "marca",
        "Casos de branding": "marca", "Sistema cromático": "marca", "Plan cierre": "prospeccion", "Protocolo de primer": "prospeccion", "Sistema comercial": "prospeccion",
        "Modelo financiero": "", "Equipo actualizado": "", "Metricool": "", "Primeras publicaciones": ""}
urls = {"uroboros": "https://latticce.com/", "shakti": B + "shakti-yoga-estudio/", "food": B + "due-fratelli-food-styling/", "prospeccion": "https://claude.ai/artifact/Hv9TAceueAQmfZfckUuuJK"}
hitos = []
for h in old:
    pid = next((v for k, v in link.items() if h["hito"].startswith(k)), "")
    hito = h["hito"].replace("Max entra, Rafa sale", "nuevas incorporaciones")
    estado = "acreditado" if h["estado"] == "acreditado" else "sin resultado"
    if hito.startswith("Modelo financiero"):
        hito = "Modelo financiero por nodo"
    hitos.append(H(h["fecha"], "exacta", h["area"], h["nodo"], hito, next((v for k, v in DET.items() if h["hito"].startswith(k)), "Hito del reporte 2026."), h["evidencia"], estado, pid, urls.get(pid, "")))

hitos += [
  H("2025-04-15", "aprox", "Marca", "LATTICCE", "Foto, video, diseño, sonido, web y marketing bajo una misma lógica", "Se integran especialidades para resolver proyectos conectados, no como catálogo.", "KOBOS · Trayectoria", proyecto="marca"),
  H("2025-09-15", "aprox", "Marca", "LATTICCE", "Surgen los seis nodos", "Studio, Sound, Design, Agency, Time y Films; los servicios sostienen y el cine marca dirección.", "KOBOS · Trayectoria", proyecto="marca"),
  H("2026-02-15", "aprox", "Sistema", "LATTICCE", "Nodos pasan de intención a estructura", "Roles por nodo, formación de equipo, contratos e instrumentos operativos.", "KOBOS · Trayectoria · Nodos de LATTICCE"),
  H("2026-04-15", "aprox", "Producción", "Studio", "Floripondios: producción multinodo", "Narrativa, sonido directo, sincronización, edición y especialista externo de postproducción.", "KOBOS · Trayectoria", proyecto="floripondios"),
  H("2026-05-01", "aprox", "Producción", "Studio", "Conciertos: cobertura y publicación", "Práctica de cobertura, selección y edición; hoy 9 coberturas en el Book.", "Book UROBOROS", proyecto="conciertos", url=B + "enjambre-estadio-gnp/"),
  H("2026-04-01", "aprox", "Producción", "Time", "Bodas y eventos antes de formalizar Time", "Experiencia de cobertura social previa al catálogo.", "KOBOS · Trayectoria", proyecto="bodas"),
  H("2026-05-15", "aprox", "Producción", "Studio", "Aby y Ali 360 entregado", "Captura 360, edición y entrega pesada vía OneDrive de 1 TB; cliente satisfecho según registro.", "KOBOS · Trayectoria", proyecto="abyali"),
  H("2026-06-01", "aprox", "Clientes", "Design", "Frutisa: branding y Brand Pet", "Cliente de branding que se vuelve piloto de CHACHA APP.", "KOBOS · Frutisa", proyecto="frutisa", url=B + "frutisa-branding-sitio-web/"),
  H("2026-06-15", "aprox", "Producción", "Studio", "Piloto gastronómico", "Foto y video sin entrega comercial satisfactoria; deja criterios para LATTICCE Food.", "KOBOS · Trayectoria", estado="sin resultado", proyecto="food"),
  H("2026-06-20", "aprox", "Sistema", "LATTICCE", "Jira organiza el trabajo", "Gestión de tareas del equipo.", "KOBOS · Trayectoria"),
  H("2026-07-15", "aprox", "Comercial", "Time", "Time formaliza 5 paquetes", "Bodas, XV y eventos con sistema de recomendados.", "KOBOS · LATTICCE Time", proyecto="bodas", url="https://latticce.com/time/"),
  H("2026-08-01", "aprox", "Comercial", "Studio", "Studio Music: videoclip y Retrato Express", "Essential / Classic y retrato en locación como productos prioritarios.", "KOBOS · Ventas Studio", proyecto="videoclips"),
  H("2026-09-15", "aprox", "Comercial", "LATTICCE", "Traductor de Mercados y Primera Expedición Comercial", "Pregunta de adquisición repetible y flujo Detectado → Recurrencia.", "KOBOS · Cierre comercial 2026", proyecto="prospeccion"),
  H("2026-10-24", "exacta", "Sitio", "Studio", "Auditoría web de Studio", "5 imágenes generadas en portada; faltan bloques de videoclip y Retrato Express.", "KOBOS · Auditoría web Studio", proyecto="uroboros", url="https://claude.ai/artifact/8uvXFprb5KaAY3fbcCaSFk"),
  H("2026-10-28", "exacta", "Sistema", "LATTICCE", "Trayectoria LATTICCE registrada en KOBOS", "Estados: ejecutado, producto, piloto, prospecto y capacidad.", "KOBOS · 01 Estrategia/Trayectoria", proyecto="kobos"),
  H("2026-10-28", "exacta", "Marca", "LATTICCE", "Deck LATTICCE 2027 · Un sistema LATTENTTE", "17 láminas para presentar al equipo después del corte.", "Este proyecto", proyecto="marca", url="https://claude.ai/artifact/7ftYMKQrGvYt7njuQejjbK"),
]
hitos.sort(key=lambda h: h["fecha"])

# Registro histórico LATTICCE — respaldo detallado 2025-2026 (KOBOS/90 Fuentes, 28-oct): detalle y matriz de cobertura documental
REG = {
 "floripondios": dict(ficha="No", accion_doc="Crear ficha de proyecto interno multinodo.",
   falta_doc="Créditos, estado de edición/post, entregables, derechos, evidencia y siguiente hito",
   definido="Narrativa y producción; sonido directo y retakes con pértiga; sincronización; edición; postproducción y mezcla con especialista externo",
   pruebas=["Postproducción documentada", "Formación de Sound en situación real (Alex)", "Especialista externo para la fase que supera la capacidad interna"]),
 "conciertos": dict(ficha="Parcial", accion_doc="Crear índice de casos/activos y ficha de producto Music.",
   falta_doc="Book/casos de Music, lista de trabajos atribuibles, permisos, alcance vigente y seguimiento por artista",
   limite="No contabilizar como facturación LATTICCE sin expediente; los pagos del medio corresponden a Hernán salvo registro."),
 "videoclips": dict(ficha="Parcial", accion_doc="Ficha de producto Studio Music con alcance y casos.",
   falta_doc="Lista de trabajos atribuibles y permisos por artista"),
 "retrato": dict(ficha="Parcial", accion_doc="Integrar a la ficha de producto Studio Music.", falta_doc="Precio y alcance vigentes"),
 "bodas": dict(ficha="Parcial", accion_doc="Crear expediente por evento; consolidar catálogo/alianzas aparte.",
   falta_doc="Expediente por evento; alianzas confirmadas (salones, wedding planners, coreógrafos)",
   pruebas=["6 memorias en el Book de Time", "7 artículos del blog de Time", "Negociación de la primera boda (Hernán)", "Gorras y etiquetas LATTICCE para la primera boda"]),
 "abyali": dict(ficha="No", accion_doc="Crear ficha ejecutada y concentrar permiso/evidencia.",
   falta_doc="Consentimiento, fecha, responsables, archivos, testimonio y autorización de portafolio",
   definido="Captura con Insta360 (Dirección); segunda cámara 360 de Dani; edición; preparación de archivos; entrega pesada vía OneDrive 1 TB",
   pruebas=["Cliente satisfecho según registro histórico", "Flujo validado: captura 360 → archivos → edición → almacenamiento pesado → entrega remota", "Imágenes preparadas en el sitio (sin página)"]),
 "food": dict(ficha="No", accion_doc="Crear registro histórico del piloto y aprendizajes (la vertical sí tiene ficha).",
   falta_doc="Ficha del piloto gastronómico, cliente/permiso, estado de materiales y lecciones",
   definido="Foto y video gastronómico (Hernán, Sony Alpha y celulares); montaje y color (Dirección); identidad Food; propuestas Due Fratelli",
   pruebas=["2 piezas Due Fratelli en el Book", "@latticce_food siguió 27 cuentas", "CRM Food: 50 cafés", "Aprendizaje: criterios visuales y aprobaciones antes de producir"],
   limite="Piloto: no se monetizó ni llegó a entrega final completa; no llamarlo caso de éxito."),
 "rodadas": dict(ficha="No", accion_doc="Crear ficha de producto con costos/alcance/casos.",
   falta_doc="Alcance y exclusiones, proyectos ejecutados, responsables y permisos de vuelo",
   definido="4 niveles por duración, foto, video, Insta360 y dron"),
 "frutisa": dict(ficha="Sí", accion_doc="Completar estado, dependencias y vínculo CHACHA."),
 "shakti": dict(ficha="Sí", accion_doc="Mantener expediente y evidencias de desarrollo/QA."),
 "deshii": dict(ficha="Sí", accion_doc="Mantener expediente."),
 "soma": dict(ficha="Sí", accion_doc="Mantener expediente."),
 "okame": dict(ficha="No", accion_doc="Crear expediente y confirmar permiso de uso público.", falta_doc="Expediente, permiso y estado en KOBOS"),
 "jeremy": dict(ficha="No", accion_doc="Crear ficha histórica cuando se confirme entidad/permiso.",
   falta_doc="Cliente/permiso, alcance, estado de implementación, activos y evidencia",
   definido="SITE123 con estructura educativa: niveles, videoteca, audioteca y podcast"),
 "cvp": dict(ficha="No", accion_doc="Crear ficha histórica cuando se confirme entidad/permiso.",
   falta_doc="Entidad, alcance, estado de activos, permiso y resultado verificable",
   definido="Medio local: logotipo, portada, mapa del Estado de México y meta de visitas"),
 "seferan": dict(ficha="Sí", accion_doc="Actualizar contacto, envío, respuesta y anticipo."),
 "somekicks": dict(ficha=None, accion_doc="Confirmar si tiene ficha de prospecto en KOBOS."),
 "gps": dict(ficha="No", accion_doc="Crear ficha de prospecto tras identificar entidad/contacto.",
   falta_doc="Entidad, contacto autorizado, necesidad, responsable, etapa y siguiente acción",
   definido="Flota aproximada de 50 unidades; presentación, QA, responsable, stack y presupuesto explorados"),
 "tennis": dict(ficha="No", accion_doc="Crear ficha de prospecto antes de contacto.",
   falta_doc="Clasificación humana, diagnóstico y decisión de oferta",
   definido="Hernán detecta la necesidad y la conecta con Agency (automatización de mensajes)"),
 "mol3": dict(ficha="No", accion_doc="Crear ficha de piloto Agency Software.",
   falta_doc="Entidad, autorización, alcance, responsables, requisitos, riesgos, versiones, QA y próximo hito",
   estado="Piloto", definido="Piloto 1 de Agency Software: personalización sobre Eleventa; prueba del método RAE",
   pruebas=["Ruta del piloto: necesidad → levantamiento → requisitos → arquitectura → ejecución → pruebas → documentación"]),
 "prospeccion": dict(ficha="Parcial", accion_doc="Mantener registro el mismo día por tanda."),
 "uroboros": dict(ficha="Sí", accion_doc="Mantener estados local/preparado/publicado/verificado."),
 "chacha": dict(ficha="Sí", accion_doc="Mantener piloto Frutisa y estado de pipeline."),
 "kobos": dict(ficha="Sí", accion_doc="Mantener mapa y fuentes enlazadas.",
   pruebas=["Trayectoria LATTICCE (28-oct)", "Registro histórico 2025–2026 con matriz de cobertura (28-oct)"]),
 "cloudex": dict(ficha="Sí", accion_doc="Mantener la estrategia CLOUDEX al día."),
 "calculadora": dict(ficha="No", accion_doc="Registrar herramienta, versión y manual de uso.",
   falta_doc="Vínculo canónico, manual, responsable, versión, criterios de uso y capacitación",
   definido="Criterio común de estimación: tipo de proyecto, complejidad, jornadas, personal, equipo, post, traslados, entregables y extras"),
 "marca": dict(ficha="Sí", accion_doc="Mantener manual y sistema cromático."),
 "sinttergia": dict(ficha="Sí", accion_doc="Mantener separación de LATTICCE comercial."),
 "oraculo": dict(ficha="No", accion_doc="Crear índice editorial y archivo de piezas.",
   falta_doc="Metodología, piezas, archivos, calendario, fuentes y estado de publicación",
   definido="Tonalpohualli, Elder Futhark y Tarot; estructura editorial fija; biblia visual en piedra/obsidiana y azul-cian"),
}
for p in proyectos:
    r = REG.get(p["id"], {})
    p.setdefault("ficha", None); p.setdefault("accion_doc", ""); p.setdefault("falta_doc", "")
    p.update(r)
    if "Registro histórico" not in p["fuente"] and p["id"] in REG and REG[p["id"]].get("ficha") is not None:
        p["fuente"] += " · Registro histórico 2025–2026"

# Investigación y cobertura de frentes (ChatGPT/LATTICCE OS, 28-oct 16:27): clasificación sustentada, faltantes y preguntas abiertas
INV = {
 "oraculo": dict(clasif="Laboratorio editorial de SINTTERGIA LATTENTTE; no nodo comercial.", falta_doc="Índice de piezas, fechas, archivos, publicación o envío y permisos"),
 "jeremy": dict(clasif="Proyecto digital histórico.", falta_doc="Entidad y permiso, alcance, activos y estado final",
   pregunta="¿Cuál es la entidad correcta y hay permiso para conservar o publicar los materiales?"),
 "cvp": dict(clasif="Proyecto histórico de medio local.", falta_doc="Entidad, activos, permiso y resultado verificable",
   pregunta="¿Cuál es la entidad correcta y hay permiso para conservar o publicar los materiales?"),
 "rodadas": dict(clasif="Producto construido; experiencia por documentar.", falta_doc="Alcance, exclusiones, costos, casos ejecutados y permisos de vuelo"),
 "okame": dict(clasif="Sin evidencia localizada en KOBOS ni en los chats revisados; solo su página en el Book.", falta_doc="Entidad, contacto, alcance, estado y fuente original",
   pregunta="¿Cuál es la entidad, el contacto autorizado y el objetivo de OKAME?"),
 "mol3": dict(clasif="Piloto 1 iniciado de Agency Software.", falta_doc="Ficha de piloto, autorización, requisitos, versiones, QA y siguiente hito",
   pregunta="¿Quién autorizó el piloto, cuál es el alcance actual y dónde están las versiones y el QA?"),
 "floripondios": dict(clasif="Ejecutado; producción interna y autoral multinodo.", falta_doc="Ficha integral, créditos, derechos, estado de post, entregables y permiso",
   pregunta="¿Qué entregable final existe, quién aprobó los créditos y puede mencionarse públicamente?"),
 "abyali": dict(clasif="Ejecutado.", falta_doc="Fecha, permiso, evidencia final, responsables y testimonio autorizado",
   pregunta="¿Cuál fue la fecha, cómo se puede nombrar al cliente y existe permiso escrito para portafolio?"),
 "food": dict(clasif="Piloto ejecutado; cierre comercial no satisfactorio.", falta_doc="Cliente y permiso, materiales, estado de entrega y lecciones concentradas"),
 "gps": dict(clasif="Oportunidad tecnológica.", falta_doc="Entidad, contacto autorizado, necesidad, etapa y responsable"),
 "tennis": dict(clasif="Prospecto pendiente.", falta_doc="Ficha de prospecto antes de contacto o propuesta"),
 "videoclips": dict(clasif="Producto priorizado en validación.", falta_doc="Casos atribuibles, permisos, alcance vigente y seguimiento"),
 "retrato": dict(clasif="Producto o servicio sin expediente individual localizado.", ficha="No", accion_doc="Crear ficha de producto (puede integrarse a Studio Music).",
   falta_doc="Oferta, casos, responsables, permisos y resultado"),
 "bodas": dict(clasif="Experiencia y producto Time; expediente parcial.", falta_doc="Expediente por evento, permisos, entregables y catálogo de alianzas"),
 "somekicks": dict(clasif="Sin confirmar: no se localizó fuente canónica.", ficha="No", accion_doc="Confirmar entidad y fuente antes de abrir ficha.",
   falta_doc="Entidad, fuente, alcance, relación y estado", pregunta="¿Cuál es la entidad, el contacto autorizado y el objetivo de Somekicks?"),
 "kobos": dict(clasif="Infraestructura operativa activa.", falta_doc="Avance por entregables, evidencia de uso y política de venta cruzada"),
 "cloudex": dict(clasif="Sistemas internos activos o en desarrollo.", falta_doc="Avance por entregables, permisos de uso comercial y resultados medibles"),
 "calculadora": dict(clasif="Herramienta interna de cotización.", falta_doc="Ruta canónica, versión, responsable, manual y capacitación",
   pregunta="¿Dónde vive la versión vigente de la calculadora y quién puede modificar sus criterios?"),
 "sinttergia": dict(clasif="Comunidad de práctica, separada de LATTICCE comercial.", falta_doc="Fecha de inicio, entregables y ritmo"),
 "deshii": dict(clasif="Cliente; desarrollo de marca.", falta_doc="Packaging, web, foto profesional y punto de venta"),
 "soma": dict(clasif="Cliente; desarrollo de marca.", falta_doc="Manual, redes y sitio web"),
 "conciertos": dict(clasif="Experiencia real y producto construido en validación.", falta_doc="Índice de casos, activos, permisos, oferta y métricas"),
 "seferan": dict(clasif="Prospecto en propuesta o cotización; no producción ejecutada.", falta_doc="Contacto, envío y recepción de la cotización, paquete, fecha y anticipo"),
 "prospeccion": dict(clasif="Parcial; dirección comercial propuesta.", falta_doc="Evidencia de contactos humanos, respuestas, diagnósticos y resultados"),
 "chacha": dict(clasif="Proyecto interno en desarrollo.", falta_doc="Pipeline, validación de prompts y OpenClaw, y caso terminado"),
 "frutisa": dict(clasif="Cliente; branding avanzado.", falta_doc="Packaging, sitio, campañas, POP y animaciones"),
 "shakti": dict(clasif="Cliente; desarrollo pendiente.", falta_doc="Desarrollo, móvil, SEO, CMS, automatizaciones y confirmación de publicación"),
 "uroboros": dict(clasif="Proyecto interno y sitio público estático.", falta_doc="Distinguir local, preparado, publicado y verificado; QA en vivo, conversión, analítica y CMS"),
 "marca": dict(clasif="Sistema de marca activo.", falta_doc=""),
}
for p in proyectos:
    p.setdefault("clasif", ""); p.setdefault("pregunta", "")
    p.update(INV.get(p["id"], {}))
    if p["id"] in INV and "Investigación de cobertura" not in p["fuente"]:
        p["fuente"] += " · Investigación de cobertura (28 oct)"

# KOBOS 28 oct 17:16: nuevas fichas (matriz de cobertura del Registro histórico, 23 de 23 con ficha)
K = "KOBOS 28 oct (17:16)"
KOB = {
 "okame": dict(ficha="Parcial", presencia="Caso publicado en latticce.com/book; respaldo de proyecto en KOBOS, permisos por asset pendientes", clasif="Respaldo de proyecto en KOBOS (identidad de uñas press on y Beauty Studio); no es cliente activo.", accion_doc="Confirmar contacto autorizado, fecha y alcance, y qué assets pueden mostrarse.",
   falta_doc="Contacto autorizado, fecha y alcance de la relación, derechos de uso por asset", pregunta="¿Quién es el contacto autorizado de OKAME y qué assets se pueden mostrar?"),
 "jeremy": dict(ficha="Sí", clasif="Registro histórico: proyecto digital en SITE123 (niveles, videoteca, audioteca y podcast); no es relación vigente.", accion_doc="Confirmar entidad, permiso, activos y estado final.",
   falta_doc="Entidad o representante, alcance, activos, estado final y autorización"),
 "cvp": dict(ficha="Sí", tipo="Proyecto interno", estado="En desarrollo", clasif="Proyecto editorial interno de Dirección y laboratorio de contenido, RRSS y Ads para Agency; no es cliente.",
   accion_doc="Inventario de piezas, canales autorizados y resultados verificables.", falta_doc="Inventario de piezas, canales autorizados, responsable, calendario y tablero de resultados", pregunta=""),
 "floripondios": dict(ficha="Sí", estado="En desarrollo", nodo="Films", clasif="Proyecto autoral multinodo (Films, Studio, Sound) en postproducción pendiente.", accion_doc="Completar revisión, musicalización, créditos, master y permisos.",
   falta_doc="Revisión, musicalización, créditos, master aprobado, derechos y decisión de difusión", pregunta="¿Cuándo es la sesión de revisión y quién aprueba créditos y master?"),
 "conciertos": dict(ficha="Sí", accion_doc="Crear índice de casos y activos, permisos y oferta vigente.", falta_doc="Índice de trabajos atribuibles, permisos, oferta vigente y seguimiento por artista"),
 "videoclips": dict(ficha="Sí", accion_doc="Cubierto en la ficha Studio Music: casos y producto.", falta_doc="Casos atribuibles, permisos, oferta vigente y seguimiento por artista"),
 "bodas": dict(ficha="Sí", accion_doc="Mantener expediente por evento y validar alianzas y permisos.", falta_doc="Expediente por evento, permisos, entregables, respaldo, testimonio y aliados confirmados"),
 "abyali": dict(ficha="Sí", nodo="Time", clasif="Cobertura 360 en Jilotepec, entregada; surgió de un servicio de OKAME. Permiso pendiente.", accion_doc="Confirmar fecha, másteres, respaldo y permiso de difusión.",
   falta_doc="Fechas exactas, másteres y respaldo, testimonio archivado y permiso de difusión", pregunta="¿Cuáles fueron las fechas exactas y hay permiso escrito para Book y reel?"),
 "food": dict(ficha="Sí", accion_doc="Confirmar entidad y permiso, materiales y estado de archivos.", falta_doc="Entidad y permiso, materiales disponibles y estado de los archivos"),
 "rodadas": dict(ficha="Sí", accion_doc="Completar alcance, costos, casos y permisos de vuelo.", falta_doc="Alcance y exclusiones vigentes, costo y margen, casos y permisos de vuelo"),
 "somekicks": dict(ficha="Sí", nodo="Agency", inicio="2026-09-08", clasif="Prospecto de sneakers y streetwear con diagnóstico (corte 8 sep) y propuestas de difusión; sin contratación.",
   accion_doc="Confirmar contacto autorizado, interés y alcance antes de activar difusión.", falta_doc="Contacto autorizado, propuesta aceptada, productos activos y reglas de operación",
   pregunta="¿Quién es el contacto autorizado de Somekicks y aceptó alguna de las propuestas?"),
 "gps": dict(ficha="Sí", inicio="2026-09-29", clasif="Prospecto de monitoreo para unos 50 vehículos; sería desarrollo a medida, no app existente. Cita sin concretar.",
   accion_doc="Confirmar cita, entidad, alcance y viabilidad.", falta_doc="Cita, entidad y contacto, alcance, viabilidad y presupuesto"),
 "tennis": dict(ficha="Sí", clasif="Posible venta cruzada Studio → Agency detectada por Hernán; por calificar.", accion_doc="Identificar entidad y contacto y calificar antes de contactar.",
   falta_doc="Entidad, persona autorizada, problema, canal, urgencia y presupuesto"),
 "mol3": dict(ficha="Sí", clasif="Piloto interno de Agency sobre Eleventa para operar tiendas; Daniel desarrolla la lógica.", accion_doc="Definir tiendas piloto, pruebas y controles antes de usar datos reales.",
   falta_doc="Tiendas piloto y responsables, alcance, seguridad, pruebas, versiones y acuerdo", pregunta="¿Qué tiendas y responsables participarán en el piloto y cuándo es la prueba?"),
 "calculadora": dict(ficha="Sí", nombre="Tabulador / calculadora", clasif="Herramienta interna en Documents/Codex/TABULADOR (Studio, paquetes, renta de equipo y horas); no sustituye cotización final.",
   accion_doc="Registrar URL o commit, responsable, manual y casos de prueba.", falta_doc="URL o commit canónico, responsable de cambios, manual y casos de prueba",
   pregunta="¿Cuál es la versión canónica en GitHub y quién aprueba cambios?"),
 "oraculo": dict(ficha="Sí", accion_doc="Crear inventario de piezas, archivos y estado de envío o publicación.", falta_doc="Índice de piezas, archivos, fechas, canal y estado de envío"),
}
for p in proyectos:
    if p["id"] in KOB:
        p.update(KOB[p["id"]])
        if K not in p["fuente"]:
            p["fuente"] += " · " + K

# Respuestas de Dirección (EMM, dictado 28 oct 18:14). avance_est = estimación cualitativa (aprox.) cuando no hay entregables contados.
D = "Dirección (EMM), 28 oct"
EMM = {
 "okame": dict(estado="Cerrado", inicio="2025-11-01", inicio_q="aprox", etapa="2025", avance_est=1.0, c_publico=True, c_comercial=True, c_permiso=True,
   clasif="Identidad para Nails + Beauty Studio. Cliente: Jacqueline. Responsable: Emanuel; diseño: Rafael. De nov 2025 a may 2026 (aprox.), con revisiones extendidas por falta de seguimiento del cliente.",
   presencia="Assets mostrables publicados en latticce.com/book y usados en brochures", falta_doc="Testimonio o permiso escrito archivado", pregunta="",
   limite="Mostrar solo los assets ya publicados.", siguiente="Archivar el permiso de uso y, si se puede, un testimonio de Jacqueline."),
 "jeremy": dict(estado="Cerrado", nodo="Agency", inicio="2026-05-15", inicio_q="aprox", avance_est=1.0, c_permiso=True,
   clasif="Sitio educativo para Jeremy (Coacalco, Edo. Méx.; atiende en remoto). Entidad: LATTICCE Agency. Responsable: Emanuel, trato directo por videollamada. Iniciado may–jun 2026 y terminado a inicios de agosto (aprox.). Entregado completo.",
   falta_doc="Confirmar por escrito el permiso de publicación", pregunta="", siguiente="Publicar el caso en el Book con el permiso confirmado."),
 "cvp": dict(inicio="2023-01-01", inicio_q="aprox", avance_est=0.35,
   clasif="Proyecto editorial de Dirección que viene desde 2023 (aprox.) y se retomó hace unos 3 meses. Laboratorio de contenido, RRSS y Ads para Agency."),
 "floripondios": dict(avance_est=0.6, clasif="Proyecto autoral multinodo. Emanuel aprueba créditos, master y diseño sonoro final. Sin fecha de revisión.",
   pregunta="", siguiente="Meta de cierre de año: cerrar el sonido de Floripondios y empezar los créditos.", falta_doc="Fecha de revisión, musicalización, créditos y master"),
 "somekicks": dict(nombre="Somekicks (tenis)", nodos="Agency, Studio", avance_est=0.2,
   clasif="Prospecto de sneakers y streetwear (absorbe el frente Tennis: es la misma necesidad). Contacto: Hernán, a través de su compañero interesado. Emanuel atiende o pasa la información a Daniel.",
   pregunta="", siguiente="Que Hernán confirme interés y propuesta; Emanuel atiende o deriva a Daniel.", falta_doc="Propuesta aceptada, productos activos y reglas de operación"),
 "calculadora": dict(clasif="Tabulador en GitHub (latticcea-git/tabulador; último commit local 23 ago 2026). Emanuel hace y aprueba los cambios; Daniel revisa que no falte nada.",
   links=[{"label": "Repositorio en GitHub", "url": "https://github.com/latticcea-git/tabulador", "publico": False}], avance_est=0.7, pregunta="",
   falta_doc="Manual y casos de prueba"),
 "mol3": dict(inicio="2026-09-28", inicio_q="aprox", avance_est=0.25, clasif="Piloto interno de Agency sobre Eleventa; Daniel desarrolla y maneja permisos. Iniciado hace un mes (aprox.).",
   pregunta="", siguiente="Probar en Abarrotes Paulita cuando el software esté terminado en lo conceptual y lo práctico.", falta_doc="Fecha de prueba y resultados"),
 "rodadas": dict(estado="Perdido", avance_est=1.0, clasif="Prospecto perdido por falta de seguimiento. Dejó paquetes de 360 y dron con imágenes de apoyo hechas con IA y una respuesta comercial lista.",
   siguiente="Reusar los paquetes en la siguiente oportunidad de automovilismo."),
 "retrato": dict(avance_est=0.55, clasif="Servicio probado que Hernán trabaja en Instagram y con piezas en el sitio. Falta describirlo, cerrarlo y crear su material de ventas.",
   falta_doc="Descripción del servicio, material de ventas y ficha", siguiente="Describir y cerrar la oferta de Retrato Express con su material de ventas."),
 "videoclips": dict(avance_est=0.75, siguiente="Distribuir y usar el material de ventas que ya existe."),
 "bodas": dict(avance_est=0.6, siguiente="Prospectar y usar el material que ya existe; abrir el servicio Bodas en 360."),
 "abyali": dict(estado="Cerrado", avance_est=1.0, clasif="Cerrado: caso de cliente satisfecho y base del servicio especializado Bodas en 360.", pregunta="",
   siguiente="Usarlo como caso de éxito para crear Bodas en 360."),
 "food": dict(estado="Producto construido", avance_est=0.75, clasif="Due Fratelli hecho y micrometa avanzada: ya se puede vender a restaurantes con lo que se hace hoy.",
   definido="Due Fratelli (food styling y food film); CRM Food con 50 restaurantes y cafeterías en 5 zonas (Coacalco, Tultepec, Tultitlán, Ecatepec, GAM), todos en estado Nuevo (15 oct)",
   siguiente="Contactar en tandas de 3 a los 50 prospectos del CRM Food y registrar respuestas.", falta_doc="Contactos registrados y respuestas"),
 "gps": dict(estado="En pausa", avance_est=0.15, clasif="Prospecto parado: sin respuesta.", siguiente="Retomar solo si responde."),
 "kobos": dict(avance_est=0.8, clasif="Lo maneja Emanuel por completo; avance constante conforme se genera información."),
 "cloudex": dict(avance_est=0.6, clasif="Lo maneja Emanuel; avance constante."),
 "sinttergia": dict(falta_doc="Descripción completa del proyecto (Emanuel la enviará; está en COBOS)"),
 "oraculo": dict(falta_doc="Información de Dirección por recibir", avance_est=0.5),
 "deshii": dict(estado="Cerrado", avance_est=0.8, clasif="Cliente cerrado y colaborador cercano: deja vender en su tienda y se le apoya con etiquetas. Sirve como caso de éxito y para experimentar."),
 "soma": dict(estado="Cerrado", avance_est=1.0, clasif="Cerrado: logotipo e imagen de marca entregados. Se reabre solo si lo buscan."),
 "conciertos": dict(avance_est=0.6, clasif="Avanza de forma constante; lo maneja Hernán. Busca actividad en redes, acreditar la fotografía y acercar contactos."),
 "seferan": dict(estado="Perdido", avance_est=1.0, clasif="Perdido. Sirvió para trabajar con un vendedor externo a porcentaje del proyecto."),
 "prospeccion": dict(avance_est=0.4, clasif="Continúa; la maneja Emanuel y se delegará poco a poco."),
 "chacha": dict(avance_est=0.4, clasif="Protocolo para automatizar sitios esenciales y sencillos; los complejos se hacen con Codex o Claude."),
 "frutisa": dict(estado="Cerrado", clasif="Cerrado salvo nuevas solicitudes."),
 "shakti": dict(clasif="Cliente activo con paquete mensual de redes. En 2027: replantear el paquete y terminar el sitio en desarrollo."),
 "uroboros": dict(estado="Activo", avance_est=0.85, clasif="Sitio cerrado; solo se actualizan partes. A Sound le falta diseño y casos. Meta: reemplazar imágenes de IA y casos internos por casos reales comprobables."),
}
for p in proyectos:
    if p["id"] in EMM:
        p.update(EMM[p["id"]])
        if D not in p["fuente"]:
            p["fuente"] += " · " + D
proyectos = [p for p in proyectos if p["id"] != "tennis"]
for p in proyectos:
    p.setdefault("avance_est", None)

# Respuestas de Dirección (EMM, dictado 29 oct) + KOBOS 29 oct (Shakti, SINTTERGIA). Permiso: Dirección confirma permiso de uso y muestra
# de todo lo hecho hasta hoy; si algo no es utilizable, Dirección lo marcará. Testimonios: borradores redactados por LATTICCE, por aprobar con cada cliente.
D2 = "Dirección (EMM), 29 oct"
TESTIMONIO = {
 "frutisa": "LATTICCE le dio a Frutisa un personaje y una imagen que por fin se sienten nuestros. Entendieron la marca antes de diseñarla.",
 "shakti": "LATTICCE acompaña a Shakti mes con mes: nuestras redes tienen ritmo y la marca se ve como se siente el estudio.",
 "deshii": "Las etiquetas que hizo LATTICCE hacen que nuestros productos se vean tan cuidados como los hacemos.",
 "soma": "LATTICCE tradujo la idea de SOMA en un logotipo y una imagen claros, listos para usarse.",
 "okame": "Con LATTICCE, OKAME pasó de tener un nombre a tener una marca: cada aplicación se ve profesional y coherente.",
 "jeremy": "LATTICCE convirtió mis clases en un sitio claro y fácil de usar; mis alumnos encuentran todo en un solo lugar.",
 "abyali": "El 360 de LATTICCE les dio a nuestros invitados un recuerdo distinto de la boda, y nosotros no tuvimos que preocuparnos por nada.",
}
EMM2 = {
 "oraculo": dict(ficha="Sí", c_publico=False, c_contenido=True, c_comercial=False, c_cruce=True,
   clasif="Grupo de WhatsApp de la comunidad SINTTERGIA con unas 61 personas. Emanuel envía a diario contenido derivado de SINTTERGIA (arquetipos y textos). No se vende: mantiene activa a la comunidad y la hace crecer como punta de lanza; la meta a futuro son cursos. Según KOBOS (29 oct) es el grupo con más actividad reciente y respuesta.",
   presencia="Grupo privado de WhatsApp (no es página pública)", falta_doc="Fecha de inicio del grupo e índice de piezas enviadas (fecha, lectura, imagen y envío)",
   siguiente="Crear el índice de piezas antes de automatizar y medir respuesta por envío.", pregunta=""),
 "sinttergia": dict(inicio="2026-01-01", inicio_q="aprox", c_publico=True, c_contenido=True, c_comercial=False, c_cruce=True,
   clasif="Comunidad de práctica creativa multidisciplinaria, «Formación en acción»; no es nodo comercial de LATTICCE. Inicio aprox. enero 2026 (Dirección); comunidad de WhatsApp creada el 10 abr 2026 con 94 miembros y 12 grupos (KOBOS, 29 oct). Instagram con 14 publicaciones y 38 seguidores; Facebook con 16. Meta 1–28 oct: 5 visualizaciones y 0 interacciones (línea base).",
   presencia="Sección Comunidad en latticce.com, Instagram y Facebook de SINTTERGIA",
   links=[{"label": "Instagram @sinttergia____lattentte", "url": "https://www.instagram.com/sinttergia____lattentte/", "publico": True},
          {"label": "Facebook Sinttergia Lattentte", "url": "https://www.facebook.com/profile.php?id=61589840495010", "publico": True}],
   falta_doc="Núcleo de 3–5 personas constantes comprobado, agenda de sesiones y registro por grupo",
   limite="Mantenerla separada de las comunicaciones comerciales de LATTICCE; 94 miembros no equivalen a participación sostenida.",
   siguiente="Durante 4 semanas registrar por grupo publicaciones, participantes, respuestas y asistencia a una sesión fija.", pregunta=""),
 "rodadas": dict(inicio="2026-08-01", inicio_q="aprox", c_publico=False, c_contenido=False, c_comercial=False, c_cruce=False,
   clasif="Prospecto perdido (inicio aprox. agosto 2026): 4 carteles con precios para fotografía y video de una rodada en Coacalco. Se enviaron al prospecto y ahí terminó.",
   siguiente="Ninguna: prospecto cerrado."),
 "cvp": dict(c_cruce=True, clasif="Proyecto propio que viene desde 2023 (aprox.) y se retomó hace unos 3 meses: imágenes y videos de servicios locales para mantenernos activos. Funciona como frente comercial y laboratorio de contenido, RRSS y Ads para Agency."),
 "retrato": dict(c_comercial=True, presencia="Material usado en latticce.com e Instagram", falta_doc="Expediente en KOBOS (Dirección lo solicitará), descripción del servicio y material de ventas"),
 "deshii": dict(c_contenido=False, c_comercial=False,
   clasif="Cliente cerrado y colaborador cercano: deja vender en su tienda. Se hizo el contenido de sus etiquetas, ya entregado y usado solo para impresión. Sirve como caso de éxito y para experimentar."),
 "soma": dict(c_contenido=False, c_comercial=False,
   clasif="Cerrado: logotipo e imagen de marca hechos por Emanuel. Sin contenido derivado ni testimonio del cliente. OPORTUNIDAD SIN EXPLOTAR: el material no se ha usado comercialmente.",
   siguiente="Destacado: convertir el logo e imagen de SOMA en caso del Book y del brochure de Design.", limite="Cerrado: mostrar el logotipo y la imagen entregados; manual, redes y sitio quedaron fuera del cierre."),
 "jeremy": dict(clasif="Sitio educativo para Jeremy (Coacalco, Edo. Méx.; atiende en remoto). Entidad: LATTICCE Agency. Responsable: Emanuel, trato directo por videollamada. Iniciado may–jun 2026 y entregado completo a inicios de agosto (aprox.). Cerrado sin continuidad.",
   falta_doc="", siguiente="Publicar el caso en el Book."),
 "shakti": dict(ficha="Sí",
   clasif="Cliente activo con paquete mensual de redes. Sitio one-page implementado (hero, galería, 8 prácticas, horarios, ubicación, CTAs de WhatsApp; QA en escritorio y móvil), publicado el 11 oct en GitHub Pages; falta validación final del cliente. Perfil y portada de Facebook preparados, no publicados. Primer gran caso de CHACHA APP. En 2027: replantear el paquete y terminar el sitio.",
   links=[{"label": "Sitio (publicación del 11 oct, por revalidar)", "url": "https://latticcea-git.github.io/shakti-yoga-estudio/", "publico": True}],
   falta_doc="Validación con el cliente: datos del negocio, fotos y video reales, autorización de redes",
   limite="Las imágenes de IA del sitio son conceptuales: no presentarlas como el estudio, sus clases o su alumnado.",
   siguiente="Sesión de validación con Shakti; después revalidar el sitio en vivo y sustituir imágenes conceptuales por material real."),
}
for p in proyectos:
    upd = EMM2.get(p["id"])
    if upd:
        p.update(upd)
    p["c_permiso"] = True
    p["testimonio"] = TESTIMONIO.get(p["id"], "")
    if (upd or p["id"] in TESTIMONIO) and D2 not in p["fuente"]:
        p["fuente"] += " · " + D2
    if p["id"] in ("shakti", "sinttergia") and "KOBOS 29 oct" not in p["fuente"]:
        p["fuente"] += " · KOBOS 29 oct"

# Contenido derivado publicado, revisado contra latticce.com (Book, blog y páginas de Agency en el código de UROBOROS, 29 oct):
# cuenta si LATTICCE publicó al menos una pieza propia sobre el frente.
WEB = "latticce.com (Book, blog y Agency), 29 oct"
CONT = {"frutisa": True, "shakti": True, "okame": True, "jeremy": True, "cvp": False, "floripondios": False, "abyali": False}
for p in proyectos:
    if p["id"] in CONT:
        p["c_contenido"] = CONT[p["id"]]
        if WEB not in p["fuente"]:
            p["fuente"] += " · " + WEB
    if p["id"] in ("shakti", "jeremy"):
        p["c_comercial"] = True
    if p["id"] == "shakti" and not any("book/shakti" in l["url"] for l in p["links"]):
        p["links"] = [{"label": "Caso en el Book", "url": "https://latticce.com/book/shakti-yoga-estudio/", "publico": True}] + p["links"]
        p["presencia"] = "Caso en el Book de latticce.com y mención en las páginas de servicios de Agency"
    if p["id"] == "jeremy":
        p["presencia"] = "Caso en el Book de latticce.com y mención en las páginas de servicios de Agency"
    if p["id"] == "abyali":
        p["falta_doc"] = "Caso propio en el Book (las bodas publicadas no lo identifican como Aby y Ali)"

# Oportunidad de contenido (Dirección, 29 oct): frentes sin contenido derivado publicado → qué se puede hacer con lo que ya existe.
SUG = {
 "cvp": ["Serie semanal en Instagram: un negocio local por semana (foto + reel de 15 s con su historia)",
         "Carrusel «detrás de la toma» con el proceso de una sesión de CVP",
         "Caso en el Book como laboratorio de Agency: qué se probó y qué se aprendió"],
 "floripondios": ["Teaser de 15 s con un fragmento del diseño sonoro",
                  "Carrusel del proceso de mezcla y diseño sonoro (le da a Sound el caso que le falta)",
                  "Caso en el Book de Sound/Films al cerrar el sonido y los créditos"],
 "deshii": ["Caso en el Book de Design: sistema de etiquetas, de la propuesta a la impresión",
            "Reel del producto con su etiqueta en la tienda",
            "Carrusel educativo: «Cómo diseñar una etiqueta que se imprime bien»"],
 "soma": ["Caso en el Book de Design: moodboard → variantes del logotipo → aplicaciones",
          "Carrusel del proceso de identidad para Instagram de Design",
          "Lámina en el brochure de Design"],
 "abyali": ["Caso «Bodas en 360» en el Book de Time con el video 360 de la boda",
            "Reel corto de la experiencia 360 de los invitados",
            "Artículo en el blog: «Qué aporta una cámara 360 a una boda»"],
}
for p in proyectos:
    p["sug_contenido"] = SUG.get(p["id"], [])

# Tabulador LATTICCE (KOBOS 02 Operacion/Tabulador LATTICCE.md, 29 oct 19:16)
for p in proyectos:
    if p["id"] == "calculadora":
        p.update(nombre="Tabulador LATTICCE · Cotizador Latente", nodo="LATTICCE", nodos="Studio, Sound, Design, Agency, Time",
          clasif="Herramienta interna que convierte horas, costos, presupuestos, paquetes y rentas en precotizaciones revisables (MXN, IVA 16 % separado). Cuatro módulos: Horas, Cotizador multinodo (Studio, Sound, Design, Agency y Time), Paquetes (Esencial, Classic, Deluxe, Cinematic) y Renta de equipo o espacio. Versión estable v1.3.0 (23 ago); commit verificado 31dde0c; compila y pasa 4/4 pruebas de render (29 oct). La skill Cotizador Latente permite pedir una precotización en lenguaje natural. Emanuel cambia y aprueba; Daniel revisa.",
          definido="Horas: precio por hora, total y plan desde presupuesto; Cotizador multinodo con honorarios, comisión y reserva protegidos; Paquetes Esencial, Classic, Deluxe y Cinematic por servicio; Renta de equipo o espacio con depósito y logística; Exportación a PDF, Markdown y CSV; Skill Cotizador Latente; Compilación y 4/4 pruebas de render",
          pendiente="Confirmar URL y estado de despliegue; Validar precios y cambiar ceros técnicos por «por confirmar»; Probar Cotizador Latente con casos reales de cada nodo y renta; Nombrar responsables y frecuencia de actualización de catálogos; Definir modelo de datos y flujo de prospecto para la versión pública",
          def_n=7, pend_n=5, avance_est=None, c_cruce=True,
          pruebas=["Repositorio latticcea-git/tabulador · v1.3.0 · commit 31dde0c", "Ramas develop, preview y main alineadas (29 oct)", "4/4 pruebas de render aprobadas (29 oct)", "Skill cotizador-latente instalada y verificada"],
          limite="Precotización interna: no es cotización final, contrato ni política comercial. Honorarios 20 %, comisión 5 % y reserva 5 % son supuestos operativos. No exponer márgenes ni costos.",
          siguiente="Gobernanza interna: validar precios y catálogos, cambiar ceros por «por confirmar» y probar Cotizador Latente con un caso real por nodo. Después, prototipo privado del cotizador público por nodo (/cotizar/studio, /sound, /design, /agency, /time, /renta).",
          falta_doc="URL de despliegue confirmada", accion_doc="Ficha completa al 29 oct (módulos, reglas, historial, skill y crecimiento propuesto).")
        if "KOBOS 29 oct" not in p["fuente"]:
            p["fuente"] += " · KOBOS 29 oct (Tabulador LATTICCE)"

CAPF = {"Producción audiovisual": "Parcial", "360": "Parcial", "Sound": "Sí", "Producción musical": "Sí", "Postproducción especializada": "No",
        "Software / QA": "Parcial", "Diseño": "Parcial", "Producción física": "Sí", "Ventas / prospección": "Parcial"}
for c in capacidad:
    c["ficha"] = CAPF.get(c["area"])
capacidad.append({"area": "Cotización", "relacion": "Calculadora interna para estimar con criterio común", "estado": "Herramienta interna; no sustituye aprobación humana", "ficha": "Sí"})

for e in etapas:
    if e["id"] == "val":
        e["cadena"] = "Mercado elegido → prospecto verificable → contacto humano → conversación → diagnóstico → propuesta → cierre/anticipo → producción → cobro → caso/testimonio → venta cruzada → aprendizaje"
    if e["id"] == "oct":
        e["cadena"] = "LATTICCE OS → UROBOROS → Codex → Claude → COBOS → CLOUDEX → equipo → agentes → documentación"

hitos += [
  H("2026-04-01", "aprox", "Marca", "Time", "Gorras y etiquetas LATTICCE en la primera boda", "Primera identidad física de campo: gorras y aplicaciones con serigrafía y corte. No es línea textil validada.", "KOBOS · Registro histórico 2025–2026", proyecto="bodas"),
  H("2026-10-28", "exacta", "Sistema", "LATTICCE", "Registro histórico 2025–2026 y matriz de cobertura", "23 frentes revisados: 7 con ficha propia, 3 parciales y 13 sin ficha; prioridad Aby y Ali, Floripondios, MOL3, Tennis, GPS, Home Studio, calculadora y red.", "KOBOS · 90 Fuentes/Registro histórico", proyecto="kobos"),
  H("2026-08-16", "exacta", "Sistema", "LATTICCE", "Tabulador v1.1.0: Paquetes y temas por nodo", "Se suman los paquetes Esencial, Classic, Deluxe y Cinematic por servicio.", "latticcea-git/tabulador · cf82c46", proyecto="calculadora"),
  H("2026-08-23", "exacta", "Sistema", "LATTICCE", "Tabulador v1.3.0: presupuesto, paquetes y renta de espacio", "Amplía presupuesto, paquetes y renta, incluida la renta de espacio. Versión estable vigente.", "latticcea-git/tabulador · 595b854", proyecto="calculadora"),
  H("2026-10-29", "exacta", "Sistema", "LATTICCE", "Tabulador verificado y skill Cotizador Latente", "Compila y pasa 4/4 pruebas de render; la skill Cotizador Latente precotiza en lenguaje natural. Ficha completa en KOBOS.", "KOBOS · 02 Operacion/Tabulador LATTICCE", proyecto="calculadora"),
  H("2026-10-28", "exacta", "Sistema", "LATTICCE", "Expedientes completados en KOBOS", "La matriz de cobertura pasa a 23 de 23 frentes con ficha: Floripondios, Aby y Ali 360, MOL3, GPS, Tennis, Somekicks, Home Studio, Tabulador, Rex y Ángel/ADN, entre otros. OKAME queda con respaldo de proyecto.", "KOBOS · 90 Fuentes/Registro histórico (17:16)", proyecto="kobos"),
]
hitos.sort(key=lambda h: h["fecha"])

redes = [
  dict(nodo="Studio", cuenta="LATTICCE Studio", ig="@___latticce___", url_ig="https://www.instagram.com/___latticce___/", fb="LATTICCE Studio", url_fb="https://www.facebook.com/profile.php?id=61594764417597",
       metricool="No conectado", meta="Página visible", vis=35578, vis_ig=35427, vis_fb=151, alcance_ig=8100, interacciones=2500, seg_nuevos=40, conversaciones=0, redondeo=True),
  dict(nodo="Design", cuenta="LATTICCE Design", ig="@latticce.design", url_ig="https://www.instagram.com/latticce.design/", fb="LATTICCE Design", url_fb="https://www.facebook.com/profile.php?id=61589128948498",
       metricool="Conectado (27 oct)", meta="Página visible", vis=587, vis_ig=569, vis_fb=18, alcance_ig=200, interacciones=37, seg_nuevos=None, conversaciones=0, redondeo=False),
  dict(nodo="Sound", cuenta="LATTICCE Sound", ig="@latticce.sound", url_ig="https://www.instagram.com/latticce.sound/", fb="LATTICCE Sound", url_fb="https://www.facebook.com/profile.php?id=61588752884212",
       metricool="No conectado", meta="Página visible", vis=525, vis_ig=462, vis_fb=63, alcance_ig=53, interacciones=13, seg_nuevos=None, conversaciones=0, redondeo=False),
  dict(nodo="Food", cuenta="LATTICCE Food (línea de Studio)", ig="@latticce_food", url_ig="https://www.instagram.com/latticce_food/", fb="Latticce Food", url_fb="https://www.facebook.com/1354749881057565",
       metricool="No conectado", meta="Página visible", vis=485, vis_ig=457, vis_fb=28, alcance_ig=209, interacciones=48, seg_nuevos=None, conversaciones=0, redondeo=False),
  dict(nodo="Agency", cuenta="LATTICCE Agency", ig="@latticce.agency", url_ig="https://www.instagram.com/latticce.agency/", fb="LATTICCE Agency", url_fb="https://www.facebook.com/profile.php?id=61589054697841",
       metricool="No conectado", meta="Página visible", vis=310, vis_ig=310, vis_fb=0, alcance_ig=14, interacciones=14, seg_nuevos=None, conversaciones=0, redondeo=False),
  dict(nodo="Time", cuenta="LATTICCE Time", ig="@latticce.time", url_ig="https://www.instagram.com/latticce.time/", fb=None, url_fb=None,
       metricool="No conectado", meta="Sin página", vis=None, vis_ig=None, vis_fb=None, alcance_ig=None, interacciones=None, seg_nuevos=None, conversaciones=None, redondeo=False),
  dict(nodo="Films", cuenta="LATTICCE Films", ig="@latticce.films", url_ig="https://www.instagram.com/latticce.films/", fb="LATTICCE Films", url_fb="https://www.facebook.com/latticce.films",
       metricool="No conectado", meta="No visible en la cuenta", vis=None, vis_ig=None, vis_fb=None, alcance_ig=None, interacciones=None, seg_nuevos=None, conversaciones=None, redondeo=False),
]

rumbo = [
  dict(nodo="LATTICCE", rol="Núcleo", foco="Corte ejecutivo del 10 de diciembre y kit de ventas mínimo.",
       proximo="Kit de ventas mínimo (3–9 nov); CRM con estados; Corte semanal de una página; Corte ejecutivo (10 dic)"),
  dict(nodo="Studio", rol="Puerta comercial", foco="Imagen y video para artistas y marcas.",
       proximo="Bloques de videoclip y Retrato Express en el sitio; Prospectos de videoclip en tandas de 3; Ficha de producto Studio Music; Expediente de Aby y Ali 360"),
  dict(nodo="Sound", rol="Puerta comercial", foco="Producción, grabación y sonido para proyectos musicales.",
       proximo="Ficha del Home Studio; Ficha de Floripondios con créditos; Primeras conversaciones de producción musical"),
  dict(nodo="Design", rol="Puerta comercial", foco="Identidad visual para negocios que quieren profesionalizarse.",
       proximo="Seguimiento de Misión 001 (Querétaro); Manual de marca de SOMA; Caso Frutisa completo"),
  dict(nodo="Agency", rol="Puerta comercial", foco="Experiencias digitales: UI/UX, tecnología y producto.",
       proximo="Terminar el desarrollo de Shakti; Caso piloto de CHACHA (Frutisa); Fichas de Somekicks, GPS y MOL3"),
  dict(nodo="Time", rol="Posicionamiento", foco="Memorias de bodas y XV años.",
       proximo="Book y PDF para parejas y recomendadores; Expediente por evento"),
  dict(nodo="Films", rol="Posicionamiento", foco="Narrativa cinematográfica, en desarrollo.",
       proximo="Decidir si Floripondios es pieza de Films; Página de cinema con piezas propias"),
]

for name, data in [("proyectos", proyectos), ("book", book), ("blog", blog), ("etapas", etapas), ("madurez", madurez), ("nodos", nodos), ("capacidad", capacidad), ("hitos", hitos), ("redes", redes), ("rumbo", rumbo)]:
    json.dump(data, open(os.path.join(OUT, name + ".json"), "w"), ensure_ascii=False, indent=1)
    print(name, len(data), os.path.getsize(os.path.join(OUT, name + ".json")))
