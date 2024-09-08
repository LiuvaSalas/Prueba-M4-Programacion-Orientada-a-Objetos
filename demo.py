from anuncio import Anuncio, Video, Display, Social, SubTipoInvalidoException
from campana import Campana, LargoExcedidoException

#"duracion, "tipo de anuncio, dentro del formato", url, url_clic
prueba_anuncio_video = Display(30, "instream", "www.x.com", "www.a.com")

print(prueba_anuncio_video.url_clic)