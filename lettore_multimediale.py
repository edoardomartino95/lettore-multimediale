import time 

mylista = []

def menu():
    menu = input("""
*---------------------------------------*
[1] Inserisci una canzone nella playlist

[2] Stampa tutta la playlist

[3] Ricerca una canzone nella playlist

[4] Elimina una canzone nella playlist

[E] Esci dal lettore multimediale
*---------------------------------------*

""")

    if menu == "1":
        inserisciCanzone(mylista)

    elif menu == "2":
        stampa(mylista)

    elif menu == "3":
        ricercaCanzone(mylista)

    elif menu == "4":
        eliminaCanzone(mylista)
        
    elif menu == "E" or menu == "e":
        esci = input("Desideri uscire dal lettore multimediale? S/n ")
        uscita = False
        if esci == "S" or esci == "s":
            print("PROGRAMMA TERMINATO...")
            uscita = True
        elif esci == "N" or esci == "n":
            menu()

def inserisciCanzone(lista):
    while True:
        canzone = input("Inserisci una canzone: ")
        lista.append(canzone)
        print("Canzone inserita con successo!")
        controllo = input("Vuoi inserire un'altra canzone? S/n ")
        if controllo == 'S' or controllo == 's':
            continue
        elif controllo == 'N' or controllo == 'n':
            print("Le tue canzoni sono state inserite con successo!")
            menu()
            break 
    
def stampa(lista):
    print("La playlist contiene le seguenti canzoni: ")
    for canzone in lista:
        print(canzone)
        if lista == []:
            print("La playlist è vuota!")
    menu()

def ricercaCanzone(lista):
    canzone = input("Inserisci una canzone da ricercare: ")
    trovato = False
    i= 0
    while i < len(lista) and not trovato:
        if lista[i] == canzone:
            trovato = True
            print("La canzone è stata trovata: ", str(lista[i]))
        
            riproduzione = input("Vuoi riprodurre la canzone? S/n: ")
            if riproduzione == "S" or riproduzione == "s":
                print("Sto riproducendo la canzone: ", str(lista[i]))
            elif riproduzione == "N" or riproduzione == "n":
                print("Caricamento...")
                time.sleep(2)
                menu()
        i += 1
    
def eliminaCanzone(lista):
    elimina = input("Inserisci una canzone da eliminare: ")
    i= 0
    trovato = False
    while i < len(lista) and not trovato:
        if lista[i] == elimina:
            trovato = True
            print("La canzone è stata trovata: ", str(lista[i]))
        
        elimina = input("Vuoi eliminare la canzone? S/n: ")
        if elimina == "S" or elimina == "s":
            print("Canzone eliminata con successo!")
            lista.remove(canzone)
        elif elimina == "N" or elimina == "n":
            print("Caricamento...")
            time.sleep(2)
            menu()
        i += 1
            
if __name__ == "__main__":

    print("""
 ____      ____      __   __                                    
|_  _|    |_  _|    [  | [  |  _                                
  \ \  /\  / /,--.   | |  | | / ]  _ .--..--.   ,--.   _ .--.   
   \ \/  \/ /`'_\ :  | |  | '' <  [ `.-. .-. | `'_\ : [ `.-. |  
    \  /\  / // | |, | |  | |`\ \  | | | | | | // | |, | | | |  
     \/  \/  \'-;__/[___][__|  \_][___||__||__]\'-;__/[___||__] 
                                                                                             
    """)

    menu()


