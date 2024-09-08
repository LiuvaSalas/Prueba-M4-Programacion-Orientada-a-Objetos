from anuncio import Anuncio, Video, Display, Social

class LargoExcedidoException(Exception):
    pass


class Campana:
    def __init__(self, nombre: str, listado_anuncios, fecha_inicio = None, fecha_termino = None):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(listado_anuncios)

    @property
    def nombre(self):
        return sef.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoException(f"El nuevo nombre de campaña proporcionado '{nuevo_nombre}' supera los 250 caracteres")
        else:
            self.__nombre = nuevo_nombre

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self.__fecha_inicio = nueva_fecha_inicio
        return self.__fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        self.__fecha_termino = nueva_fecha_termino
        return self.__fecha_termino

    @property
    def anuncios(self):
        return _anuncios

    def _crear_anuncios(self, listado_anuncios):
        anuncios = []
        for data in listado_anuncios:
            FORMATO = data.get("FORMATO")
            if FORMATO == "Video":
                anuncio = Video(**data)
            elif FORMATO == "Display":
                anuncio = Display(**data)
            elif FORMATO == "Social":
                anuncio = Social(**data)
            anuncios.append(anuncio)
        return anuncios

    def __str__(self):
        video_count = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Video))
        display_count = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Display))
        social_count = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Social))
        return f"Nombre de la Campaña: {self.__nombre} \nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"