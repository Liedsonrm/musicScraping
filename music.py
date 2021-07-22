from bs4 import BeautifulSoup;
import requests

#Get the link off a music from the vagalume website


trans = True

while True:
    link = str(input("Qual link da musica, pelo site vagalume? "))
    if link == "exit":
        break
    #Check if the music are from the vagalume website
    if link.find('vagalume') != -1:
        # Check if the music have a translate

        if link.find('traducao') == -1:
            trans = False

        html = requests.get(link)
        site = BeautifulSoup(html.content, "html.parser")

        #Get the name and the author of the music
        music = site.find(class_="col1-2-1")
        compositor = site.find('h2')

        #Check if the music has a translate
        if trans:
            completeTranslate = 'Translate \n'
            completeOrigin = 'Origin \n'

            translate = site.find_all(class_='trad')
            for trad in translate:
                completeTranslate += trad.get_text()+" \n "

            print(completeTranslate)

            origin = site.find_all(class_ = "orig")
            for orig in origin:
                completeOrigin += orig.get_text()+" \n "

            print(completeOrigin)
        #If the music hasn't a translate we use the other method to get information

        else:
            letter = site.find(id="lyrics")
            print(music.find('h1').get_text())
            print(compositor.get_text())
            print(letter.get_text())
    else: 
        print("We cant get informations from this website!\n")


