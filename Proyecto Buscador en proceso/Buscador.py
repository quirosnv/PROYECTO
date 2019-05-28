data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))
cantante = ['KALEO', 'kaleo', 'Coldplay', 'COLDPLAY', 'The Beatles', 'beatles']
contador = 0
while data != -1:
    if data == 1:
        print("Eligio buscar por cantante:")
        cant=  input("Ingrese el nombre de un cantante o banda, para ser buscado: ")
        if cant == 'kaleo':
           print("Cancion: Way Down we go")
        if cant == 'beatles':
           print("Cancion: Let It Be\n","Cancion: Love Me Do")
        if cant == 'lp':
           print("Cancion: Lost On You")
        if cant == 'status quo':
           print("Cancion: In the Army Now")
        if cant == 'coldplay':
           print("Cancion: Yellow")
        if cant == 'depeche mode':
          print("Enjoy The Silence")
        if cant == 'the cure':
          print("Cancion: LoveSong\n","Cancion: Friday im in love")
        contador = contador +1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))
    #else:
     #   print("ARTISTA NO ENCONTRADO")


    if data == 2:
        print("\n***Eligio buscar por cancion***\n")
        music = input("\nIngrese el nombre de la cancion para ver su informacion:\n")
        if music == 'in the army now':
          print("Artista: Status Quo\n", "Album: In the Army Now\n", "Fecha de lanzamineto: 1986")
        if music == 'army':
          print("Cacion relacionada")
          print("Artista: Status Quo\n", "Album: In the Army Now\n", "Fecha de lanzamineto: 1986")
        if music == 'lovesong':
          print("Artist: The Cure\n", "Album: Japanese Whispers\n", "Year: 1989")
        if music== 'friday im in love' and 'friday':
          print("Artist: The Cure\n", "Album: Wish\n", "Year: 1992")
        if music == 'love me do' and 'love':
          print("Artist: The Beatles\n", "Album: Please Please Me\n" "Year: 1963")
        if music == 'let it be':
          print("Artist: The Beatles\n" "Format: MP3\n" "Album: Parachutes\n", "Year: 1970")
        if music == 'yellow':
          print("Artist: Coldplay\n" "Title: Yellow\n" "Album: Parachutes\n" "Year: 2000")
        if music == 'way down we go':
          print("Artist: KALEO\n", "Album: A/B\n", "Year: 2017")
        if music == 'lost on you':
          print("Artist: LP\n", "Album: Lost On You\n", "Year: 2016")
        contador = contador + 1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))
    #else:
     #   print("\nCANCION NO ENCONTRADA\n")

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
    #else:
     #   print("ALBUM NO ENCONTRADO")

    if data == 4:
        print("***ELIGIO BUSCAR POR AÑO")
        year = int(input("Ingrese un año para buscar informacion\n"))
        if year == 2017:
          print("Artist: KALEO\n", "Title: Way Down We Go\n", "Album: A/B")
        if year == 2016:
          print("Artist: LP\n", "Title: Lost On You\n", "Album: Lost On You")
        if year == 1986:
          print("Artist: Status Quo\n", "Title: In The Army Now\n", "Album: In The Army Now")
        if year == 2000:
          print("Artist: Coldplay\n", "Title: Yellow\n", "Format: MP3\n","Album: Parachutes")
        if year == 1990:
          print("Artist: Depeche Mode\n", "Title: Emjoy the Silence\n", "Album:  The Singles")
        if year == 1989:
          print("Artist: The Cure\n" "Title: LoveSong\n","Album: Japanese Whispers")
        if year == 1992:
          print("Artist: The Cure\n", "Title: Friday Im In Love\n","Album: Wish")
        if year == 1963:
          print("Artist: The Beatles\n", "Title: Love Me  Do\n", "Album: Please Please Me")
        if year == 1970:
          print("Artist: The Beatles\n", "Title: Let It Be\n", "Album: Parachutes")
    #else:
     #   print("NO SE ENCONTRO INFORMACION POR AÑO")
        contador = contador +1
        data = int(input("ingrese 1 si quiere buscar por cantante, 2 por cancion, 3 por album, 4 por año, -1 SALIR:  "))
