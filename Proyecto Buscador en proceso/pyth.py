#!/usr/bin/python3
import xml.sax #libreria sax

print("Playlist")


class MovieHandler(xml.sax.ContentHandler):  #Etiquetas llamadas del xml
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # Se llaman cuando el elemento empieza
    def startElement(self, tag, attributes): #la funcion tendra la etiqueta y a su vez su atributo para iniciar
        self.CurrentData = tag
        if tag == "movie": #Etiqueta a llamar
            print("\n*****Song*****\n")
            title = attributes["title"] #Atributo llamado de la etiqueta
            print("Artist:", title) #atributo impreso

    # Llamadas cuando el elemento finaliza
    def endElement(self, tag):
        if self.CurrentData == "type": #Etiqueta llamada
            print("Title:", self.type) #Etiqueta impresa
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Album:", self.year)
        elif self.CurrentData == "rating":
            print("Year:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # Se llama cuando un caracter se lea
    def characters(self, content):
        if self.CurrentData == "type": #si CurrentData es igual a TYPE
            self.type = content        #Del objeto type asignar a content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    #Xml que se lea
    parser = xml.sax.make_parser()
    # apagar namespces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # Anular el predeterminado ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("list.xml") #Se llama el xml y se parsea


#Se le pide instrucciones por teclado al usuario (Buscador)
data = int(input("\nIngrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))
contador = 0
while data != -1: #Continuar mientras no se introduzca -1
    if data == 1:
        print("Eligio buscar por cantante:")
        cant = input("Ingrese el nombre de un cantante o banda, para ser buscado: ")
        if cant == 'kaleo':
            print("Cancion: Way Down we go")
        if cant == 'beatles' or 'the beatles':
            print("Cancion: Let It Be\n","Cancion: Love Me Do\n", "Cancion: Love me" )
        if cant == 'lp':
            print("Cancion: Lost On You")
        if cant == 'status quo':
            print("Cancion: In the Army Now\n", "Cancion: Calling\n", "Cancion: Red Sky\n" )
        if cant == 'coldplay':
            print("Cancion: Yellow\n", "Cancion: Parachutes\n", "Cancion: Truples\n", "Cancion: Shiver\n")
        if cant == 'depeche mode':
            print("Enjoy The Silence")
        if cant == 'the cure':
            print("Cancion: LoveSong\n","Cancion: Friday im in love\n", "Cancion: Open\n", "Cancion: Cut\n", "Cancion: End\n")
        contador = contador +1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))
    #else:
     #   print("ARTISTA NO ENCONTRADO")


    if data == 2:
        print("\n***Eligio buscar por cancion***\n")
        music = input("\nIngrese el nombre de la cancion para ver su informacion:\n")
        if music == 'in the army now':
            print("Artista: Status Quo\n", "Album: In the Army Now\n", "Fecha de lanzamineto: 1986")
        if music == 'red sky':
            print("Artista: Status Quo\n", "Album: In the Army Now\n", "Fecha de lanzamineto: 1986")
        if music == 'calling':
            print("Artista: Status Quo\n", "Album: In the Army Now\n", "Fecha de lanzamineto: 1986")
        if music == 'army':
            print("Cacion relacionada")
            print("Artista: Status Quo\n", "Album: In the Army Now\n", "Fecha de lanzamineto: 1986")
        if music == 'lovesong':
            print("Artist: The Cure\n", "Album: Japanese Whispers\n", "Year: 1989")
        if music == 'friday im in love' and 'friday':
            print("Artist: The Cure\n", "Album: Wish\n", "Year: 1992")
        if music == 'end':
            print("Artist: The Cure\n", "Album: Wish\n", "Year: 1992")
        if music == 'open':
            print("Artist: The Cure\n", "Album: Wish\n", "Year: 1992")
        if music == 'cut':
            print("Artist: The Cure\n", "Album: Wish\n", "Year: 1992")
        if music == 'love me do' or 'love':
            print("Artist: The Beatles\n", "Album: Please Please Me\n" "Year: 1963")
        if music == 'love me' or 'love':
            print("Artist: The Beatles\n", "Album: Please Please Me\n" "Year: 1963")
        if music == 'let it be':
            print("Artist: The Beatles\n" "Format: MP3\n" "Album: Parachutes\n", "Year: 1970")
        if music == 'yellow':
            print("Artist: Coldplay\n" "Title: Yellow\n" "Album: Parachutes\n" "Year: 2000")
        if music == 'parachutes':
            print("Artist: Coldplay\n" "Title: Parachutes\n" "Album: Parachutes\n" "Year: 2000")
        if music == 'dont panic':
            print("Artist: Coldplay\n" "Title: Dont Panic\n" "Album: Parachutes\n" "Year: 2000")
        if music == 'shilver':
            print("Artist: Coldplay\n" "Title: Shilver\n" "Album: Parachutes\n" "Year: 2000")
        if music == 'truples':
            print("Artist: Coldplay\n" "Title: Truples\n" "Album: Parachutes\n" "Year: 2000")
        if music == 'way down we go':
            print("Artist: KALEO\n", "Album: A/B\n", "Year: 2017")
        if music == 'lost on you':
            print("Artist: LP\n", "Album: Lost On You\n", "Year: 2016")
        contador = contador + 1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))

    if data == 3:
        print("***Eligio buscar por album***")
        albu = input("\nIngrese el nombre del album\n")
        if albu == 'ab':
            print("Artist: KALEO\n", "Year: 2017")
        if albu == 'lost on you':
            print("Artist: LP\n", "Year: 2016")
        if albu == 'in the army now':
            print("Artist; Status Quo\n", "Year: 1986")
        if albu == 'parachutes':
            print("Artist: Coldplay\n", "Year: 2000")
        if albu == 'the singles':
            print("Artist: The Peche Mode\n", "Year: 1990")
        if albu == 'japanese whisper':
            print("Artist: The Cure\n", "Year: 1989")
        if albu == 'wish':
            print("Artist: The Cure\n", "Year: 1992")
        if albu == 'please please me':
            print("Artist: The Beatles\n", "Year: 1970")
        contador = contador + 1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))

    if data == 4:
        print("***ELIGIO BUSCAR POR AÑO")
        year = int(input("Ingrese un año para buscar informacion\n"))
        if year == 2017:
            print("Artist: KALEO\n", "Title: Way Down We Go\n", "Album: A/B")
        if year == 2016:
            print("Artist: LP\n", "Title: Lost On You\n", "Album: Lost On You")
        if year == 1986:
            print("Artist: Status Quo\n", "Title: In The Army Now\n", "Album: In The Army Now")
            print("Artist: Status Quo\n", "Title: Calling\n", "Album: In The Army Now")
            print("Artist: Status Quo\n", "Title: Red Sky\n", "Album: In The Army Now")

        if year == 2000:
            print("Artist: Coldplay\n", "Title: Yellow\n", "Format: MP3\n","Album: Parachutes")
            print("Artist: Coldplay\n", "Title: Dont Panic\n", "Format: MP3\n", "Album: Parachutes")
            print("Artist: Coldplay\n", "Title: Shiver\n", "Format: MP3\n", "Album: Parachutes")
            print("Artist: Coldplay\n", "Title: Parachutes\n", "Format: MP3\n", "Album: Parachutes")
            print("Artist: Coldplay\n", "Title: Trouples\n", "Format: MP3\n", "Album: Parachutes")

        if year == 1990:
            print("Artist: Depeche Mode\n", "Title: Emjoy the Silence\n", "Album:  The Singles")
        if year == 1989:
            print("Artist: The Cure\n" "Title: LoveSong\n","Album: Japanese Whispers")
        if year == 1992:
            print("Artist: The Cure\n", "Title: Friday Im In Love\n","Album: Wish")
            print("Artist: The Cure\n", "Open\n", "Album: Wish")
            print("Artist: The Cure\n", "Title: Cut\n", "Album: Wish")
            print("Artist: The Cure\n", "Title: End\n", "Album: Wish")
        if year == 1963:
            print("Artist: The Beatles\n", "Title: Love Me  Do\n", "Album: Please Please Me")
            print("Artist: The Beatles\n", "Title: Love you\n", "Album: Please Please Me")

        if year == 1970:
            print("Artist: The Beatles\n", "Title: Let It Be\n", "Album: Let It be")

        contador = contador +1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))