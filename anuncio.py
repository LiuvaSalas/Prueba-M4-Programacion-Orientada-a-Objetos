from abc import ABC, abstractmethod

class SubTipoInvalidoException(Exception):
    pass

class Anuncio(ABC):
    SUB_TIPOS = {
        "Video": ("instream", "outstream"),
        "Display": ("tradicional", "native"),
        "Social": ("facebook", "linkedin")
    }

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str,  sub_tipo: str) -> None:
        self.__ancho = None
        self.__alto = None
        self.url_archivo = None
        self.url_clic = None
        self._sub_tipo = None
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        if nuevo_ancho <= 0:
            self.__ancho = 1
        else:
            self.__ancho = nuevo_ancho

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto):
        if nuevo_alto <= 0:
            self.__alto = 1
        else:
            self.__alto = nuevo_alto

    @property
    def url_archivo(self) -> str:
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self._url_archivo = url_archivo

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, url_clic):
        self._url_clic = url_clic

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if nuevo_sub_tipo in self.SUB_TIPOS:
            self._sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoException(f"El subtipo '{nuevo_sub_tipo}' no es válido para el formato '{self.FORMATO}'.")

    @staticmethod
    def mostrar_formatos():
        for formato, subtipos in Anuncio.SUB_TIPOS.items():
            print(f"{formato.upper()}:")
            print("=" * 10)
            for subtipo in subtipos:
                print(f"- {subtipo.capitalize()}")
        return "-" * 10

    @abstractmethod
    def comprimir_anuncio():
        pass
    
    @abstractmethod
    def redimensionar_anuncio():
        pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, duracion: int, url_archivo: str, url_clic: str, sub_tipo: str):

        super().__init__( ancho = 1, alto = 1, url_archivo = url_archivo, url_clic = url_clic, sub_tipo = sub_tipo)
        self.duracion = duracion

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, nueva_duracion:int):
        if nueva_duracion > 0:
            self._duracion = nueva_duracion
        else:
            self._duracion = 5

    def comprimir_anuncio():
        return "COMPRESION DE VIDEO NO IMPLEMENTADA AUN"

    def redimensionar_anuncio():
        return "REDIMENSIONAMIENTO DE VIDEO NO IMPLEMENTADO AUN"

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio():
        return "COMPRESION DE ANUNCIOS DISPLAY NO IMPLEMENTADA AUN"

    def redimensionar_anuncio():
        return "RECORTE DE ANUNCIOS DISPLAY NO IMPLEMENTADO AUN"

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio():
        return "COMPRESION DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AUN"

    def redimensionar_anuncio():
        return "REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AUN"








    



    

    
