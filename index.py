from IPython.display import display, HTML, Image

HTML("<h1 style='color:blue;>Este es un título en azul</h1>")

html_content1 = """
<div class="title_home">
    <h2 class="title">Subtítulo en verde</h2>
    <p>Este es un párrafo con <strong>negrita</strong> y tamaño de letra ajustado.</p>
    <div class="content-informacion">
                <!-- Título principal alineado al centro -->
                <h1 align="center">Hi 👋<br> I'M STUDENT <br> UNIVERSIDAD AUTÓNOMA DE CHIRIQUÍ</h1>
                <!-- Subtítulo alineado al centro -->
                <h3 align="center">TÉCNICO EN PROGRAMACIÓN EMPRESARIAL</h3>

                <!-- Sección para conectar con la universidad -->
                <h3 align="center">Connect with me:</h3>

                <!-- Sección de lenguajes y herramientas -->
                <h3 align="center">Languages and Tools:</h3>
            </div>
            
            
             <h4 align="left">Languages:</h4>
                <div class="card-list">
                    <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer" class="card-item">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg"
                            alt="C++" width="40" height="40">
                        <span class="developer">C++</span>
                        <h3>Un lenguaje potente para el desarrollo de sistemas/software y programación de juegos.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>
                    <a href="https://www.php.net/" target="_blank" rel="noreferrer" class="card-item">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg"
                            alt="PHP" width="40" height="40">
                        <span class="developer">PHP</span>
                        <h3>Un popular lenguaje de programación de uso general para el desarrollo web.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>
                    <a href="https://www.python.org" target="_blank" rel="noreferrer" class="card-item">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"
                            alt="Python" width="40" height="40">
                        <span class="developer">Python</span>
                        <h3>Un lenguaje versátil conocido por su simplicidad y legibilidad.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>
                    <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer" class="card-item">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"
                            alt="HTML5" width="40" height="40">
                        <span class="developer">HTML5</span>
                        <h3>El lenguaje de marcado estándar para crear páginas web.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>
                    <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer" class="card-item">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg"
                            alt="CSS3" width="40" height="40">
                        <span class="designer">CSS3</span>
                        <h3>Dale estilo a la web con diseños y diseños visualmente atractivos.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>

                    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"
                        class="card-item">
                        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg"
                            alt="JavaScript" width="40" height="40">
                        <span class="developer">JavaScript</span>
                        <h3>El lenguaje de programación de la Web, que permite contenido dinámico.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>

                </div>

                <!-- Card list for Frameworks -->
                <h4 align="left">Frameworks:</h4>
                <div class="card-list">
                    <a href="https://getbootstrap.com" target="_blank" rel="noreferrer" class="card-item">
                        <img src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo-shadow.png"
                            alt="Bootstrap" width="40" height="40" / style="color: #fff;">
                        <span class="developer">Bootstrap</span>
                        <h3>Un marco de trabajo front-end para desarrollar sitios web responsivos y orientados a
                            dispositivos móviles.</h3>
                        <div class="arrow">
                            <i class="fas fa-arrow-right card-icon"></i>
                        </div>
                    </a>
                </div>
</div>
"""

css_styles = """
<style>
    .title_hero{
        border: 1px solid white;
        padding: 10px;
    }
    .content-informacion {
      align-items: center;
      justify-content: center;
      border: 2px solid rgba(249,38,225,.2);
      border-radius: 20px;
      padding: 20px;
      margin: 14px;
      color: #0056b3;
}
.content {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 50px;
}

.card-list {
   
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    row-gap: 20px;
    column-gap: 20px;
    margin: 22px auto;
    max-width: 800px;
}

.card-item {
    background-image: linear-gradient(90deg, #000, #fff);
    background-color: #f9f9f9;
    border-radius: 8px;
    text-align: center;
    padding: 10px;
    width: 340px;
    text-decoration: none;
    color: var(--text-light);
    transition: all 0.3s ease;
}
.card-item span {
    display: flex;
    text-align: center;
    justify-content: center;
    margin: 12px;
    font-weight: bold;
}
.card-item:hover {
    transform: translateY(-12px);
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(255, 254, 254, 0.733);
}

.card-item img {
    margin-bottom: 15px;
    max-width: 100%;
    color: var(--text-light);
}


.card-item h3 {
    color: var(--text-light);
    font-size: 18px;
    margin-bottom: 10px;
}

.card-item .arrow {
    margin-top: 10px;
    font-size: 18px;
    color: var(--text-light);

}
    ul {
        color: darkred;
    }
    p {
        color: gray;
        font-size: 16px;
    }
    .title {
        color:green;
    }
    .custom-title {
        color: purple;
        font-size: 24px;
    }
    .custom-paragraph {
        font-family: Arial, sans-serif;
        font-size: 18px;
    }
</style>
"""

html_content2 = """
<h2 class="custom-title">Título con clase personalizada</h2>
<p class="custom-paragraph">Este es un párrafo con estilos aplicados desde el CSS.</p>
"""

display(HTML(css_styles + html_content1 + html_content2))



# Mostrar una imagen desde una URL
display(Image(url="https://www.python.org/static/community_logos/python-logo.png"))






