
import streamlit as st

# -----------------------------------------
# CONFIGURACIÓN
# -----------------------------------------

st.set_page_config(
    page_title="Entre Líneas",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# ESTILOS
# -----------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #fff8fd 0%, #f5efff 55%, #fff2f8 100%);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #42245f, #70458c);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    background: linear-gradient(120deg, #633b83, #a46bb5, #df9cbd);
    padding: 48px 35px;
    border-radius: 25px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    font-size: 17px;
}

.section-title {
    color: #633b83;
    font-size: 29px;
    font-weight: 800;
    margin-top: 15px;
}

.subtitle {
    color: #795c89;
    font-size: 16px;
}

.info-card {
    background: white;
    padding: 23px;
    border-radius: 18px;
    border: 1px solid #eadcf1;
    box-shadow: 0 8px 28px rgba(75,48,105,.09);
    margin-bottom: 15px;
    color: #493657;
}

.info-card h3 {
    color: #70458c;
    margin-top: 0;
}

.quote {
    background: #f0e5f7;
    padding: 20px;
    border-left: 5px solid #a46bb5;
    border-radius: 12px;
    color: #543b68;
    font-style: italic;
    margin: 18px 0;
}

.stButton button {
    background: linear-gradient(100deg, #70458c, #b47ab8);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 9px 20px;
    font-weight: 600;
}

.stButton button:hover {
    background: #57346f;
    color: white;
    border: none;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #eadcf1;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# DATOS Y ESTADO DE LA APLICACIÓN
# -----------------------------------------

if "stories_pending" not in st.session_state:
    st.session_state.stories_pending = []

if "stories_public" not in st.session_state:
    st.session_state.stories_public = []

if "videos" not in st.session_state:
    st.session_state.videos = []

if "quiz_answer" not in st.session_state:
    st.session_state.quiz_answer = None


# -----------------------------------------
# FUNCIONES
# -----------------------------------------

def title(text, description=None):
    st.markdown(
        f'<div class="section-title">{text}</div>',
        unsafe_allow_html=True
    )
    if description:
        st.markdown(
            f'<p class="subtitle">{description}</p>',
            unsafe_allow_html=True
        )


def card(heading, content):
    st.markdown(
        f"""
        <div class="info-card">
            <h3>{heading}</h3>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def reflection(question):
    st.markdown(
        f'<div class="quote">💭 {question}</div>',
        unsafe_allow_html=True
    )


# -----------------------------------------
# MENÚ LATERAL
# -----------------------------------------

with st.sidebar:
    st.markdown("# 💜 Entre Líneas")
    st.caption("Escuchar también transforma")
    st.divider()

    page = st.radio(
        "NAVEGACIÓN",
        [
            "🏠 Inicio",
            "📱 Acoso y ciberacoso",
            "💗 Sexualidad y respeto",
            "🌱 Salud mental y bienestar",
            "🎥 Experiencias compartidas",
            "🎲 Zona interactiva",
            "🆘 Orientación y ayuda",
            "🔐 Administración"
        ],
        label_visibility="visible"
    )

    st.divider()
    st.caption("Un espacio para escuchar, comprender, aprender y expresarse.")


# -----------------------------------------
# INICIO
# -----------------------------------------

if page == "🏠 Inicio":

    st.markdown("""
    <div class="hero">
        <h1>Entre Líneas 💜</h1>
        <p><b>Un espacio para escuchar, comprender, aprender y expresarse.</b></p>
        <p>Hay experiencias que no siempre sabemos cómo contar.
        Aquí encontrarás información, reflexión y herramientas para
        reconocer situaciones que afectan nuestro bienestar.</p>
    </div>
    """, unsafe_allow_html=True)

    title("Bienvenidos a Entre Líneas")

    st.write("""
    Este espacio educativo busca promover el respeto, la empatía,
    el autocuidado y la convivencia. A través de información,
    experiencias y actividades interactivas, queremos generar
    conversaciones sobre situaciones que muchas veces permanecen
    en silencio.
    """)

    col1, col2 = st.columns(2)

    with col1:
        card(
            "📱 Acoso y ciberacoso",
            "Reconoce las diferentes formas de violencia, sus consecuencias "
            "y las maneras de actuar frente a ellas."
        )
        card(
            "🌱 Salud mental y bienestar",
            "Comprende la importancia de cuidar tus emociones, reconocer "
            "tus necesidades y buscar apoyo."
        )

    with col2:
        card(
            "💗 Sexualidad y respeto",
            "Aprende sobre consentimiento, límites personales, relaciones "
            "saludables y decisiones informadas."
        )
        card(
            "🎲 Zona interactiva",
            "Participa en dilemas, actividades y preguntas que te invitan "
            "a reflexionar sobre situaciones cotidianas."
        )

    st.markdown("""
    <div class="quote">
        "Escuchar también transforma. Comprender al otro es el primer
        paso para construir espacios más seguros."
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------
# ACOSO Y CIBERACOSO
# -----------------------------------------

elif page == "📱 Acoso y ciberacoso":

    title(
        "Acoso y ciberacoso",
        "Identificar la violencia es el primer paso para detenerla."
    )

    card(
        "¿Qué es el acoso?",
        "Es una conducta agresiva que puede repetirse en el tiempo y que "
        "implica un desequilibrio de poder. Puede manifestarse mediante "
        "insultos, amenazas, humillaciones, exclusión o agresiones físicas."
    )

    card(
        "¿Qué es el ciberacoso?",
        "Es una forma de agresión que ocurre mediante tecnologías digitales, "
        "como redes sociales, aplicaciones de mensajería, videojuegos "
        "o plataformas en línea."
    )

    title("Formas en las que puede manifestarse")

    card(
        "Insultos y humillaciones",
        "Comentarios ofensivos, burlas constantes o mensajes destinados "
        "a hacer sentir inferior a otra persona."
    )

    card(
        "Exclusión social",
        "Aislar intencionalmente a alguien de grupos, conversaciones "
        "o actividades para hacerlo sentir rechazado."
    )

    card(
        "Difusión de contenido privado",
        "Compartir fotografías, conversaciones o información personal "
        "sin autorización."
    )

    card(
        "Suplantación de identidad",
        "Crear perfiles falsos o utilizar la cuenta de otra persona "
        "para perjudicar su reputación."
    )

    title("Señales de alerta")

    st.markdown("""
    - Cambios repentinos en el estado de ánimo.
    - Miedo a revisar el celular o las redes sociales.
    - Aislamiento de amigos y familiares.
    - Pérdida de interés en actividades habituales.
    - Ansiedad antes de asistir a clases o participar en grupos.
    - Disminución del rendimiento académico.
    """)

    title("¿Qué consecuencias puede tener?")

    card(
        "Consecuencias emocionales",
        "Puede generar miedo, tristeza, ansiedad, inseguridad, vergüenza "
        "y pérdida de confianza."
    )

    card(
        "Consecuencias sociales y académicas",
        "Puede afectar las relaciones interpersonales, la participación "
        "en clase, la concentración y el sentido de pertenencia."
    )

    title("¿Qué podemos hacer?")

    st.markdown("""
    1. No responder con más agresiones.
    2. Guardar evidencias de los mensajes o publicaciones.
    3. Bloquear y reportar las cuentas responsables.
    4. Hablar con una persona de confianza.
    5. Informar a las autoridades de la institución cuando corresponda.
    6. Buscar acompañamiento psicológico si la situación está afectando
       el bienestar emocional.
    """)

    reflection(
        "¿Alguna vez has presenciado una situación de acoso y no has "
        "sabido cómo intervenir?"
    )

    title("Mitos y realidades")

    card(
        "Mito: 'Si es una broma, no puede ser acoso'.",
        "Realidad: Una broma deja de serlo cuando humilla, intimida "
        "o afecta a otra persona."
    )

    card(
        "Mito: 'El ciberacoso termina cuando se apaga el celular'.",
        "Realidad: El contenido digital puede permanecer disponible, "
        "compartirse y seguir afectando a la víctima."
    )


# -----------------------------------------
# SEXUALIDAD Y RESPETO
# -----------------------------------------

elif page == "💗 Sexualidad y respeto":

    title(
        "Sexualidad y respeto",
        "Conocer tus derechos también es una forma de cuidarte."
    )

    card(
        "¿Qué es la sexualidad?",
        "La sexualidad es una dimensión integral del ser humano. Incluye "
        "aspectos físicos, emocionales, afectivos, sociales y culturales. "
        "No se limita únicamente a las relaciones sexuales."
    )

    card(
        "¿Qué es el consentimiento?",
        "Es una decisión libre, voluntaria, informada y reversible. "
        "Todas las personas tienen derecho a decidir sobre su cuerpo "
        "y establecer sus propios límites."
    )

    title("Características del consentimiento")

    card(
        "Libre",
        "No debe existir presión, manipulación, amenaza o intimidación."
    )

    card(
        "Informado",
        "Las personas deben comprender qué están aceptando."
    )

    card(
        "Reversible",
        "Una persona puede cambiar de opinión en cualquier momento."
    )

    card(
        "Específico",
        "Aceptar una situación no significa aceptar todas las demás."
    )

    title("Relaciones saludables")

    st.markdown("""
    Una relación saludable se construye a partir de:

    - Respeto mutuo.
    - Comunicación honesta.
    - Confianza.
    - Libertad individual.
    - Reconocimiento de los límites.
    - Ausencia de control y manipulación.
    """)

    title("Señales de una relación poco saludable")

    card(
        "Control excesivo",
        "Exigir contraseñas, revisar conversaciones o controlar "
        "las amistades de la pareja."
    )

    card(
        "Manipulación emocional",
        "Hacer sentir culpable a alguien por expresar sus límites "
        "o tomar decisiones propias."
    )

    card(
        "Presión",
        "Insistir para que una persona haga algo que no desea."
    )

    reflection(
        "¿Por qué respetar los límites de otra persona también significa "
        "respetar su autonomía?"
    )


# -----------------------------------------
# SALUD MENTAL
# -----------------------------------------

elif page == "🌱 Salud mental y bienestar":

    title(
        "Salud mental y bienestar",
        "Cuidar lo que sentimos también es importante."
    )

    card(
        "¿Qué es la salud mental?",
        "Es un estado de bienestar que permite afrontar las situaciones "
        "de la vida, desarrollar habilidades, aprender, trabajar y "
        "participar en la comunidad. No significa sentirse feliz todo "
        "el tiempo."
    )

    title("Reconocer nuestras emociones")

    card(
        "Tristeza",
        "Puede aparecer ante una pérdida, una decepción o una situación "
        "difícil. Es una emoción humana que merece atención."
    )

    card(
        "Ansiedad",
        "Puede manifestarse mediante preocupación excesiva, tensión, "
        "inquietud o dificultad para concentrarse."
    )

    card(
        "Frustración",
        "Puede aparecer cuando las cosas no salen como esperamos "
        "o cuando encontramos obstáculos."
    )

    card(
        "Soledad",
        "No siempre significa estar físicamente solo. También puede "
        "aparecer cuando sentimos que nadie nos comprende."
    )

    title("¿Cuándo buscar ayuda?")

    st.markdown("""
    Es importante considerar apoyo profesional cuando:

    - Las emociones difíciles persisten y afectan la vida cotidiana.
    - Se presentan cambios importantes en el sueño o el apetito.
    - Hay aislamiento o pérdida de interés en actividades.
    - Las preocupaciones interfieren con los estudios o las relaciones.
    - Sientes que no puedes manejar la situación por tu cuenta.
    """)

    title("Pequeñas acciones de autocuidado")

    st.markdown("""
    - Mantener rutinas de descanso.
    - Hablar con personas de confianza.
    - Realizar actividades que disfrutes.
    - Establecer límites.
    - Tomar pausas cuando las necesites.
    - Buscar orientación profesional cuando sea necesario.
    """)

    reflection(
        "¿Te permites expresar lo que sientes o sueles guardarlo "
        "para evitar preocupar a los demás?"
    )

    st.info(
        "Este contenido es educativo y no sustituye la evaluación "
        "ni la atención de profesionales de salud mental."
    )


# -----------------------------------------
# EXPERIENCIAS COMPARTIDAS
# -----------------------------------------

elif page == "🎥 Experiencias compartidas":

    title(
        "Experiencias compartidas",
        "Cada experiencia merece ser escuchada con respeto."
    )

    st.write(
        "Este espacio permite compartir reflexiones y experiencias "
        "relacionadas con los temas de la plataforma."
    )

    tab1, tab2 = st.tabs(["📖 Historias escritas", "🎬 Videos"])

    with tab1:

        title("Historias de la comunidad")

        if st.session_state.stories_public:
            for story in st.session_state.stories_public:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <h3>💜 Experiencia compartida</h3>
                        <p>{story}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.info(
                "Todavía no hay experiencias publicadas. "
                "¡Puedes ser parte de este espacio!"
            )

        st.divider()
        st.subheader("Comparte tu experiencia")

        with st.form("story_form"):
            story_text = st.text_area(
                "Escribe tu reflexión o experiencia:",
                placeholder="Este es un espacio para expresarte...",
                height=160
            )

            anonymous = st.checkbox(
                "Quiero compartirla de manera anónima",
                value=True
            )

            submitted = st.form_submit_button("Enviar experiencia")

            if submitted:
                if story_text.strip():
                    st.session_state.stories_pending.append(
                        story_text.strip()
                    )
                    st.success(
                        "Tu experiencia fue enviada para revisión. "
                        "No aparecerá públicamente hasta ser aprobada."
                    )
                else:
                    st.warning("Por favor, escribe algo antes de enviar.")

    with tab2:

        title("Videos y testimonios")

        if st.session_state.videos:
            for video in st.session_state.videos:
                st.subheader(video["name"])
                st.video(video["data"])
        else:
            st.info(
                "Próximamente encontrarás videos y testimonios "
                "en este espacio."
            )

    st.caption(
        "Las experiencias enviadas requieren revisión antes de publicarse. "
        "Evita incluir nombres, teléfonos, direcciones u otros datos "
        "personales. No compartas contenido íntimo de otras personas."
    )


# -----------------------------------------
# ZONA INTERACTIVA
# -----------------------------------------

elif page == "🎲 Zona interactiva":

    title(
        "Zona interactiva",
        "Piensa, decide y reflexiona. No siempre existe una respuesta sencilla."
    )

    st.subheader("💭 Dilemas de la vida cotidiana")

    dilemmas = [
        {
            "title": "1. El secreto del grupo",
            "situation": (
                "Un compañero comparte una captura de pantalla de una "
                "conversación privada de otra estudiante. Todos comienzan "
                "a burlarse. Tú sabes que la información no debía compartirse."
            ),
            "question": "¿Qué harías?",
            "options": [
                "Compartir la captura para no quedar excluido.",
                "No participar y pedir que eliminen la captura.",
                "Reírme de la situación sin compartirla."
            ],
            "reflection": (
                "Compartir contenido privado sin permiso puede afectar "
                "la confianza y la privacidad de una persona."
            )
        },
        {
            "title": "2. La cuenta anónima",
            "situation": (
                "Aparece una cuenta anónima en redes sociales que publica "
                "rumores y comentarios ofensivos sobre estudiantes "
                "de tu universidad."
            ),
            "question": "¿Cómo actuarías?",
            "options": [
                "Seguir la cuenta porque parece entretenida.",
                "Reportar el contenido y apoyar a las personas afectadas.",
                "Comentar las publicaciones para aumentar su alcance."
            ],
            "reflection": (
                "El anonimato no elimina la responsabilidad por las "
                "acciones realizadas en internet."
            )
        },
        {
            "title": "3. Una prueba de amor",
            "situation": (
                "Tu pareja te pide las contraseñas de tus redes sociales "
                "y afirma que, si no las compartes, significa que ocultas algo."
            ),
            "question": "¿Qué decisión tomarías?",
            "options": [
                "Entregar las contraseñas para evitar una discusión.",
                "Explicar que la privacidad también existe dentro de una relación.",
                "Dejar de utilizar las redes sociales."
            ],
            "reflection": (
                "La confianza no exige renunciar a la privacidad. "
                "Los límites personales deben respetarse."
            )
        },
        {
            "title": "4. La presión de los demás",
            "situation": (
                "En una fiesta, tus amigos insisten en que bebas o participes "
                "en una situación íntima que no deseas."
            ),
            "question": "¿Qué harías?",
            "options": [
                "Aceptar para evitar que se burlen de mí.",
                "Expresar que no quiero y mantener mi decisión.",
                "Hacerlo solamente para no parecer diferente."
            ],
            "reflection": (
                "Tienes derecho a decir no. La presión social no debe "
                "determinar tus decisiones personales."
            )
        },
        {
            "title": "5. La sonrisa que engaña",
            "situation": (
                "Un amigo suele mostrarse alegre, pero un día te dice "
                "que está cansado de fingir que todo está bien."
            ),
            "question": "¿Cómo responderías?",
            "options": [
                "Decirle que no exagere.",
                "Escucharlo sin juzgarlo y animarlo a buscar apoyo.",
                "Cambiar de tema para evitar una conversación incómoda."
            ],
            "reflection": (
                "Escuchar con empatía puede ser un primer paso importante. "
                "No tienes que resolverlo todo: también puedes ayudarle "
                "a encontrar apoyo profesional."
            )
        },
        {
            "title": "6. Compararse hasta desaparecer",
            "situation": (
                "Una estudiante pasa horas comparando su cuerpo, su vida "
                "y sus logros con los de personas que sigue en redes sociales. "
                "Cada vez se siente menos satisfecha consigo misma."
            ),
            "question": "¿Qué podría ayudar?",
            "options": [
                "Seguir comparándose para intentar mejorar.",
                "Recordar que las redes muestran una parte seleccionada "
                "de la realidad y cuidar su bienestar digital.",
                "Intentar parecerse exactamente a esas personas."
            ],
            "reflection": (
                "El contenido de redes no representa necesariamente "
                "la vida completa de quienes lo publican."
            )
        }
    ]

    for index, dilemma in enumerate(dilemmas):

        with st.expander(dilemma["title"]):

            st.write(dilemma["situation"])
            st.markdown("**" + dilemma["question"] + "**")

            selected = st.radio(
                "Selecciona tu respuesta:",
                dilemma["options"],
                key=f"dilemma_{index}"
            )

            if st.button(
                "Ver reflexión",
                key=f"reflection_{index}"
            ):
                st.info(dilemma["reflection"])

    st.divider()

    title("🧠 Comprueba lo que sabes")

    st.write(
        "Una persona comparte una fotografía privada de otra sin "
        "su autorización. ¿Cuál es la acción más adecuada?"
    )

    answer = st.radio(
        "Selecciona una respuesta:",
        [
            "Compartirla con más personas.",
            "No difundirla y reportar la situación.",
            "Guardar la fotografía para compartirla después."
        ],
        key="quiz_question"
    )

    if st.button("Comprobar respuesta"):
        if answer == "No difundirla y reportar la situación.":
            st.success(
                "¡Correcto! Respetar la privacidad y actuar "
                "responsablemente ayuda a prevenir el daño."
            )
        else:
            st.warning(
                "Inténtalo nuevamente. Recuerda que compartir "
                "contenido privado sin permiso puede causar daño."
            )


# -----------------------------------------
# ORIENTACIÓN Y AYUDA
# -----------------------------------------

elif page == "🆘 Orientación y ayuda":

    title(
        "Orientación y ayuda",
        "Pedir ayuda no es una señal de debilidad."
    )

    card(
        "Línea 123",
        "En Colombia, el 123 es la línea de emergencias para situaciones "
        "que requieren atención inmediata."
    )

    card(
        "Línea 141 del ICBF",
        "Canal de atención y orientación para situaciones que afectan "
        "los derechos de niños, niñas y adolescentes."
    )

    card(
        "Instituciones educativas",
        "Puedes acudir a bienestar universitario, orientación escolar, "
        "docentes de confianza o los protocolos institucionales "
        "de atención."
    )

    card(
        "Atención en salud mental",
        "Puedes consultar con profesionales de psicología o acudir "
        "a los servicios de salud disponibles en tu municipio."
    )

    st.warning(
        "Si tú o alguien más está en peligro inmediato, busca ayuda "
        "de emergencia. Si existe riesgo de autolesión o suicidio, "
        "no dejes sola a la persona y contacta servicios de emergencia "
        "o atención profesional."
    )

    reflection(
        "No tienes que atravesar una situación difícil sin acompañamiento."
    )


# -----------------------------------------
# PANEL DE ADMINISTRACIÓN
# -----------------------------------------

elif page == "🔐 Administración":

    title(
        "Panel de administración",
        "Espacio de gestión de los contenidos de Entre Líneas."
    )

    password = st.text_input(
        "Contraseña de administración:",
        type="password"
    )

    if password == "EntreLineas2026":

        st.success("Acceso al panel de demostración.")

        tab1, tab2 = st.tabs([
            "🎬 Gestionar videos",
            "📖 Revisar experiencias"
        ])

        with tab1:

            st.subheader("Agregar un video")

            uploaded_video = st.file_uploader(
                "Selecciona un video desde tu dispositivo:",
                type=["mp4", "mov", "webm"]
            )

            video_name = st.text_input(
                "Título del video:"
            )

            if st.button("Agregar video"):

                if uploaded_video and video_name.strip():

                    st.session_state.videos.append({
                        "name": video_name.strip(),
                        "data": uploaded_video.getvalue()
                    })

                    st.success("Video agregado a esta sesión.")
                else:
                    st.warning(
                        "Debes seleccionar un video y escribir su título."
                    )

            st.divider()
            st.subheader("Videos disponibles")

            if st.session_state.videos:

                for i, video in enumerate(
                    st.session_state.videos
                ):

                    col1, col2 = st.columns([4, 1])

                    with col1:
                        st.write(video["name"])

                    with col2:
                        if st.button(
                            "Eliminar",
                            key=f"delete_video_{i}"
                        ):
                            st.session_state.videos.pop(i)
                            st.rerun()

            else:
                st.info("Todavía no hay videos agregados.")

        with tab2:

            st.subheader("Experiencias pendientes de revisión")

            if st.session_state.stories_pending:

                for i, story in enumerate(
                    st.session_state.stories_pending
                ):

                    st.markdown(
                        f'<div class="info-card">{story}</div>',
                        unsafe_allow_html=True
                    )

                    col1, col2 = st.columns(2)

                    with col1:
                        if st.button(
                            "Aprobar",
                            key=f"approve_{i}"
                        ):
                            st.session_state.stories_public.append(story)
                            st.session_state.stories_pending.pop(i)
                            st.rerun()

                    with col2:
                        if st.button(
                            "Rechazar",
                            key=f"reject_{i}"
                        ):
                            st.session_state.stories_pending.pop(i)
                            st.rerun()

            else:
                st.info(
                    "No hay experiencias pendientes de revisión."
                )

    elif password:
        st.error("Contraseña incorrecta.")

    st.caption(
        "Contraseña de demostración: EntreLineas2026. "
        "Cámbiala antes de publicar el proyecto. "
        "Este panel no cuenta con autenticación segura."
    )

    st.warning(
        "Esta versión de demostración mantiene los videos y las "
        "experiencias en la sesión de la aplicación. Para conservarlos "
        "permanentemente y compartirlos entre visitantes se necesita "
        "una base de datos y almacenamiento de archivos."
    )


# -----------------------------------------
# PIE DE PÁGINA
# -----------------------------------------

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:15px; color:#795c89;">
        <b>Entre Líneas 💜</b><br>
        Un espacio para escuchar, comprender, aprender y expresarse.<br>
        <small>Proyecto educativo de sensibilización y reflexión.</small>
    </div>
    """,
    unsafe_allow_html=True
)
