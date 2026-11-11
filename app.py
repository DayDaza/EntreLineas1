
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Entre Líneas | Un espacio para escucharnos</title>
<style>
:root{
 --purple:#7654a8;
 --deep:#49336e;
 --light:#f2ebfa;
 --pink:#e9b8d2;
 --rose:#fff0f6;
 --ink:#30283a;
 --muted:#777080;
 --white:#fff;
 --green:#e4f4ec;
 --border:#e9e1f0;
 --shadow:0 8px 28px rgba(75,48,105,.09);
}
*{box-sizing:border-box}
body{
 margin:0;background:#faf8fc;color:var(--ink);
 font-family:Inter,"Segoe UI",Arial,sans-serif;
}
button,input,textarea,select{font:inherit}
button{cursor:pointer}
.layout{min-height:100vh}
.sidebar{
 position:fixed;inset:0 auto 0 0;width:250px;
 background:linear-gradient(165deg,#49336e,#7654a8);
 color:white;padding:27px 18px;z-index:20;
 display:flex;flex-direction:column;
}
.brand{font-size:27px;font-weight:800;letter-spacing:-1px}
.brand span{color:#f5c9df}
.brand-sub{font-size:12px;color:#e5d8f2;margin:7px 0 30px}
.nav-label{
 font-size:10px;letter-spacing:2px;color:#d4c2e8;
 margin:12px 10px;
}
.nav-btn{
 display:flex;align-items:center;gap:12px;width:100%;
 padding:12px 13px;border:0;border-radius:12px;
 background:transparent;color:#eee5f8;text-align:left;
 font-size:13px;margin:3px 0;transition:.2s;
}
.nav-btn:hover,.nav-btn.active{background:#ffffff22;color:white}
.nav-btn.active{box-shadow:inset 3px 0 #f5c9df}
.sidebar-footer{margin-top:auto;font-size:11px;color:#d8cce8;line-height:1.6;padding:12px}
.main{margin-left:250px;min-height:100vh}
.topbar{
 height:66px;padding:0 34px;display:flex;align-items:center;
 justify-content:space-between;background:#ffffffdc;
 border-bottom:1px solid var(--border);position:sticky;top:0;z-index:10;
 backdrop-filter:blur(12px);
}
.topbar-label{font-size:12px;color:var(--muted)}
.admin-link{
 border:1px solid var(--border);background:white;color:var(--deep);
 padding:9px 15px;border-radius:30px;font-size:12px;
}
.page{display:none;padding:35px;max-width:1200px;margin:auto}
.page.active{display:block;animation:appear .25s ease}
@keyframes appear{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:none}}
.hero{
 border-radius:25px;padding:48px;
 background:linear-gradient(120deg,#eee4fa,#fceaf2);
 position:relative;overflow:hidden;min-height:300px;
 display:flex;align-items:center;
}
.hero:after{
 content:"♡";position:absolute;right:8%;top:-55px;
 font-size:270px;color:#ffffff70;transform:rotate(-15deg);
}
.hero-content{max-width:610px;position:relative;z-index:1}
.eyebrow{color:var(--purple);font-weight:800;font-size:11px;letter-spacing:2px}
h1{font-size:clamp(34px,5vw,54px);line-height:1.08;margin:14px 0;color:var(--deep)}
.hero p{font-size:15px;line-height:1.8;color:#62576d;max-width:540px}
.btn{
 border:0;border-radius:30px;padding:12px 20px;
 background:var(--purple);color:white;font-weight:700;font-size:13px;
 transition:.2s;
}
.btn:hover{transform:translateY(-2px);filter:brightness(1.08)}
.btn-light{background:white;color:var(--deep);border:1px solid var(--border)}
.btn-pink{background:#d98fb6}
.btn-small{padding:8px 14px;font-size:12px}
.section-head{margin:36px 0 20px}
.section-head h2{color:var(--deep);font-size:25px;margin:0 0 8px}
.section-head p{color:var(--muted);font-size:13px;line-height:1.7;margin:0}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:17px}
.card{
 background:white;border:1px solid var(--border);border-radius:19px;
 padding:22px;box-shadow:var(--shadow);
}
.card-icon{font-size:27px;margin-bottom:13px}
.card h3{font-size:16px;color:var(--deep);margin:0 0 9px}
.card p{font-size:13px;color:var(--muted);line-height:1.7}
.card-link{border:0;background:none;color:var(--purple);font-weight:700;font-size:12px;padding:8px 0}
.pill{
 display:inline-block;border-radius:30px;background:var(--light);
 color:var(--purple);padding:6px 10px;font-size:10px;font-weight:800;
 letter-spacing:.5px;
}
.content-box{
 background:white;border:1px solid var(--border);border-radius:20px;
 padding:26px;margin:18px 0;box-shadow:var(--shadow);
}
.content-box h3{color:var(--deep);margin-top:0}
.content-box p,.content-box li{font-size:14px;line-height:1.85;color:#625b6c}
.content-box ul{padding-left:20px}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.callout{
 padding:18px;border-radius:15px;background:var(--rose);
 color:#64445a;font-size:13px;line-height:1.8;
}
.soft-callout{background:var(--light);color:var(--deep)}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}
.tab{
 border:1px solid var(--border);background:white;color:var(--muted);
 border-radius:30px;padding:10px 16px;font-size:12px;font-weight:700;
}
.tab.active{background:var(--purple);color:white;border-color:var(--purple)}
.hidden{display:none!important}
.field{margin:14px 0}
.field label{display:block;font-size:12px;font-weight:700;color:var(--deep);margin-bottom:7px}
.field input,.field textarea,.field select,
.dilemma-card textarea{
 width:100%;border:1px solid var(--border);border-radius:12px;
 padding:12px 14px;background:#fdfcff;color:var(--ink);
 outline:none;font-size:13px;
}
.field input:focus,.field textarea:focus,.field select:focus,
.dilemma-card textarea:focus{border-color:var(--purple)}
.field textarea{min-height:115px;resize:vertical}
.notice{font-size:11px;color:var(--muted);line-height:1.7}
.empty{
 padding:30px;text-align:center;background:#faf8fc;border:1px dashed #d9cbe7;
 border-radius:16px;color:var(--muted);font-size:13px;line-height:1.7;
}
.video-stage{
 background:#21192c;border-radius:17px;overflow:hidden;
 display:flex;align-items:center;justify-content:center;min-height:240px;
}
.video-stage video{width:100%;max-height:450px;display:block}
.video-info{padding:14px 2px}
.video-info h3{margin:0 0 5px;color:var(--deep)}
.video-info p{font-size:12px;color:var(--muted)}
.video-controls{display:flex;justify-content:space-between;align-items:center;gap:10px}
.video-list{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:18px}
.video-item{
 padding:12px;border:1px solid var(--border);border-radius:13px;
 display:flex;justify-content:space-between;align-items:center;gap:10px;
 font-size:12px;
}
.story-item{
 background:#fff;border:1px solid var(--border);border-radius:15px;
 padding:17px;margin:12px 0;
}
.story-item h4{margin:0 0 7px;color:var(--deep)}
.story-item p{font-size:13px;line-height:1.7;color:#625b6c;white-space:pre-wrap}
.dilemma-intro{
 background:linear-gradient(120deg,#eee4fa,#fceaf2);
 border-radius:20px;padding:27px;margin-bottom:22px;
}
.dilemma-intro>span{font-size:29px}
.dilemma-intro h2{font-size:27px;color:var(--deep);margin:8px 0}
.dilemma-intro p{font-size:13px;line-height:1.8;color:#62576d;max-width:720px}
.dilemma-card{
 background:white;border:1px solid var(--border);border-radius:20px;
 padding:23px;margin:16px 0;box-shadow:var(--shadow);
}
.dilemma-top{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
.dilemma-tag{font-size:10px;font-weight:800;letter-spacing:.7px;color:var(--purple)}
.dilemma-number{font-size:10px;color:#a49aaa}
.dilemma-card h3{font-size:21px;color:var(--deep);margin:16px 0 10px}
.dilemma-story{
 background:#faf7fc;border-left:3px solid var(--pink);
 padding:17px;border-radius:0 12px 12px 0;
 font-size:13px;line-height:1.85;color:#625b6c;
}
.dilemma-question{font-size:13px;font-weight:700;line-height:1.7;margin:17px 0 10px}
.dilemma-card textarea{min-height:100px;resize:vertical}
.dilemma-actions{display:flex;gap:9px;flex-wrap:wrap;margin-top:12px}
.dilemma-submit{
 background:var(--purple);color:white;border:0;border-radius:25px;
 padding:10px 17px;font-size:12px;font-weight:700;
}
.dilemma-hint{
 display:none;margin-top:14px;padding:15px;border-radius:13px;
 background:var(--rose);font-size:12px;line-height:1.8;color:#684c60;
}
.dilemma-hint strong{display:block;margin-bottom:5px}
.saved-message{font-size:11px;color:#498567;margin-top:8px}
.quiz-question{font-weight:700;color:var(--deep);font-size:15px;line-height:1.6}
.quiz-option{
 display:block;width:100%;text-align:left;padding:12px 14px;
 margin:8px 0;border:1px solid var(--border);background:white;
 border-radius:11px;font-size:13px;color:var(--ink);
}
.quiz-option:hover{border-color:var(--purple);background:#faf7ff}
.quiz-option.selected{border-color:var(--purple);background:var(--light)}
.quiz-feedback{font-size:12px;margin-top:12px;line-height:1.7}
.resource{
 display:flex;gap:15px;align-items:flex-start;padding:17px 0;
 border-bottom:1px solid var(--border);
}
.resource:last-child{border:0}
.resource-icon{font-size:25px}
.resource h4{margin:0 0 5px;color:var(--deep)}
.resource p{font-size:12px;line-height:1.7;color:var(--muted);margin:0}
.admin-box{max-width:700px;margin:auto}
.admin-top{display:flex;justify-content:space-between;gap:10px;align-items:center}
footer{text-align:center;padding:25px;color:#978da0;font-size:11px}
.mobile-brand{display:none}
@media(max-width:850px){
 .sidebar{width:205px}
 .main{margin-left:205px}
 .page{padding:25px 20px}
 .grid{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:650px){
 .sidebar{
  position:sticky;top:0;width:100%;height:auto;padding:10px 12px;
  display:block;overflow-x:auto;white-space:nowrap;
 }
 .brand{font-size:21px;display:inline-block;margin:2px 8px 8px}
 .brand-sub,.nav-label,.sidebar-footer{display:none}
 .sidebar nav{display:flex;gap:5px}
 .nav-btn{display:inline-flex;width:auto;white-space:nowrap;padding:9px 11px;font-size:11px;margin:0}
 .main{margin:0}
 .topbar{height:52px;padding:0 16px}
 .page{padding:20px 14px}
 .hero{padding:28px 23px;min-height:280px}
 .hero:after{font-size:150px;right:-15px;top:5px}
 .grid,.two-col{grid-template-columns:1fr}
 .video-list{grid-template-columns:1fr}
 .content-box{padding:19px}
 .dilemma-card{padding:17px}
 .admin-link{font-size:11px}
}
</style>
</head>

<body>
<div class="layout">
<aside class="sidebar">
 <div class="brand">Entre <span>Líneas.</span></div>
 <div class="brand-sub">Un espacio para escucharnos, aprender y respetarnos.</div>
 <div class="nav-label">EXPLORA</div>
 <nav>
  <button class="nav-btn active" onclick="go('inicio',this)">⌂ Inicio</button>
  <button class="nav-btn" onclick="go('acoso',this)">🛡️ Acoso y ciberacoso</button>
  <button class="nav-btn" onclick="go('sexualidad',this)">💗 Sexualidad y respeto</button>
  <button class="nav-btn" onclick="go('bienestar',this)">🌷 Salud mental</button>
  <button class="nav-btn" onclick="go('experiencias',this)">💬 Experiencias</button>
  <button class="nav-btn" onclick="go('interactiva',this)">🎮 Zona interactiva</button>
  <button class="nav-btn" onclick="go('ayuda',this)">🫶 Orientación y ayuda</button>
 </nav>
 <div class="sidebar-footer">Un espacio seguro comienza cuando aprendemos a escucharnos.<br><br>© Entre Líneas</div>
</aside>

<main class="main">
 <header class="topbar">
  <span class="topbar-label">Un espacio para aprender sin prejuicios ♡</span>
  <button class="admin-link" onclick="go('admin')">⚙ Administración</button>
 </header>

 <!-- INICIO -->
 <section class="page active" id="inicio">
  <div class="hero">
   <div class="hero-content">
    <span class="eyebrow">BIENVENIDO/A A ENTRE LÍNEAS</span>
    <h1>Hay cosas que merecen ser habladas.</h1>
    <p>Un espacio para conversar sobre situaciones que vivimos, sentimos y muchas veces no sabemos cómo expresar. Aquí encontrarás información, reflexiones y actividades sobre el respeto, el bienestar y las relaciones saludables.</p>
    <button class="btn" onclick="go('acoso')">Comenzar a explorar →</button>
   </div>
  </div>
  <div class="section-head">
   <h2>Un espacio para cada conversación</h2>
   <p>Explora los temas y encuentra información que puede ayudarte a comprender mejor tu entorno.</p>
  </div>
  <div class="grid">
   <article class="card"><div class="card-icon">🛡️</div><h3>Acoso y ciberacoso</h3><p>Reconoce las señales, comprende sus consecuencias y descubre cómo actuar ante estas situaciones.</p><button class="card-link" onclick="go('acoso')">Explorar tema →</button></article>
   <article class="card"><div class="card-icon">💗</div><h3>Sexualidad y respeto</h3><p>Hablemos de consentimiento, límites, decisiones y relaciones basadas en el respeto.</p><button class="card-link" onclick="go('sexualidad')">Explorar tema →</button></article>
   <article class="card"><div class="card-icon">🌷</div><h3>Salud mental y bienestar</h3><p>Reconoce tus emociones, cuida tu bienestar y aprende a pedir apoyo cuando lo necesites.</p><button class="card-link" onclick="go('bienestar')">Explorar tema →</button></article>
   <article class="card"><div class="card-icon">💬</div><h3>Experiencias compartidas</h3><p>Historias, reflexiones y experiencias que nos permiten comprender otras perspectivas.</p><button class="card-link" onclick="go('experiencias')">Conocer experiencias →</button></article>
   <article class="card"><div class="card-icon">🎮</div><h3>Zona interactiva</h3><p>Participa en actividades, responde preguntas y enfrenta dilemas de la vida cotidiana.</p><button class="card-link" onclick="go('interactiva')">Participar →</button></article>
   <article class="card"><div class="card-icon">🫶</div><h3>Orientación y ayuda</h3><p>Encuentra información sobre dónde buscar orientación y apoyo.</p><button class="card-link" onclick="go('ayuda')">Ver recursos →</button></article>
  </div>
  <div class="content-box" style="margin-top:24px">
   <span class="pill">NUESTRA IDEA</span>
   <h3>Tu voz también importa.</h3>
   <p>Entre Líneas busca promover conversaciones informadas, respetuosas y libres de prejuicios. No necesitas tener todas las respuestas para comenzar a hablar de lo que importa.</p>
  </div>
 </section>

 <!-- ACOSO -->
 <section class="page" id="acoso">
  <span class="pill">01 · CONVIVENCIA DIGITAL Y SOCIAL</span>
  <div class="section-head"><h2>Acoso y ciberacoso</h2><p>Reconocer una situación es el primer paso para no normalizarla.</p></div>
  <div class="content-box">
   <h3>¿Qué es el acoso?</h3>
   <p>El acoso implica comportamientos agresivos o intimidatorios que buscan dañar, humillar o someter a otra persona. Puede presentarse en espacios educativos, sociales y cotidianos.</p>
   <div class="two-col">
    <div class="callout"><strong>En espacios presenciales</strong><br>Insultos, amenazas, burlas constantes, exclusión intencional, intimidación o agresiones físicas.</div>
    <div class="callout soft-callout"><strong>En espacios digitales</strong><br>Mensajes ofensivos, difusión de imágenes sin permiso, amenazas, suplantación de identidad o humillaciones en redes.</div>
   </div>
  </div>
  <div class="two-col">
   <div class="content-box"><h3>¿Cómo identificarlo?</h3><ul><li>La conducta genera miedo, incomodidad o humillación.</li><li>Puede repetirse o mantenerse en el tiempo.</li><li>Existe una relación de poder o presión.</li><li>Puede afectar la seguridad y la participación de la persona.</li></ul></div>
   <div class="content-box"><h3>¿Qué puedes hacer?</h3><ul><li>No compartas contenido que humille a alguien.</li><li>Conserva evidencias cuando sea seguro hacerlo.</li><li>Bloquea y reporta cuentas agresoras.</li><li>Busca apoyo de personas o instituciones de confianza.</li><li>Acompaña a quien está viviendo la situación.</li></ul></div>
  </div>
  <div class="callout"><strong>Recuerda:</strong> compartir una publicación ofensiva también puede contribuir a que el daño continúe. Antes de reenviar, piensa en sus consecuencias.</div>
 </section>

 <!-- SEXUALIDAD -->
 <section class="page" id="sexualidad">
  <span class="pill">02 · AUTONOMÍA Y RESPETO</span>
  <div class="section-head"><h2>Sexualidad y respeto</h2><p>Conocerte, tomar decisiones y establecer límites también es parte del bienestar.</p></div>
  <div class="content-box">
   <h3>La sexualidad va más allá de lo físico</h3>
   <p>Incluye aspectos emocionales, afectivos, sociales y personales. Se relaciona con nuestra identidad, la manera en que construimos vínculos y cómo expresamos nuestros límites y decisiones.</p>
  </div>
  <div class="grid">
   <div class="card"><div class="card-icon">✋</div><h3>Consentimiento</h3><p>Debe ser libre, informado, específico y reversible. Aceptar algo una vez no significa aceptarlo siempre.</p></div>
   <div class="card"><div class="card-icon">🔐</div><h3>Privacidad</h3><p>Todas las personas tienen derecho a decidir qué comparten, con quién y en qué circunstancias.</p></div>
   <div class="card"><div class="card-icon">🤝</div><h3>Relaciones sanas</h3><p>Se construyen con confianza, comunicación, respeto mutuo y libertad, no con vigilancia o presión.</p></div>
   <div class="card"><div class="card-icon">💬</div><h3>Comunicación</h3><p>Hablar de límites, expectativas y preocupaciones permite construir vínculos más seguros.</p></div>
   <div class="card"><div class="card-icon">🌈</div><h3>Diversidad</h3><p>Respetar las diferencias significa evitar prejuicios y reconocer la dignidad de cada persona.</p></div>
   <div class="card"><div class="card-icon">🧭</div><h3>Autonomía</h3><p>Tienes derecho a tomar decisiones sobre tu cuerpo y tu vida sin presiones ni amenazas.</p></div>
  </div>
  <div class="content-box"><h3>Una idea para llevar contigo</h3><p>El amor, la amistad o la confianza no justifican controlar, presionar ni invadir la privacidad de otra persona. Un límite merece respeto, incluso cuando no estamos de acuerdo con él.</p></div>
 </section>

 <!-- BIENESTAR -->
 <section class="page" id="bienestar">
  <span class="pill">03 · AUTOCUIDADO Y EMOCIONES</span>
  <div class="section-head"><h2>Salud mental y bienestar</h2><p>Estar bien no significa sentirse bien todo el tiempo.</p></div>
  <div class="content-box">
   <h3>¿Qué significa cuidar la salud mental?</h3>
   <p>La salud mental está relacionada con nuestro bienestar emocional, psicológico y social. Influye en cómo pensamos, sentimos, nos relacionamos y enfrentamos las situaciones de la vida cotidiana.</p>
  </div>
  <div class="grid">
   <div class="card"><div class="card-icon">🌱</div><h3>Reconoce tus emociones</h3><p>Identificar lo que sientes puede ayudarte a comprender qué necesitas y cómo expresarlo.</p></div>
   <div class="card"><div class="card-icon">⏳</div><h3>Respeta tus tiempos</h3><p>No tienes que resolver todo de inmediato. Descansar también es una necesidad.</p></div>
   <div class="card"><div class="card-icon">🫂</div><h3>Busca apoyo</h3><p>Hablar con alguien de confianza o un profesional puede ayudarte a no enfrentar las dificultades en soledad.</p></div>
   <div class="card"><div class="card-icon">📵</div><h3>Cuida tu relación con las redes</h3><p>Tomar descansos y evitar comparaciones constantes puede favorecer tu bienestar.</p></div>
   <div class="card"><div class="card-icon">🧘</div><h3>Construye hábitos posibles</h3><p>El descanso, la alimentación, el movimiento y las actividades que disfrutas pueden contribuir a tu bienestar.</p></div>
   <div class="card"><div class="card-icon">💜</div><h3>Evita juzgarte</h3><p>Sentir tristeza, ansiedad o frustración no te hace débil ni significa que estés fallando.</p></div>
  </div>
  <div class="callout"><strong>Importante:</strong> esta información es educativa y no sustituye la atención de un profesional de salud mental.</div>
 </section>

 <!-- EXPERIENCIAS -->
 <section class="page" id="experiencias">
  <span class="pill">04 · VOCES Y PERSPECTIVAS</span>
  <div class="section-head"><h2>Experiencias compartidas</h2><p>Escuchar otras perspectivas puede ayudarnos a sentirnos acompañados y comprender realidades distintas.</p></div>
  <div class="tabs">
   <button class="tab active" onclick="showPanel('videos',this)">▶ Videos</button>
   <button class="tab" onclick="showPanel('historias',this)">✍ Compartir una historia</button>
  </div>
  <div id="videos">
   <div class="content-box">
    <h3>Historias que merecen ser escuchadas</h3>
    <p>Explora los videos disponibles. Los videos de demostración o los que agregue la administración aparecerán aquí.</p>
    <div id="videoStage" class="video-stage"><div style="color:white;text-align:center;padding:30px"><div style="font-size:38px">▶</div><p>Aún no hay videos publicados.</p></div></div>
    <div class="video-info"><h3 id="videoTitle">Entre Líneas</h3><p id="videoDescription">Un espacio para escuchar y reflexionar.</p></div>
    <div class="video-controls">
     <button class="btn btn-light btn-small" onclick="previousVideo()">← Anterior</button>
     <span id="videoCount" class="notice">0 videos</span>
     <button class="btn btn-light btn-small" onclick="nextVideo()">Siguiente →</button>
    </div>
   </div>
  </div>
  <div id="historias" class="hidden">
   <div class="content-box">
    <h3>Tu experiencia también cuenta 💌</h3>
    <p>Comparte una reflexión, una experiencia o un mensaje que pueda ayudar a otras personas.</p>
    <div class="field"><label for="storyTitle">Título de tu historia</label><input id="storyTitle" placeholder="Dale un título a tu experiencia"></div>
    <div class="field"><label for="storyTopic">Tema</label><select id="storyTopic"><option>Acoso y ciberacoso</option><option>Sexualidad y respeto</option><option>Salud mental y bienestar</option><option>Otra experiencia</option></select></div>
    <div class="field"><label for="storyName">¿Cómo quieres aparecer?</label><input id="storyName" placeholder="Puedes dejarlo vacío para compartir anónimamente"></div>
    <div class="field"><label for="storyText">Tu historia</label><textarea id="storyText" placeholder="Escribe lo que quieras compartir..." rows="5"></textarea></div>
    <button class="btn" onclick="submitStory()">Compartir mi historia ♡</button>
    <p class="notice">Este prototipo muestra las historias en el navegador actual. No cuenta con envío privado, moderación real ni publicación pública. Para recibir historias de forma segura y desde distintos dispositivos se necesita conectar un sistema de almacenamiento y revisión.</p>
   </div>
   <div class="content-box"><h3>Historias compartidas</h3><div id="storyList"><div class="empty">Todavía no hay historias en esta sesión. ¡Puedes iniciar la conversación!</div></div></div>
  </div>
 </section>

 <!-- INTERACTIVA -->
 <section class="page" id="interactiva">
  <span class="pill">05 · PARTICIPA Y REFLEXIONA</span>
  <div class="section-head"><h2>Zona interactiva</h2><p>Aprender también puede ser cuestionar, decidir y mirar una situación desde otra perspectiva.</p></div>
  <div class="tabs">
   <button class="tab active" onclick="showPanel('quiz',this)">⚡ ¿Qué tanto sabes?</button>
   <button class="tab" onclick="showPanel('dilemas',this)">💭 Dilemas sin filtro</button>
  </div>

  <div id="quiz">
   <div class="content-box">
    <span class="pill">MINI RETO</span>
    <h3>¿Qué tanto sabes?</h3>
    <p>Responde estas preguntas y descubre cuánto sabes sobre los temas de Entre Líneas.</p>
    <div id="quizArea"></div>
    <div class="video-controls" style="margin-top:20px">
     <span id="quizProgress" class="notice">Pregunta 1 de 5</span>
     <button class="btn" id="quizNext" onclick="nextQuestion()">Siguiente →</button>
    </div>
   </div>
  </div>

  <div id="dilemas" class="hidden">
   <div class="dilemma-intro">
    <span>💭</span>
    <h2>Dilemas sin filtro</h2>
    <p>La vida no siempre presenta situaciones con respuestas fáciles. Lee estos escenarios, ponte en el lugar de sus protagonistas y cuéntanos qué harías tú. No buscamos respuestas perfectas, sino opiniones auténticas.</p>
    <p><strong>Tu reflexión no será calificada.</strong> Lo importante es que puedas expresar tus ideas con libertad y respeto.</p>
   </div>

   <div class="dilemma-card">
    <div class="dilemma-top"><span class="dilemma-tag">🛡️ ACOSO Y CIBERACOSO</span><span class="dilemma-number">01 / 06</span></div>
    <h3>El secreto del grupo 🤐</h3>
    <div class="dilemma-story">Estás en un grupo de WhatsApp con tus amigos de la universidad. Una noche, alguien comparte una captura de pantalla de una conversación privada de una compañera y todos comienzan a burlarse de ella. Tú sabes que esa conversación no debía salir de su chat original. Cuando expresas que no te parece correcto, uno de tus amigos te responde: «No seas exagerado/a, todos nos reímos de todos». Además, temes que si sigues contradiciéndolos, terminen excluyéndote del grupo.</div>
    <p class="dilemma-question">¿Qué harías tú? ¿Defenderías a tu compañera aunque eso pudiera afectar tu relación con el grupo?</p>
    <textarea id="d1" placeholder="Cuéntanos cómo actuarías y qué te haría tomar esa decisión..."></textarea>
    <div class="dilemma-actions"><button class="dilemma-submit" onclick="reflect(1)">Ver otra perspectiva ♡</button></div>
    <div class="dilemma-hint" id="hint1"><strong>💡 Para seguir pensando...</strong>¿Hasta qué punto el miedo a no encajar puede hacer que participemos o guardemos silencio ante algo que sabemos que puede lastimar a otra persona?</div>
   </div>

   <div class="dilemma-card">
    <div class="dilemma-top"><span class="dilemma-tag">📱 ACOSO Y CIBERACOSO</span><span class="dilemma-number">02 / 06</span></div>
    <h3>La cuenta anónima 👀</h3>
    <div class="dilemma-story">En tu universidad comienza a hacerse popular una cuenta anónima donde publican confesiones, chismes y opiniones sobre estudiantes. Al principio, muchos la consideran entretenida. Sin embargo, una publicación empieza a circular con comentarios sobre el físico y la vida personal de una estudiante. La publicación recibe cientos de reacciones y algunos de tus conocidos la comparten. Incluso te ofrecen participar enviando una confesión.</div>
    <p class="dilemma-question">¿Participarías en esa cuenta? ¿Qué harías si descubrieras que alguien cercano está detrás de las publicaciones ofensivas?</p>
    <textarea id="d2" placeholder="Imagina que estás viviendo esta situación. ¿Qué decisión tomarías?"></textarea>
    <div class="dilemma-actions"><button class="dilemma-submit" onclick="reflect(2)">Ver otra perspectiva ♡</button></div>
    <div class="dilemma-hint" id="hint2"><strong>💡 Para seguir pensando...</strong>¿Ser anónimo en internet nos da derecho a publicar cualquier cosa? ¿Qué responsabilidad tenemos cuando compartimos contenido sobre otras personas?</div>
   </div>

   <div class="dilemma-card">
    <div class="dilemma-top"><span class="dilemma-tag">💗 SEXUALIDAD Y RESPETO</span><span class="dilemma-number">03 / 06</span></div>
    <h3>Una prueba de amor 🔐</h3>
    <div class="dilemma-story">Llevas varios meses en una relación. Un día, tu pareja te pide las contraseñas de tus redes sociales. Te dice que si realmente confías en ella no deberías tener problemas en compartirlas. Cuando te niegas, comienza a decir que seguramente escondes algo y que las parejas que se aman no tienen secretos. Empiezas a preguntarte si estás exagerando por querer conservar tu privacidad.</div>
    <p class="dilemma-question">¿Compartirías tus contraseñas para evitar un conflicto? ¿Cómo explicarías que tener privacidad no significa necesariamente ocultar algo?</p>
    <textarea id="d3" placeholder="¿Qué pensarías? ¿Qué límites establecerías?"></textarea>
    <div class="dilemma-actions"><button class="dilemma-submit" onclick="reflect(3)">Ver otra perspectiva ♡</button></div>
    <div class="dilemma-hint" id="hint3"><strong>💡 Para seguir pensando...</strong>¿Dónde termina la confianza y dónde comienza el control? ¿Es posible construir una relación sana sin renunciar a la privacidad?</div>
   </div>

   <div class="dilemma-card">
    <div class="dilemma-top"><span class="dilemma-tag">🤝 SEXUALIDAD Y RESPETO</span><span class="dilemma-number">04 / 06</span></div>
    <h3>La presión de los demás 🎭</h3>
    <div class="dilemma-story">Estás en una fiesta con personas de tu edad. Tus amigos comienzan a insistir en que bebas, aunque ya dijiste que no quieres. Después, una persona con la que estás hablando te propone ir a un lugar privado y tus amigos empiezan a hacer comentarios para presionarte. Te dicen que eres demasiado aburrido/a y que deberías dejar de pensar tanto. No quieres hacer nada con lo que no te sientas cómodo/a, pero tampoco quieres sentirte excluido/a.</div>
    <p class="dilemma-question">¿Cómo manejarías la presión? ¿Qué significa para ti tomar una decisión libre?</p>
    <textarea id="d4" placeholder="Cuéntanos cómo reaccionarías ante la presión de tus amigos..."></textarea>
    <div class="dilemma-actions"><button class="dilemma-submit" onclick="reflect(4)">Ver otra perspectiva ♡</button></div>
    <div class="dilemma-hint" id="hint4"><strong>💡 Para seguir pensando...</strong>¿Por qué a veces nos cuesta decir que no? ¿Cómo podemos respetar las decisiones de otras personas aunque sean diferentes a las nuestras?</div>
   </div>

   <div class="dilemma-card">
    <div class="dilemma-top"><span class="dilemma-tag">🌷 SALUD MENTAL</span><span class="dilemma-number">05 / 06</span></div>
    <h3>La sonrisa que engaña 🎭</h3>
    <div class="dilemma-story">Tienes un amigo que siempre es el más divertido del grupo. Hace bromas, participa en todas las actividades y parece tener una vida perfecta. Sin embargo, un día, mientras conversan, te dice que está agotado de fingir que todo está bien. Te confiesa que últimamente se siente solo, que tiene muchas preocupaciones y que no sabe cómo hablar de ello con los demás. Antes de irse, te pide que no le cuentes a nadie.</div>
    <p class="dilemma-question">¿Qué harías después de esa conversación? ¿Cómo podrías acompañarlo sin asumir que tienes que resolver todos sus problemas?</p>
    <textarea id="d5" placeholder="¿Qué le dirías? ¿Cómo podrías acompañarlo sin juzgarlo?"></textarea>
    <div class="dilemma-actions"><button class="dilemma-submit" onclick="reflect(5)">Ver otra perspectiva ♡</button></div>
    <div class="dilemma-hint" id="hint5"><strong>💡 Para seguir pensando...</strong>¿Cómo podemos respetar la privacidad de alguien y, al mismo tiempo, actuar si su seguridad podría estar en riesgo? ¿Qué papel puede tener el apoyo profesional?</div>
   </div>

   <div class="dilemma-card">
    <div class="dilemma-top"><span class="dilemma-tag">✨ SALUD MENTAL</span><span class="dilemma-number">06 / 06</span></div>
    <h3>Compararse hasta desaparecer 📲</h3>
    <div class="dilemma-story">Una compañera pasa gran parte de su tiempo viendo contenido de influencers y personas que muestran cuerpos, viajes, relaciones y estilos de vida aparentemente perfectos. Poco a poco comienza a sentirse inferior. Cambia su forma de vestir, evita aparecer en fotografías y deja de disfrutar actividades que antes le encantaban porque siente que nunca será suficiente. Cuando intentas hablar con ella, responde que solo está intentando mejorar su versión.</div>
    <p class="dilemma-question">¿Cómo abordarías esta conversación? ¿Crees que las redes sociales influyen en la manera en que construimos nuestra autoestima?</p>
    <textarea id="d6" placeholder="Comparte tu punto de vista y las ideas que le propondrías..."></textarea>
    <div class="dilemma-actions"><button class="dilemma-submit" onclick="reflect(6)">Ver otra perspectiva ♡</button></div>
    <div class="dilemma-hint" id="hint6"><strong>💡 Para seguir pensando...</strong>¿Cuánto de lo que vemos en redes representa la vida real? ¿Cómo podemos disfrutar de las redes sin convertirlas en una medida de nuestro valor personal?</div>
   </div>
   <div class="callout"><strong>♡ Recuerda:</strong> No hay una única respuesta correcta para estos dilemas. Tus experiencias, valores y perspectivas también forman parte de la conversación.</div>
  </div>
 </section>

 <!-- AYUDA -->
 <section class="page" id="ayuda">
  <span class="pill">06 · NO TIENES QUE HACERLO EN SOLEDAD</span>
  <div class="section-head"><h2>Orientación y ayuda</h2><p>Pedir apoyo es una decisión válida. No tienes que esperar a que una situación empeore para hablar de ella.</p></div>
  <div class="content-box">
   <h3>¿A quién puedes acudir?</h3>
   <div class="resource"><div class="resource-icon">🏫</div><div><h4>En tu institución educativa</h4><p>Consulta los servicios de bienestar universitario, orientación psicológica, coordinación o las rutas institucionales de atención.</p></div></div>
   <div class="resource"><div class="resource-icon">🫂</div><div><h4>Personas de confianza</h4><p>Un familiar, amigo, docente u otra persona que te escuche sin juzgarte puede ayudarte a dar el primer paso.</p></div></div>
   <div class="resource"><div class="resource-icon">🧠</div><div><h4>Profesionales de salud</h4><p>Un profesional puede orientarte y ayudarte a encontrar estrategias de acuerdo con tu situación.</p></div></div>
  </div>
  <div class="content-box">
   <h3>Recursos en Colombia</h3>
   <div class="resource"><div class="resource-icon">🚨</div><div><h4>Línea 123</h4><p>Línea de atención de emergencias en Colombia. Si existe peligro inmediato, busca ayuda urgente.</p></div></div>
   <div class="resource"><div class="resource-icon">🧒</div><div><h4>Línea 141 del ICBF</h4><p>Canal de orientación y protección para niños, niñas y adolescentes.</p></div></div>
  </div>
  <div class="callout"><strong>Importante:</strong> Entre Líneas es un proyecto educativo e informativo. No es un servicio de atención psicológica, médica ni de emergencias.</div>
 </section>

 <!-- ADMINISTRACIÓN -->
 <section class="page" id="admin">
  <div class="admin-box">
   <div class="admin-top">
    <div><span class="pill">GESTIÓN DEL SITIO</span><h2 style="color:var(--deep)">Administración</h2></div>
    <button class="btn btn-light btn-small" onclick="go('inicio')">← Volver al inicio</button>
   </div>
   <div id="adminLogin" class="content-box">
    <h3>Acceso administrativo 🔐</h3>
    <p>Ingresa la contraseña para gestionar el contenido de la página.</p>
    <div class="field"><label>Contraseña</label><input id="adminPassword" type="password" placeholder="Contraseña de administrador"></div>
    <button class="btn" onclick="loginAdmin()">Ingresar</button>
    <p class="notice">Demo: la contraseña incluida en este código es visible en el código fuente. No utilices esta versión como sistema de administración seguro en una página pública.</p>
   </div>
   <div id="adminPanel" class="hidden">
    <div class="content-box">
     <h3>🎬 Administrar videos</h3>
     <div class="field"><label>Título del video</label><input id="newVideoTitle" placeholder="Título"></div>
     <div class="field"><label>Descripción</label><input id="newVideoDesc" placeholder="Descripción breve"></div>
     <div class="field"><label>Seleccionar archivo de video</label><input type="file" id="newVideoFile" accept="video/*"></div>
     <button class="btn" onclick="addVideo()">Agregar video</button>
     <div id="adminVideoList" class="video-list"></div>
    </div>
    <div class="content-box">
     <h3>💬 Historias recibidas en esta sesión</h3>
     <div id="adminStoryList"><div class="empty">No hay historias todavía.</div></div>
    </div>
    <button class="btn btn-light" onclick="logoutAdmin()">Cerrar sesión</button>
   </div>
  </div>
 </section>

 <footer>Entre Líneas · Un espacio para escucharnos, aprender y respetarnos ♡</footer>
</main>
</div>

<script>
/* NAVEGACIÓN */
function go(id,button){
 document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
 const page=document.getElementById(id);
 if(page) page.classList.add('active');
 document.querySelectorAll('.nav-btn').forEach(b=>b.classList.remove('active'));
 if(button && button.classList.contains('nav-btn')) button.classList.add('active');
 else{
  const nav=[...document.querySelectorAll('.nav-btn')].find(b=>b.getAttribute('onclick')?.includes("'"+id+"'"));
  if(nav)nav.classList.add('active');
 }
 window.scrollTo({top:0,behavior:'smooth'});
}
function showPanel(id,button){
 const parent=button.closest('.page');
 parent.querySelectorAll(':scope > .tabs ~ div').forEach(el=>el.classList.add('hidden'));
 const target=document.getElementById(id);
 if(target)target.classList.remove('hidden');
 parent.querySelectorAll('.tabs .tab').forEach(b=>b.classList.remove('active'));
 button.classList.add('active');
}

/* DILEMAS */
function reflect(n){
 const area=document.getElementById('d'+n);
 const hint=document.getElementById('hint'+n);
 if(!area.value.trim()){
  area.focus();
  hint.style.display='block';
  hint.innerHTML='<strong>♡ Antes de continuar...</strong>Escribe primero tu reflexión. No tiene que ser perfecta: queremos conocer tu punto de vista.';
  return;
 }
 hint.style.display='block';
 hint.scrollIntoView({behavior:'smooth',block:'nearest'});
}

/* CUESTIONARIO */
const questions=[
 {q:'¿Qué debes hacer si recibes una imagen íntima de otra persona sin su consentimiento?',a:['Compartirla con tus amigos','No difundirla y buscar orientación si es necesario','Guardarla para hacer bromas'],correct:1,why:'La intimidad y la privacidad deben respetarse. No difundas contenido íntimo sin consentimiento.'},
 {q:'¿Cuál de estas situaciones representa una relación basada en el respeto?',a:['Revisar el celular de la pareja','Exigir contraseñas como prueba de amor','Respetar los límites y la privacidad'],correct:2,why:'La confianza no exige renunciar a la privacidad. Los límites personales merecen respeto.'},
 {q:'Un compañero te cuenta que está atravesando un momento difícil. ¿Qué puedes hacer?',a:['Escucharlo sin juzgar y orientarlo para buscar apoyo','Decirle que no es para tanto','Contarle a todo el grupo'],correct:0,why:'Escuchar y acompañar puede ser importante. No tienes que resolverlo todo: también puedes orientarlo hacia apoyo profesional.'},
 {q:'¿Qué es el consentimiento?',a:['Aceptar para evitar una discusión','Una decisión libre que puede cambiarse','Algo que se supone cuando existe una relación'],correct:1,why:'El consentimiento debe ser libre, informado y reversible. Una relación no elimina ese derecho.'},
 {q:'¿Qué puedes hacer ante una publicación que humilla a alguien?',a:['Compartirla para conocer opiniones','Comentar con más burlas','Evitar difundirla y utilizar los canales de reporte'],correct:2,why:'No amplificar el contenido ayuda a evitar que la situación siga creciendo.'}
];
let qIndex=0,score=0,answered=false;
function renderQuestion(){
 const q=questions[qIndex];
 answered=false;
 document.getElementById('quizArea').innerHTML=
 '<p class="quiz-question">'+(qIndex+1)+'. '+q.q+'</p>'+
 q.a.map((a,i)=>'<button class="quiz-option" onclick="answerQuestion('+i+',this)">'+a+'</button>').join('')+
 '<div class="quiz-feedback" id="quizFeedback"></div>';
 document.getElementById('quizProgress').textContent='Pregunta '+(qIndex+1)+' de '+questions.length;
 document.getElementById('quizNext').textContent=qIndex===questions.length-1?'Ver resultado':'Siguiente →';
}
function answerQuestion(i,button){
 if(answered)return;
 answered=true;
 const q=questions[qIndex];
 const options=document.querySelectorAll('.quiz-option');
 options.forEach((b,index)=>{
  if(index===q.correct)b.classList.add('selected');
 });
 const good=i===q.correct;
 if(good)score++;
 document.getElementById('quizFeedback').innerHTML='<strong>'+(good?'¡Muy bien! ♡':'¡Sigue aprendiendo!')+'</strong><br>'+q.why;
}
function nextQuestion(){
 if(!answered){
  document.getElementById('quizFeedback').textContent='Selecciona una respuesta para continuar.';
  return;
 }
 if(qIndex<questions.length-1){qIndex++;renderQuestion();}
 else{
  document.getElementById('quizArea').innerHTML='<div class="callout"><h3>¡Terminaste! ♡</h3><p>Tu resultado es <strong>'+score+' de '+questions.length+'</strong>.</p><p>Más allá del puntaje, lo importante es seguir cuestionando, aprendiendo y construyendo espacios respetuosos.</p><button class="btn" onclick="restartQuiz()">Volver a intentarlo</button></div>';
  document.getElementById('quizProgress').textContent='Actividad completada';
  document.getElementById('quizNext').style.display='none';
 }
}
function restartQuiz(){qIndex=0;score=0;document.getElementById('quizNext').style.display='';renderQuestion();}
renderQuestion();

/* EXPERIENCIAS ESCRITAS */
let stories=[];
function submitStory(){
 const title=document.getElementById('storyTitle').value.trim();
 const topic=document.getElementById('storyTopic').value;
 const name=document.getElementById('storyName').value.trim()||'Anónimo/a';
 const content=document.getElementById('storyText').value.trim();
 if(!title||!content){alert('Por favor, completa el título y tu historia.');return;}
 stories.unshift({title,topic,name,content});
 document.getElementById('storyTitle').value='';
 document.getElementById('storyName').value='';
 document.getElementById('storyText').value='';
 renderStories();
 alert('Tu reflexión se ha añadido a esta demostración. ♡');
}
function renderStories(){
 const html=stories.map((s,i)=>'<div class="story-item"><span class="pill">'+escapeHTML(s.topic)+'</span><h4>'+escapeHTML(s.title)+'</h4><p>'+escapeHTML(s.content)+'</p><small class="notice">Compartido por '+escapeHTML(s.name)+'</small></div>').join('');
 document.getElementById('storyList').innerHTML=html||'<div class="empty">Todavía no hay historias en esta sesión.</div>';
 const admin=document.getElementById('adminStoryList');
 if(admin)admin.innerHTML=stories.map((s,i)=>'<div class="story-item"><h4>'+escapeHTML(s.title)+'</h4><p>'+escapeHTML(s.content)+'</p><small>'+escapeHTML(s.name)+' · '+escapeHTML(s.topic)+'</small><br><button class="btn btn-small" style="margin-top:10px" onclick="deleteStory('+i+')">Eliminar</button></div>').join('')||'<div class="empty">No hay historias todavía.</div>';
}
function deleteStory(i){stories.splice(i,1);renderStories();}
function escapeHTML(value){
 return String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

/* ADMINISTRACIÓN DE VIDEOS */
let videos=[],videoIndex=0,adminOpen=false;
function loginAdmin(){
 // Contraseña de demostración. Reemplazar por autenticación segura en producción.
 if(document.getElementById('adminPassword').value==='EntreLineas2026'){
  adminOpen=true;
  document.getElementById('adminLogin').classList.add('hidden');
  document.getElementById('adminPanel').classList.remove('hidden');
  renderAdminVideos();
 }else alert('Contraseña incorrecta.');
}
function logoutAdmin(){
 adminOpen=false;
 document.getElementById('adminPanel').classList.add('hidden');
 document.getElementById('adminLogin').classList.remove('hidden');
 document.getElementById('adminPassword').value='';
}
function addVideo(){
 if(!adminOpen)return;
 const file=document.getElementById('newVideoFile').files[0];
 const title=document.getElementById('newVideoTitle').value.trim();
 const desc=document.getElementById('newVideoDesc').value.trim();
 if(!file||!title){alert('Agrega un título y selecciona un video.');return;}
 if(!file.type.startsWith('video/')){alert('Selecciona un archivo de video válido.');return;}
 const url=URL.createObjectURL(file);
 videos.push({title,desc,url,fileName:file.name});
 document.getElementById('newVideoTitle').value='';
 document.getElementById('newVideoDesc').value='';
 document.getElementById('newVideoFile').value='';
 videoIndex=videos.length-1;
 renderVideos();
 renderAdminVideos();
}
function renderVideos(){
 const stage=document.getElementById('videoStage');
 const count=document.getElementById('videoCount');
 count.textContent=videos.length+' video(s)';
 if(!videos.length){
  stage.innerHTML='<div style="color:white;text-align:center;padding:30px"><div style="font-size:38px">▶</div><p>Aún no hay videos publicados.</p></div>';
  document.getElementById('videoTitle').textContent='Entre Líneas';
  document.getElementById('videoDescription').textContent='Un espacio para escuchar y reflexionar.';
  return;
 }
 videoIndex=(videoIndex+videos.length)%videos.length;
 const v=videos[videoIndex];
 stage.innerHTML='';
 const player=document.createElement('video');
 player.src=v.url;player.controls=true;player.playsInline=true;
 stage.appendChild(player);
 document.getElementById('videoTitle').textContent=v.title;
 document.getElementById('videoDescription').textContent=v.desc||'Una experiencia compartida.';
}
function nextVideo(){if(videos.length){videoIndex++;renderVideos();}}
function previousVideo(){if(videos.length){videoIndex--;renderVideos();}}
function renderAdminVideos(){
 document.getElementById('adminVideoList').innerHTML=videos.map((v,i)=>'<div class="video-item"><span>'+escapeHTML(v.title)+'</span><button class="btn btn-small" onclick="deleteVideo('+i+')">Eliminar</button></div>').join('')||'<div class="empty">Todavía no hay videos.</div>';
}
function deleteVideo(i){
 if(!adminOpen)return;
 URL.revokeObjectURL(videos[i].url);
 videos.splice(i,1);
 videoIndex=0;
 renderVideos();
 renderAdminVideos();
}
renderVideos();
</script>
</body>
</html>
