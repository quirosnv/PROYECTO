#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.sax
from flask import Flask
from flask import render_template

app = Flask (__name__)
@app.route('/') #Responde al entrar al local host 5000
def index ():
    pelicula = "Directorior: Robert Rodriguez"
    duracion = "Duracion: 122 minutos"

    return render_template('index.html' ) #regresa string

if __name__ == '__main__':
    app.run(debug = True, port = 8000) #se encarga de ejecutar en el servidor por defecto el 5000
