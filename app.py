code = r import streamlit as st
from supabase import create_client
import uuid

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
# CONEXIÓN CON SUPABASE
# -----------------------------------------

@st.cache_resource
def conectar_supabase():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


@st.cache_resource
def conectar_supabase_admin():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_SECRET_KEY"]
    )


# Conexión pública: se utiliza para consultar videos publicados.
supabase = conectar_supabase()


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

        try:
            respuesta_videos = (
                supabase.table("testimonios")
                .select("id, nombre, video_url, fecha")
                .eq("tipo", "video")
                .eq("publicado", True)
                .order("fecha", desc=True)
                .execute()
            )

            videos_publicados = respuesta_videos.data

            if videos_publicados:
                for video in videos_publicados:
                    st.subheader(video["nombre"])
                    st.video(video["video_url"])
                    st.divider()
            else:
                st.info(
                    "Todavía no hay videos publicados. "
                    "Próximamente encontrarás testimonios aquí."
                )

        except Exception as error:
            st.error("No pudimos cargar los videos.")
            st.write(str(error))

    st.caption(
        "Las experiencias enviadas requieren revisión antes de publicarse. "
        "Evita incluir nombres, teléfonos, direcciones u otros datos "
        "personales. No compartas contenido íntimo de otras personas."
    )


# -----------------------------------------
# ZONA INTERACTIVA: DILEMAS ABIERTOS
# -----------------------------------------

elif page == "🎲 Zona interactiva":

    title(
        "Zona interactiva",
        "Historias que invitan a pensar, sentir y ponerse en el lugar del otro."
    )

    st.markdown("""
    Cada historia presenta una situación que podría ocurrir en la vida
    cotidiana de un estudiante universitario.

    Lee con atención, imagina que estás viviendo esa situación y expresa
    tu opinión con libertad. No se trata de encontrar una respuesta
    perfecta, sino de reflexionar sobre nuestras decisiones.
    """)

    dilemmas = [
        {
            "title": "01. El secreto del grupo",
            "story": """
            ### Una conversación que nunca debió salir del chat

            Laura es una estudiante universitaria que suele compartir
            sus preocupaciones en un grupo privado con sus compañeros.
            Una noche, después de una discusión familiar, escribe un
            mensaje contando algo muy personal y pide que nadie lo comparta.

            Al día siguiente, uno de sus compañeros toma una captura
            de pantalla y la envía a otro grupo. Poco después, varias
            personas comienzan a hacer comentarios y bromas sobre lo
            que Laura había contado.

            Laura se entera de lo ocurrido y deja de participar en clase.
            Algunos compañeros saben quién compartió la captura, pero
            prefieren guardar silencio porque no quieren tener problemas
            con el grupo.
            """,
            "question": """
            Si fueras parte de ese grupo, ¿qué harías frente a lo ocurrido?
            ¿Cómo crees que podrías apoyar a Laura sin empeorar la situación?
            """
        },
        {
            "title": "02. La cuenta anónima",
            "story": """
            ### Detrás de una pantalla también hay personas

            Durante varias semanas, comienza a circular una cuenta anónima
            en redes sociales de una universidad. Al principio publica
            memes y situaciones graciosas relacionadas con la vida
            estudiantil.

            Sin embargo, poco a poco empieza a publicar fotografías
            de estudiantes acompañadas de rumores, burlas y comentarios
            sobre su apariencia física y su vida personal.

            Andrés descubre que una de las publicaciones habla de él.
            Aunque intenta ignorarla, recibe mensajes de personas que
            se burlan de su situación. Sus amigos le dicen que no se
            preocupe porque todo es parte de las redes sociales.

            Una compañera sabe quién administra la cuenta, pero tiene
            miedo de denunciarlo porque podría convertirse en el próximo
            objetivo.
            """,
            "question": """
            ¿Cómo actuarías si fueras Andrés o si conocieras a la persona
            que administra la cuenta? ¿Qué responsabilidad tienen quienes
            comparten o comentan esas publicaciones?
            """
        },
        {
            "title": "03. Una prueba de amor",
            "story": """
            ### ¿Amar significa compartirlo todo?

            Camila lleva varios meses en una relación. Al principio,
            todo parece funcionar bien, pero su pareja comienza a pedirle
            que comparta la contraseña de sus redes sociales.

            Le dice que las parejas no deberían tener secretos y que,
            si realmente lo ama, no tendría ningún problema en mostrarle
            sus conversaciones.

            Camila se siente incómoda porque considera que tiene derecho
            a conservar su privacidad. Sin embargo, teme que negarse
            provoque una discusión o que su pareja piense que está
            ocultando algo.

            Una amiga le aconseja que entregue las contraseñas para
            demostrar confianza, mientras otra le recuerda que una
            relación también necesita límites.
            """,
            "question": """
            ¿Qué le aconsejarías a Camila? ¿Dónde termina la confianza
            y dónde comienza el control dentro de una relación?
            """
        },
        {
            "title": "04. La presión de los demás",
            "story": """
            ### Cuando decir que no parece difícil

            Mateo asiste a una fiesta con varios compañeros de la
            universidad. Durante la noche, algunos amigos comienzan
            a insistirle para que consuma alcohol y participe en una
            situación íntima con otra persona.

            Mateo no quiere hacerlo. Sin embargo, sus amigos empiezan
            a decirle que es aburrido, que debe dejar de comportarse
            como un niño y que no debería tener miedo de experimentar.

            Aunque se siente incómodo, comienza a pensar que quizás
            debería aceptar para evitar las burlas y no sentirse
            excluido del grupo.

            Una amiga nota que Mateo está incómodo y le pregunta
            si realmente quiere participar.
            """,
            "question": """
            ¿Qué decisión tomarías si estuvieras en el lugar de Mateo?
            ¿Por qué puede ser difícil establecer límites cuando existe
            presión social?
            """
        },
        {
            "title": "05. La sonrisa que engaña",
            "story": """
            ### A veces, quien más sonríe también necesita ayuda

            Valentina es conocida en su universidad por ser una persona
            alegre, participativa y siempre dispuesta a ayudar a sus amigos.
            Sin embargo, durante las últimas semanas ha comenzado a
            aislarse y a faltar a algunas clases.

            Un día, después de una jornada académica, se queda conversando
            con Daniel y le confiesa que está agotada emocionalmente.
            Le cuenta que siente mucha presión por sus estudios, por las
            expectativas de su familia y por intentar demostrar que
            puede con todo.

            Daniel no sabe qué responder. Quiere ayudarla, pero teme
            decir algo incorrecto. Otros compañeros le han comentado
            que Valentina siempre parece estar bien, así que seguramente
            está exagerando.
            """,
            "question": """
            ¿Cómo responderías si fueras Daniel? ¿Qué significa escuchar
            a alguien sin juzgarlo y de qué manera podrías acompañar
            a Valentina?
            """
        },
        {
            "title": "06. Compararse hasta desaparecer",
            "story": """
            ### La vida perfecta que aparece en una pantalla

            Mariana pasa gran parte de su tiempo en redes sociales.
            Todos los días observa fotografías y videos de personas
            que muestran viajes, logros académicos, cuerpos que considera
            perfectos y estilos de vida aparentemente increíbles.

            Poco a poco comienza a comparar su apariencia, sus resultados
            académicos y su situación económica con lo que ve en internet.
            Aunque sabe que las publicaciones no muestran toda la realidad,
            siente que su propia vida no es suficiente.

            Deja de publicar fotografías porque no le gusta cómo se ve
            y comienza a evitar reuniones con sus amigos. Una compañera
            nota el cambio y le pregunta si se encuentra bien.

            Mariana responde que simplemente necesita esforzarse más
            para llegar a ser como las personas que sigue.
            """,
            "question": """
            ¿Qué le dirías a Mariana? ¿Cómo pueden influir las redes
            sociales en la autoestima y qué cambios podrían ayudarla
            a construir una relación más saludable con ellas?
            """
        }
    ]

    if "dilemma_answers" not in st.session_state:
        st.session_state.dilemma_answers = {}

    for index, dilemma in enumerate(dilemmas):

        with st.expander(dilemma["title"], expanded=False):

            st.markdown(dilemma["story"])

            st.divider()

            st.markdown("### 💭 Tu espacio de reflexión")

            st.write(dilemma["question"])

            with st.form(key=f"dilemma_form_{index}"):

                answer = st.text_area(
                    "Escribe tu respuesta:",
                    placeholder=(
                        "Puedes expresar lo que piensas, cómo te sentirías "
                        "y qué harías en esta situación..."
                    ),
                    height=160,
                    key=f"dilemma_text_{index}"
                )

                submitted = st.form_submit_button(
                    "Enviar mi reflexión"
                )

                if submitted:

                    if answer.strip():

                        st.session_state.dilemma_answers[index] = (
                            answer.strip()
                        )

                        st.success(
                            "¡Tu reflexión ha sido registrada en esta sesión!"
                        )

                    else:

                        st.warning(
                            "Escribe tu reflexión antes de enviarla."
                        )

            if index in st.session_state.dilemma_answers:

                st.caption("Tu última reflexión está registrada.")

    st.divider()

    st.markdown("### 💜 Para pensar...")

    st.markdown("""
    Las situaciones que vivimos no siempre tienen soluciones sencillas.
    Escuchar otras perspectivas, reconocer nuestras emociones y
    comprender las consecuencias de nuestras decisiones nos ayuda
    a construir relaciones más respetuosas y espacios más seguros.
    """)


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

    # La contraseña se guarda en Streamlit Secrets, nunca en el código.
    if password and password == st.secrets["ADMIN_PASSWORD"]:

        supabase_admin = conectar_supabase_admin()

        st.success("Acceso al panel de administración.")

        tab1, tab2 = st.tabs([
            "🎬 Gestionar videos",
            "📖 Revisar experiencias"
        ])

        # -----------------------------------------
        # GESTIONAR VIDEOS
        # -----------------------------------------

        with tab1:

            st.subheader("Agregar videos")

            uploaded_videos = st.file_uploader(
                "Selecciona uno o varios videos:",
                type=["mp4", "mov", "webm"],
                accept_multiple_files=True,
                key="multiple_videos"
            )

            if uploaded_videos:

                st.write("### Escribe el título de cada video")

                titles = []

                for i, video in enumerate(uploaded_videos):

                    title_video = st.text_input(
                        f"Título del video {i + 1}:",
                        value="",
                        placeholder="Escribe aquí el título que quieras mostrar",
                        key=f"custom_title_{i}"
                    )

                    titles.append(title_video)

                if st.button("Guardar videos"):

                    if all(title.strip() for title in titles):

                        for i, video in enumerate(uploaded_videos):

                            extension = (
                                video.name.rsplit(".", 1)[-1].lower()
                                if "." in video.name
                                else "mp4"
                            )

                            nombre_archivo = (
                                f"{uuid.uuid4().hex}.{extension}"
                            )

                            archivo_subido = False

                            try:

                                # Subir el archivo al bucket público.
                                supabase_admin.storage.from_(
                                    "videos-testimonios"
                                ).upload(
                                    nombre_archivo,
                                    video.getvalue(),
                                    file_options={
                                        "content-type": (
                                            video.type
                                            or "application/octet-stream"
                                        ),
                                        "upsert": "false"
                                    }
                                )

                                archivo_subido = True

                                # Obtener la URL pública del archivo.
                                video_url = (
                                    supabase_admin.storage.from_(
                                        "videos-testimonios"
                                    ).get_public_url(nombre_archivo)
                                )

                                # Guardar título y URL en la tabla.
                                supabase_admin.table(
                                    "testimonios"
                                ).insert({
                                    "nombre": titles[i].strip(),
                                    "tipo": "video",
                                    "video_url": video_url,
                                    "publicado": True
                                }).execute()

                                st.success(
                                    f"¡{titles[i].strip()} se guardó correctamente!"
                                )

                            except Exception as error:

                                # Si el archivo se subió pero falló el
                                # registro en la tabla, borrar el archivo
                                # para evitar dejarlo sin registro.
                                if archivo_subido:
                                    try:
                                        supabase_admin.storage.from_(
                                            "videos-testimonios"
                                        ).remove([nombre_archivo])
                                    except Exception:
                                        pass

                                st.error(
                                    f"No se pudo guardar {video.name}: {error}"
                                )

                    else:

                        st.error(
                            "Escribe un título para cada video."
                        )

            st.divider()

            # -----------------------------------------
            # VIDEOS DISPONIBLES
            # -----------------------------------------

            st.subheader("Videos disponibles")

            try:

                respuesta_videos = (
                    supabase_admin.table("testimonios")
                    .select("id, nombre, video_url, fecha")
                    .eq("tipo", "video")
                    .order("fecha", desc=True)
                    .execute()
                )

                videos_guardados = respuesta_videos.data

                if videos_guardados:

                    for video in videos_guardados:

                        col1, col2 = st.columns([4, 1])

                        with col1:
                            st.write(video["nombre"])

                        with col2:

                            if st.button(
                                "Eliminar",
                                key=f"delete_video_{video['id']}"
                            ):

                                try:

                                    marcador = (
                                        "/storage/v1/object/public/"
                                        "videos-testimonios/"
                                    )

                                    if marcador not in video["video_url"]:
                                        raise ValueError(
                                            "No se pudo identificar la ruta "
                                            "del archivo en Storage."
                                        )

                                    ruta_archivo = (
                                        video["video_url"]
                                        .split(marcador, 1)[1]
                                        .split("?", 1)[0]
                                    )

                                    # Eliminar primero el archivo del bucket.
                                    supabase_admin.storage.from_(
                                        "videos-testimonios"
                                    ).remove([ruta_archivo])

                                    # Eliminar después el registro de la tabla.
                                    supabase_admin.table(
                                        "testimonios"
                                    ).delete().eq(
                                        "id", video["id"]
                                    ).execute()

                                    st.success(
                                        "Video eliminado correctamente."
                                    )

                                    st.rerun()

                                except Exception as error:

                                    st.error(
                                        f"No se pudo eliminar el video: {error}"
                                    )

                        st.video(video["video_url"])

                else:

                    st.info("Todavía no hay videos agregados.")

            except Exception as error:

                st.error("No pudimos cargar los videos guardados.")
                st.write(str(error))

        # -----------------------------------------
        # REVISAR EXPERIENCIAS ESCRITAS
        # -----------------------------------------

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


# Basic syntax validation before sharing.

print(f"Líneas: {len(code.splitlines())}")
