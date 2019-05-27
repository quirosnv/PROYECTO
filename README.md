# PROYECTO
LENGUAJE MARCAS
## **PROYECTO LENGUAJE MARCAS**

## Introduction

> El siguiente proyecto  esta basado en la aplicación de los conocimientos aprendidos durante el curso 2019 con el profesor Carlos Gonzáles de Lenguaje de Marcas.
Los diferentes tipos de lenguajes utilizados para llevar a cabo el proyecto son **HTML,CSS,XML,XSL,JAVASCRIPT** y un poco 
de **PYTHON.**

> Durante el desarrollo del proyecto tuvimos muchos contras ya que es dificil  enlazar los diferentes documentos dentro de otros con ext diferentes, ya que no hemos utilizado anaconda el cual se nos pedia.

> Anaconda lo descargamos en el ordenador pero no nos trabajaba bien ya que no nos abria el archivo y teniamos que actualizar y formatear.
> Antes de crear la pagina web hemos creado un reproductor de musica pero no lograbamos enlazar la base de datos de xml, ya que es el que se nos pide y con ese reproductor habiamos utilizado **Pycharm, python, pygame, mixer y tkinter** en esta parte nos dio un reproductor pero sin la base de datos de xml, así que cambiamos a utilizar solo **Pycharm, Python y el xml** pero vimos que era muy simple y no tenia mas interfaz. (ya que se nos pedia utilizar todo lo que hemos aprendido durante el año)

> Viendo que el tiempo corria en nuestra contra decidimos cambiar el proyecto el cual decidimos realizar un catalogo de películas en donde nos redirige a una pagina web y nos salen las películas tipo cartelera en donde cada una de ellas tiene su información (dada por el xml) y dándole click sobre ella nos redirige a un link del trailer de cada una de ella
Esto lo estamos haciendo con Python: 
Utilizando el **framework flask, para renderizar las plantillas(templates)
html y css). Retorna una app.py y  se compila en cmd**.  

> Es necesario recalcar que poco a poco fuimos resolviendo los errores.

## Code Samples

**PARTE PYTHON**
> #!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask (__name__)
@app.route('/') #Responde al entrar al local host 5000
def index ():
    return render_template('index.html') #regresa string
if __name__ == '__main__':
    app.run(debug = True, port = 8000) #se encarga de ejecutar en el servidor por defecto el 5000
    

**JavaScript**
> <script>
           			if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
           				xmlhttp = new XMLHttpRequest();
           			} else {// code for IE6, IE5
           				xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
           			}
           			xmlhttp.open("GET", "{{ url_for('static', filename='xml/Biblioteca.xml')}}", false);
           			xmlhttp.send();
           			xmlDoc = xmlhttp.responseXML;

           			document.write("<p id="2"");
           			var x = xmlDoc.getElementsByTagName("MAD");
           			for ( i = 0; i < x.length; i++) {
           				document.write("<br><p><t>");
           				document.write(x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue);
           				document.write("<br></td><td>");
           				document.write(x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue);
           				document.write("<br></td></t>");
           			}
           			document.write("</p>");
           		</script>

**PARTE DE HTML**
> <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css')}}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/6.3.1/flexboxgrid.min.css">

**PARTE CCS**

> < .body{
  padding-top: 50px;
  padding-bottom: 60px;
  background: ;
}

.menu {
  background: linear-gradient(); /*dos colores o mas*/
  background:  #00091a;
  padding-left: 15px;
  padding-right: 15px;
  padding-top: 10px;
  padding-bottom: 10px;
  margin-top: 1em;
  border-radius: 6px;
} >

**PARTE XML**

<<?xml version="1.0" encoding="UTF-8"?>
<cine>
    <pelicula categoria="accion">
        <titulo idioma="ingles">Mad Max</titulo>
        <director>George Miller</director>
       <duracion>93 minutos</duracion>
        <clasificacion>R</clasificacion>
        <estreno>15 mayo 2015</estreno>
        <reparto>Tom Hardy</reparto>
        <reparto>Charlize Theron</reparto>
        <reparto>Nicholas Hoult</reparto>
    </pelicula>>



> Algunos pocos códigos que se pueden ver al inspeccionar el código de la pagina web.


## Installation

>* Primero, ha de crearse una base de datos con XML.

>* Segundo, crear el HTML con CSS para lograr el estilo de la página Web a la que queremos salir.

>* Enlazar los diferentes documentos para optener una interfaz gráfica agradable y que la base de datos sea xml desde un principio.

>* Utilizando el framework **(Frameworks que son herramientas que nos dan un esquema de trabajo y una serie de utilidades y funciones que nos facilita y nos abstrae de la construcción de páginas web dinámicas.(conjunto de herramientas))** flask **(Flask es un “micro” Framework escrito en Python y concebido para facilitar el desarrollo de Aplicaciones Web bajo el patrón MVC.)**, para renderizar las plantillas(templates) html y css. Retorna una app.py y  se compila en cmd.

**Instalar python3**

>* Procedimiento
 
1.- Ir a https://www.python.org/downloads/release/python-373/
2.- Pinchar sobre "Windows x86-64 executable installer"
3.- Doble click sobre el fichero descargado llamado "python-3.7.3-amd64"
4.- Instalar sobre el directorio c:\Python\Python37


Instalar prerrequisitos
1.- Instalar Flask con el siguiente comando:

c:\Python\Python37\python.exe -m pip install Flask


Ejecutar proyecto

1.- Descargar fichero PyWeb.rar
2.- Desempaquetar en c:\
3.- Ejecutar la siguiente orden:

c:\Python\Python37\python.exe c:\PyWeb\app.py

4.- Abrir navegador e ir a http://127.0.0.1:8000
.



