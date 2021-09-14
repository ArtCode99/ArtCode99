    #Cum se deschide un fisier, plus try in caz ca nu exista. Optional dupa nume poti sa pui w/r + sau a. E bine a daca vrei sa nu ti se stearga.

# try:
#     with open('Text.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Fisieru nu exista")

    #Pt copiat fisiere:

# import shutil   #->e o modalitate pt copiat fisiere. Are 3 functii principale
# shutil.copyfile('Text.txt','copyText.txt')       #are 2 argumente, sursa (numele daca e aici, path-ul daca altundeva) si destinatia. Asta copiaza doar content-urile
#shutil.copy('sursa','destinatie')          #copiaza si permisiunile
#shutil.copy2('sursa','destinatie')          #copiaza si metadata


    #Pt mutat  fisiere: se face cu pachetul os, care are functiile path.exists() si replace(sursa,dest)  , remove(cale)

# import os
# source="Text.txt"     #->merge pt ca fisieru e aici, altfel trebuia toata calea
# destination="/home/ubuntu/PycharmProjects/pythonProject/Text.txt"       #trb ori sa inversam slash-urile si sa le dublam, ori un replace
# try:
#         os.replace(source,destination)
# except FileNotFoundError:
#     print("File wasn't find")
# else:
#     print(source + " was moved")


    #Pt sters fisiere:  tot cu os
# import os
# import shutil
# path="copyText.txt"
# try:
#     os.remove(path)            #nu sterge si FOLDERE, doar fisiere, daca vrei sa stergi foldere ai shutil.rmtree(cale)
# except:
#     print("Eroare")
# else:
#     print("A fost sters")


