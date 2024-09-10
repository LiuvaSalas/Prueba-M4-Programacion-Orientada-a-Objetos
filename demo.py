from anuncio import Anuncio, Video, Display, Social, SubTipoInvalidoException
from campana import Campana, LargoExcedidoException

listado_anuncios = [{"FORMATO": "Video", "duracion": 30, "url_archivo": "www.video.com", "url_clic": "www.click.com", "sub_tipo": "instream"}]
campanha = Campana("Campaña1", listado_anuncios, "x", "y")

#probamos que se crea la campaña
print(campanha)