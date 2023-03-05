![Project Status](https://badgen.net/badge/Development/Paused/orange)
![Python Version](https://badgen.net/badge/Python/3.11/blue)
![License](https://badgen.net/badge/License/CC-BY-NC-ND-2.0/cyan)

<p align="center">
  <img src="https://user-images.githubusercontent.com/20795201/222973381-32c97bdf-502d-4067-bbe4-568259a807ee.gif">
</p>

# Knives out 🕵🏼‍♂️💀

Eres un detective que debe resolver el asesinato ocurrido en la mansion de la familia Blackwood, en cabeza de Bruno B.

Se trata de un grupo de amigos los cuales, al verse envueltos en líos amorosos y problemas legales tienen motivos para asesinar a uno de sus compañeros, unos más probables que otros.

Knives Out 🕵🏼‍♂️💀 es una historia visual, basada en la pelicula del mismo nombre, donde el usuario, en la piel de un detective tiene que resolver el misterio de un asesinato en la mansión Blackwood sumergido entre estimulos visuales como imagenes y música de fondo para sumergir al usuario dentro de esta trama.

## Contexto

Proyecto final de la materia Introducción a la Inteligencia Artificial, parte del programa de Ingeniería Mecatrónica de la [Universidad Nacional Sede La Paz](http://delapaz.unal.edu.co/) bajo el modelo de colaboratorio de creación.
Se requiere crear un agente computacional que utilice los cuatro (4) conceptos desarrollados en clase:
- Proceso de búsqueda.
- Análisis lógico.
- Inferencia.
- Aprendizaje.

Asi como algunas librerias provistas, como lo son _pomegranate.py_ y _logic.py_. Para leer un poco más sobre el proyecto, mirar [esta diapositiva](https://github.com/dfzunigah/AI_LaPaz/blob/main/Proyecto%20Final/Complementary/Presentaci%C3%B3n%20-%20Proyecto%20final.pdf)

## Instalación

**1.** Clonar [este repositorio](https://github.com/dfzunigah/AI_LaPaz):

```bash
git clone https://github.com/dfzunigah/AI_LaPaz.git
```

O descargarlo el archivo comprimido.

**2.** Dentro de este repositorio, ubicarse en la carpeta **Proyecto Final**.

**3.** Abrir Google Colab. Si no sabes cómo, [aquí hay una guía](https://www.educative.io/answers/how-to-create-a-notebook-in-google-colab).

> NOTA⚠️: Recomendamos ejecutar este programa en Google Colab, otras plataformas pueden causar problemas con la instalación de las librerias.

**4.** Copiar el contenido de la carpeta **Proyecto Final**, en el Colab.

* Para ello, al lado izquierdo del cuaderno, abrir el menú lateral 🔵, luego pulsar el icono con forma de carpeta 🟢 y por último pulsar el primer icono 🟡 (de un archivo con una flecha) o también arrastre el contenido hasta este menú:

<img src="https://i.stack.imgur.com/L2iwc.png" width="450" height="391">

> NOTA #1⚠️: Cada vez que se abra el Colab es necesario volver a subir los archivos, pues la instancia del Colab se reinicia.

> NOTA #2⚠️: Asegurarse que al final quedes con una organización así: imagen de lo que tiene que estar incluido

```bash
/
├─ Visuals/
│  ├─ Intro.gif
│  ├─ Image1.webp
│  ├─ Image2.webp
│  ├─ Image3.webp
│  ├─ Image4.webp
│  ├─ Image5.webp
│  ├─ Image6.webp
│  ├─ badx.png
│  ├─ goodx.png
├─ Complementary/
│  ├─ Presentación - Proyecto final.pdf
│  ├─ Red Bayesiana.pdf
├─ Knives Out v2.0.ipynb
├─ Bayesian.py
├─ Learning.py
├─ Logic.py
├─ Search.py
├─ changelog.md
├─ README.md
```

## Uso

**1.** Ya con los archivos subidos, abrir el archivo **Knives Out.ipynb**, este es el archivo principal desde donde ejecutaremos la historia.

**2.** Instalar la libreria _pomegranate_, esta librería la usaremos para realizar cálculos probabilisticos posteriormente.

```python
pip install pomegranate
```

> NOTA⚠️: Esta instrucción puede tomar algunos minutos, aproximadamente 5.

**3.** Mientras se instala la librería, aprovechamos para configurar los elementos realizar una experiencia más inmersiva.

- Colocar el estilo oscuro o Dark en Google Colab.
- Colapsar los menús superior y lateral, de modo que se tenga la mayor cantidad de espacio para visualizar las imagenes.
- En otra pestaña, reproducir [esta música 🎶](https://www.youtube.com/watch?v=w5FX0kXTLhM). Recomendamos utilizar audifonos 🎧.
- Usar en pantalla completa.

**4.** Una vez instalada la liberia, podemos inicar nuestra historia inmersiva. ¡Disfruta!

> NOTA #1⚠️: Las primeras celdas de texto, te darán un contexto de la historia que se está desarrollando, presta atención a ellas.

> NOTA #2⚠️: Ejecuta las instrucciones de manera secuencial, una detrás de otra.

**5:** Algunos screenshoots de las salidas correctas al ejecutar las celdas interactivas:

```bash
▶️Generamos evidencias al azar

[[Habitación de Jeff],
 [Sala de estár, Greta],
 [Cocina],
 [Patio, Podrick, Hacha],
 [Habitacion de Bruno, Alfred],
 [Comedor, Teresa, Revolver],
 [Habitacion de huéspedes, Jeff, Veneno],
 [Sotano],
 [Balcón, Elon, Cuchillo]]
```
```bash
▶️Parametros del juego

Busqueda
['revisando', 'right', 'revisando', 'right', 'revisando', 'down', 'revisando', 'left', 'revisando', 'left', 'revisando', 'down', 'revisando', 'right', 'revisando', 'right', 'revisando']

Sospechosos
[[Comedor, Teresa, Revolver], [Patio, Podrick, Hacha], [Habitacion de huéspedes, Jeff, Veneno], [Balcón, Elon, Cuchillo]]
```
```bash
▶️Comprobamos lo que sabemos hasta el momento

Greta: TAL VEZ
Teresa: TAL VEZ
Alfred: TAL VEZ
Comedor: TAL VEZ
Habitación de Jeff: TAL VEZ
Habitacion de Bruno: TAL VEZ
Revolver: TAL VEZ
Hacha: TAL VEZ
Cuchillo: TAL VEZ
```
```bash
▶️¿Quién será el culpable?

[[Teresa, '0.13'], [Podrick, '0.46'], [Jeff, '0.43'], [Elon, '0.43']]
[Podrick, '0.46']

Podrick: SI

Patio: SI

Hacha: SI
```
```bash
▶️¿Es nuestra predicción acertada de acuerdo a nuestra experiencia?

Esperabamos 1, conseguimos 1.
```

<img src="https://user-images.githubusercontent.com/20795201/222972838-5e714da9-1b38-4f54-b899-2b1b4ac3fa3d.png" width="450" height="391"><img src="https://user-images.githubusercontent.com/20795201/222972898-7019fc32-c716-4c1a-b931-5896b548bb1c.png" width="450" height="391">

**6.** Para ejecutar de nuevo la historia:

- Si sigues en la misma instancia del Colab (es decir, no has cerrado la pestaña, recargado el Colab, apagado el computador o no ha pasado más de una hora desde la última ejecución), vuelve a correr desde la segunda (2da) celda ejecutable, es decir, desde _Traemos los módulos adicionales que hemos creado_
- En caso de que el Colab se haya desconectado o se haya reiniciado la instancia (es decir, cerraste la pestaña, recargaste el Colab, apagaste el computador o ha pasado más de una hora desde la última ejecución) será necesario reinstalar la librería _pomegranate_, es decir, ejecutar el código desde la primera celda ejecutable.

## Resolución de problemas

- **Tengo problemas instalando la libreria _pomegranate_:** Sugerimos utilizar Google Colab, ya que en nuestra experiencia no tiene problemas al instalar _el módulo pomegranate_, como si pasa con todos los demás entornos de desarrollo (IDEs).
- **El Google Colab no inicia, se queda colgado:** Cierra sesión de Google e intentalo de nuevo.
- **Al final de la historia, me salen dos (2) personajes con las mismas probabilidades:** Esto no es un error, es una posibilidad. El algoritmo siempre eligirá al primer candidato.
- **Al final de la historia, sale 'Tal vez' en lugar de 'Sí':** Vuelve a correr el Colab, esto sucede a veces porque se quedan variables guardadas que pueden intervenir en la correcta ejecución del código.

## Soporte

Contactar alguno de los siguientes correos: [Felipe Zuñiga](mailto:dfzunigah@unal.edu.co), [Andres Peralta](mailto:aperaltaf@unal.edu.co), [Sergio Guzman](mailto:seguzmanc@unal.edu.co) 

## TODO's

- Estructurar mejor el código, eliminar redundancias.
- Solucionar el problema para instalar la librerira _pomegranate_ y así poder portar a otras plataformas.
- Agregar elementos visuales a la historia.
- Agregar interacción del usuario.
- Eliminar la necesidad de cargar los archivos cada vez que se inicie el proyecto.

## Contribuir

Estamos abiertos a contribuciones, pero esperamos que sean discutidas primero con el equipo desarrollador.

## Licencia

[CC-BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/). Este trabajo se puede compartir, para desarrollar o contribuir sobre él, por favor ponerse en contacto con los autores.

## Autores 

- [Felipe Zuñiga](https://github.com/dfzunigah), estudiante de ingeniería mecatrónica Sede Bogotá.
- [Andres Peralta](https://github.com/Andres0047), estudiante de ingeniería mecatrónica Sede La Paz.
- [Sergio Guzman](), estudiante de ingeniería mecatrónica Sede La Paz.

## Menciones

- Agradecemos a los profesores [Juan Pablo Hoyos](mailto:jhoyoss@unal.edu.co) y [Jose Francisco Ruiz Muñoz](mailto:jfruizmu@unal.edu.co) por la retroalimentación y guía en el proyecto.
- Se utilizó [Make a README](https://www.makeareadme.com/) como una guía para crear este README.
- Se implementó la [Guía de documentación de Google](https://github.com/goog[le/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) junto a [esta guía complementaria](https://realpython.com/documenting-python-code/) para documentar el código.
- Todas las imagenes utilizadas se generaron a través de Stable Diffusion.
