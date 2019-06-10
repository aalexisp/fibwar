import tweepy
from time import sleep
import random

auth = tweepy.OAuthHandler("lp2hHlqLChGum3CeROCNyIiig", "FLptgr8qqkEuRiZmP6bSSUJzg71FcU2TbhGdWCpJny1Kn098NF")
auth.set_access_token("1135110202762694656-UwQq9kpDQL7X2w9GNNczNTSPVXYZvp", "DmSXus0XVTnYoR6F9Fm6OD2SEF8j6suEHePtpqlfKv3ea")

api = tweepy.API(auth)


def guerra(api):

    tiempo = 90
    jugadores = {"David":random.randint(0,3),
    "Dani":random.randint(0,3),
    "Sergi":random.randint(0,3),
    "Alexis":random.randint(0,3),
    "Ferri":random.randint(0,3)}

    listaJugadores = ["David", "Dani", "Alexis", "Sergi", "Ferri"]
    listaMuertos = []
    
    while len(jugadores) > 1:
        if len(jugadores) < 5:
            resucitar = random.randint(0,1000)
            suicidar = random.randint(0, 1000)
            if resucitar < 400:
                i = random.randint(0,len(listaMuertos)-1)
                resucitado = listaMuertos[i]
                jugadores.update({resucitado:random.randint(0,4)})
                listaJugadores.append(resucitado)
                listaMuertos.pop(i)
                print(resucitado + " ha resucitado gracias a la fuerza de los bocatas del bar de la FIB!")
                foto = resucitado + ".jpeg"
                status = resucitado + " ha resucitado gracias a la fuerza de los bocatas del bar de la FIB!"
                api.update_with_media(foto, status)
                sleep(tiempo)
                
            if suicidar < 400:
                i = random.randint(0,len(listaJugadores)-1)
                suicidio = listaJugadores[i]
                jugadores.pop(suicidio)
                listaMuertos.append(suicidio)
                listaJugadores.pop(i)
                print(suicidio + " se ha acordado de EC y se ha suicidado!")
                foto = suicidio + ".jpeg"
                status = suicidio + " se ha acordado de EC y se ha suicidado!"
                api.update_with_media(foto, status)
                if len(listaJugadores) == 1:
                    ganador = listaJugadores[0]
                    break

        i = random.randint(0,len(listaJugadores)-1)
        j = random.randint(0,len(listaJugadores)-1)
        while i == j:
            j = random.randint(0,len(listaJugadores)-1)

        ataca1 = listaJugadores[i]
        ataca2 = listaJugadores[j]

        ataque1 = random.randint(0, 100)
        ataque2 = random.randint(0, 100)
        if jugadores[ataca1]*ataque1 > jugadores[ataca2]*ataque2:
            jugadores[ataca1] += random.randint(0,2)
            foto = ataca1 + ".jpeg"
            status = ataca1 + " ha eliminado a " + ataca2
            api.update_with_media(foto, status)
            print(ataca1 + " ha eliminado a " + ataca2)
            listaJugadores.pop(j)
            listaMuertos.append(ataca2)
            jugadores.pop(ataca2)
            ganador = ataca1

        elif jugadores[ataca1]*ataque1 < jugadores[ataca2]*ataque2:
            jugadores[ataca2] += random.randint(0,2)
            foto = ataca2 + ".jpeg"
            status = ataca2 + " ha eliminado a " + ataca1
            api.update_with_media(foto, status)
            print(ataca2 + " ha eliminado a " + ataca1)
            listaJugadores.pop(i)
            listaMuertos.append(ataca1)
            jugadores.pop(ataca1)
            ganador = ataca2

        else:
            aux = [ataca1, ataca2]
            aux2 = random.randint(0,1)

            if aux2 == 0:
                foto = ataca2 + ".jpeg"
                status = ataca2 + " ha eliminado a " + ataca1
                api.update_with_media(foto, status)
                print(ataca2 + " ha eliminado a " + ataca1)
                jugadores[ataca2] += random.randint(0,2)
                ganador = ataca2
                listaJugadores.pop(aux2)
                listaMuertos.append(ataca1)
                jugadores.pop(ataca1)
            else:
                foto = ataca1 + ".jpeg"
                status = ataca1 + " ha eliminado a " + ataca2
                api.update_with_media(foto, status)
                print(ataca1 + " ha eliminado a " + ataca2)
                jugadores[ataca1] += random.randint(0,2)
                ganador = ataca1
                listaJugadores.pop(aux2)
                listaMuertos.append(ataca2)
                jugadores.pop(ataca2)

        if len(jugadores) > 1:
            sleep(tiempo)
    return ganador

tiempoEmpezar = 180
api.update_status("La guerra empieza en 3 minutos!!")
print("La guerra empieza en 3 minutos!!")
sleep(tiempoEmpezar)
ganador = guerra(api) 

foto = ganador + ".jpeg"
status = ganador + " ha ganado la guerra!!"
api.update_with_media(foto, status)
print(ganador + " ha ganado la guerra!")
