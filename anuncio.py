from abc import abstractmethod

class SubTipoInvalidoException(Exception):
    pass

class Anuncio():
    maximo = 1

    SUB_TIPOS = {
        #Subtipos
        "Video" : ("instream", "outstream"),
        "Display" : ("tradicional", "native"),
        "Social" : ("facebook", "linkedin")
    }

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = None
        self.__alto = None
        self.ancho = ancho
        self.alto = alto
        url_archivo = url_archivo
        url_clic = url_clic
        sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def (self, nuevo_ancho):
        if ancho <= 0:
            self.__ancho = 1
        else:
            self.__ancho = nuevo_ancho

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def (self, nuevo_alto):
        if alto <= 0:
            self.__alto = 1
        else:
            self.__alto = nuevo_alto

    @property
    def url_archivo(self) -> str:
        return self._url_archivo

    @url_archivo.setter
    def (self, url_archivo):
        self._url_archivo = url_archivo

    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def (self, url_clic):
        self._url_clic = url_clic

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def (self, sub_tipo):
        if sub_tipo in self.SUB_TIPOS.get(self.formato, []):
            self._sub_tipo = value
        else:
            raise SubTipoInvalidoException(f"El subtipo '{sub_tipo}' no es válido para el formato '{self.formato}'.")

    @staticmethod
    def mostrar_formatos():
        for formato, subtipos in Anuncio.SUB_TIPOS.items():
            print(f"FORMATO {formato.upper()}:")
            print("-" * 10)
            print("-" * 10)
            for subtipo in subtipos:
                print(f"- {subtipo}")
            print()

    @abstractmethod
    def comprimir_anuncio():
        pass
    
    @abstractmethod
    def redimensionar_anuncio():
        pass


class Video(Anuncio):
    def __init__(self, duracion: int, sub_tipo: str, url_archivo: str, url_clic: str):

        super().__init__(ancho = 1, alto = 1, sub_tipo = sub_tipo, url_archivo = url_archivo, url_clic = url_clic)
        self.duracion = duracion

        @property
        def duracion(self):
            return self._duracion

        @duracion.setter
        def (self, nueva_duracion):
            if nueva_duracion > 0:
                self._duracion = nueva_duracion
            else:
                5

        def comprimir_anuncio():
            return "COMPRESION DE VIDEO NO IMPLEMENTADA AUN"

        def redimensionar_anuncio():
            return "REDIMENSIONAMIENTO DE VIDEO NO IMPLEMENTADO AUN"

class Display(Anuncio):

    def comprimir_anuncio():
        return "COMPRESION DE ANUNCIOS DISPLAY NO IMPLEMENTADA AUN"

    def redimensionar_anuncio():
        return "RECORTE DE ANUNCIOS DISPLAY NO IMPLEMENTADO AUN"

class Social(Anuncio):
    def comprimir_anuncio():
        return "COMPRESION DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AUN"

    def redimensionar_anuncio():
        return "REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AUN"








    



    

    
