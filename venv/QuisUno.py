dicCancion = {}
dicartista = {}
mainDic = {'artista': dicartista,'caniones':dicCancion}

def es_numero(msg):
    esNum = False
    num = 0
    while not esNum:
        try:
            num = int(input(msg))
            esNum = True
        except ValueError:
            print('Digite un valor numerico')
    return  num
def menu():
    print("""
    [1] Crear un artista
    [2] crear una cancion
    [3] Listar canciones por artista
    [4] Salir    
    """)
    opcion = es_numero("Seleccione una opcion: ")
    return opcion



class Cancion:
    tituloCancion = ''
    genero = ''
    agnoCreacion = 0
    idArtista = 0
    idCancion = 0

    def crear_cancion(self):
        self.titulo = input('Digite el titilo de la cancion: ')
        self.genero = input('Digite el genero de la cancion: ')
        self.agnoCreacion = es_numero('Digite el el año de creacion de la canion: ')
        self.idArtista = es_numero('Digite de el numero de documento del autor de la cancion: ')
        self.idCancion = es_numero('Digite un id para esta cancion')

        dicCancion [self.idCancion] = {
            'titulo': self.titulo,
            'genero': self.genero,
            'agnoCreacion': self.agnoCreacion,
            'idArtista': self.idArtista
        }
    def listar_canciones(self):
        print('en construccion')



class Artista(Cancion):
    id = 0
    nombreReal = ''
    nombreArtistico = ''
    edad = 0
    nacionalidad = ''

    def create_artista(self):
        self.id = es_numero('Digite el numero de cedula: ')
        self.nombreReal = input('Digite el nombre real del artista: ')
        self.nombreArtistico = input('Digite el nombre artistico: ')
        self.edad = es_numero('Digite la edad del artista: ')
        self.nacionalidad = input('Digite el pais de origen del artista: ')

        dicartista[self.id] ={
            'nomReal':self.nombreReal,
            'nomArtistico': self.nombreArtistico,
            'edad': self.edad,
            'nacionalidad': self.nacionalidad
        }






artista = Artista()
opcion = menu()
while 0 < opcion <= 4:

    if opcion == 1:
        artista.create_artista()

    elif opcion == 2:
        artista.crear_cancion()


    elif opcion == 3:
        print(mainDic)
        artista.listar_canciones()

    elif opcion == 4:
        exit()

    opcion = menu()





