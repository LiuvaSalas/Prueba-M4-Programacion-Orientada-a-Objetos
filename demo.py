from anuncio import Anuncio, Video, Display, Social, SubTipoInvalidoException
from campana import Campana, LargoExcedidoException

#creamos el listado con el anuncio de video
listado_anuncios = [{"FORMATO": "Video", "duracion": 30, "url_archivo": "www.video.com", "url_clic": "www.click.com", "sub_tipo": "instream"}]

#creamos la campaña para modificar posteriormente
campanha = Campana("Campaña1", listado_anuncios, "x", "y")

#probamos que se crea la campaña
print(campanha)

#solicitamos el nombre nuevo que el usuario desea asignar a la campaña anteriormente impresa y modificamos el subtipo
nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
nuevo_sub_tipo = input(f"Ingrese el nuevo subtipo para el anuncio de video {campanha.anuncios[0].SUB_TIPOS}: ")


#generamos el ciclo try y except con las excepciones generadas en cada clase.
try:
    #asignamos el nuevo nombre a la campaña
    campanha.nombre = nuevo_nombre
    
    #cambiamos el tipo de anuncio
    campanha.anuncios[0].sub_tipo = nuevo_sub_tipo

    #mostramos la campaña con los nuevos valores
    print(f"Campaña actualizada: {campanha}")

except (LargoExcedidoException, SubTipoInvalidoException) as e:
    #guardamos el mensaje de error en un archivo
    with open("error.log", "a") as log_file:
        log_file.write(f"{str(e)}\n")
    
    #mostramos el error en la terminal
    print(f"Error: {str(e)}")