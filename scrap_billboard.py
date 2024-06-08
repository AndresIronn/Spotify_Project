#Función del Lab de Webscraping
#La misma devuelve el dataframe del top 100 Billboard
#Está puesta de forma de que si el top 100 cambia, la función lo tomará en cuenta y devolverá el dataframe
#actualizado

def scrap():
    from bs4 import BeautifulSoup
    import requests ## HTTP REQUEST
    import pandas as pd 
    import time
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    artistas = []
    classes = ["title-of-a-story", "c-title", "a-no-trucate", "a-font-primary-bold-s", "u-letter-spacing-0021",
               "u-font-size-23@tablet", "lrv-u-font-size-16", "u-line-height-125", "u-line-height-normal@mobile-max",
               "a-truncate-ellipsis", "u-max-width-245", "u-max-width-230@tablet-only", "u-letter-spacing-0028@tablet"]
    for i in soup.find_all("span", class_=classes):
        artistas.append(i.get_text().replace("\t", "").replace("\n", ""))

    artistas = artistas[12:]

    canciones = []
    for i in soup.find_all("h3", class_=classes):
        cancion = i.get_text().replace("\t", "").replace("\n", "")
        if "(s)" not in cancion and cancion != "Imprint/Promotion Label:":
            canciones.append(cancion)

    canciones = canciones[:103]
    canciones = canciones[3:]

    data = pd.DataFrame({"song": canciones, "artist": artistas})    
    return data