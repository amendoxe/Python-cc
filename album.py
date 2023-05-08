
"""8-7 function album(name, title, #s), builds a dictionary of music album
# return album dictionary """
albums = []


def make_album(band_name, disc_title, tracks=None):
    """ create a dictionary with the user input """

    album = {"name": band_name, "album": disc_title}
    if tracks:
        album["number of tracks"] = tracks
    albums.append(album)
    print(f"This is the last album you recorded \n {album}\n")


while True:
    name = input("Escribe el nombre de la banda: ")
    title = input("Escribe el nombre del disco: ")
    track = input("Numero de canciones, pulsa enter para omitir: ")
    make_album(name, title, track)
    print("This are all the albums you have recorded so far:\n")
    for al in albums:
        print(al)
    continuing = input("Continue?: y/n ")
    if continuing == "n":
        break
