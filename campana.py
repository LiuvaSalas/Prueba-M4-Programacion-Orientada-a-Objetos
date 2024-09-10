from anuncio import Anuncio, Video, Display, Social
from errores import LargoExcedidoException

class Campana:
    """
    Clase para generar campañas con listado de anuncios ya especificados

    Parametros:
    - nombre: str, nombre de la campaña
    - listado_anuncios: list-dict, listado con diccionario de anuncios para crear anuncios para cada campaña.
    - fecha_inicio: date, fecha de inicio de la campaña.
    - fecha_termino: date, fecha de termino de la campaña.
    
    Return:
    - crear_anuncios(), crea anuncios iterando la lista-diccionario que se le paso como atributo
    - anuncios listado de anuncios para una campaña en especifico
    - __str__: cadena de texto con el detalle de la campaña y el contenido de anuncios, como cuantos anuncios de cada tipo hay.
    """
    def __init__(self, nombre: str, listado_anuncios, fecha_inicio = None, fecha_termino = None):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(listado_anuncios)

    @property
    def nombre(self):
        return self.__nombre

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
        return self._anuncios


    def _crear_anuncios(self, listado_anuncios: list):
        """
        Parametros:
        - listado_anuncios: list-dict, listado con diccionario de anuncios para crear anuncios para cada campaña.
        
        Return:
        - anuncios listado de anuncios para una campaña en especifico
        """
        anuncios = []
        for x in listado_anuncios:
            FORMATO = x.get("FORMATO")
            if FORMATO == "Video":
                anuncio = Video(x.get("duracion"), x.get("url_archivo"), x.get("url_clic"), x.get("sub_tipo"))
            elif FORMATO == "Display":
                anuncio = Display(x.get("ancho"), x.get("alto"), x.get("url_archivo"), x.get("url_clic"), x.get("sub_tipo"))
            elif FORMATO == "Social":
                anuncio = Social(x.get("ancho"), x.get("alto"), x.get("url_archivo"), x.get("url_clic"), x.get("sub_tipo"))
            else:
                raise ValueError(f"Formato de anuncio desconocido: {FORMATO}")
            anuncios.append(anuncio)
        return anuncios

    def __str__(self):
        video_count = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Video))
        display_count = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Display))
        social_count = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Social))
        return f"Nombre de la Campaña: {self.__nombre} \nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"