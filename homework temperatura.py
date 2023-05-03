import json
import turtle
import datetime
import requests


# Conversione dei dati sulla temperatura da kelvin a gradi centigradi
def conversione_temperatura(temp):
    gradi = int(temp - 273.15)
    return gradi


# Input dati (città, Nazione) da parte dell'utente e generazione URL
citta = input("Inserisci la città: ")
Nazione = input("Inserisci la nazione (es. IT): ")
url = "http://api.openweathermap.org/data/2.5/weather?q=" + citta + "," + Nazione + "&appid=b2ec2976ea25dfb069cbf6ba4466712b&lang=it"


# Serializzazione dei dati
ris = requests.get(url)
dati = json.loads(ris.text)

# Assegnamento dati alle variabili con relativa conversione
nome = dati["name"]
meteo = dati["weather"][0]["main"]
descrizione = dati["weather"][0]["description"]
temperatura = conversione_temperatura(int(dati["main"]["temp"]))
temperatura_max = conversione_temperatura(int(dati["main"]["temp_max"]))
temperatura_min = conversione_temperatura(int(dati["main"]["temp_min"]))
pressione = dati["main"]["pressure"]
umidita = dati["main"]["humidity"]
velocita_vento = dati["wind"]["speed"]
nuvole = dati["clouds"]["all"]


# Stampa
print("Il tempo a " + nome + " e' "+ str(meteo)+" con " + descrizione)
print("La temperatura e' di "+ str(temperatura)+ "c°")
print("Con una minima di "+ str(temperatura_min)+ "c°")
print("E una massima di "+ str(temperatura_max)+ "c°")
print("")
print("La pressione e' di "+ str(pressione)+ "hPa")
print("Con un umidita' del "+ str(umidita)+ "%")
print("La velocita' del vento e' di "+ str(velocita_vento)+ "m/s")
print("Il cielo e' copeto dal "+ str(nuvole)+ "% di nuvole")

#Grafico con turtle
turtle.setup (width=1000, height=1000)
data = datetime.datetime.now()
ora = data.hour
turtle.hideturtle()
giorno=True

#Verifica orario
if ora >= 8 and ora <18:
    giorno=True
if ora >= 18 or ora < 7:
    giorno=False
t=turtle.Turtle()
turtle.penup()
turtle.goto(0,400)
turtle.write(nome,font=("arial",30),align="center")
t.goto(0,0)

#Condizioni per definire l'immagine da mostrare
if meteo == "Clouds" and giorno:
    turtle.addshape("IMG/clouds giorno.gif")
    t.shape("IMG/clouds giorno.gif")
if meteo == "Clouds" and not giorno:
    turtle.addshape("IMG/clouds notte.gif")
    t.shape("IMG/clouds notte.gif")
if meteo == "Clear" and giorno:
    turtle.addshape("IMG/sole clear.gif")
    t.shape("IMG/sole clear.gif")
if meteo == "Clear" and not giorno:
    turtle.addshape("IMG/luna clear.gif")
    t.shape("IMG/luna clear.gif")
if meteo == "Snow":
    turtle.addshape("IMG/Snow.gif")
    t.shape("IMG/Snow.gif")
if meteo == "Rain":
    turtle.addshape("IMG/rain.gif")
    t.shape("IMG/rain.gif")
if meteo == "Drizzle" and giorno:
    turtle.addshape("IMG/drizzle giorno.gif")
    t.shape("IMG/drizzle giorno.gif")
if meteo == "Drizzle" and not giorno:
    turtle.addshape("IMG/drizzle notte.gif")
    t.shape("IMG/drizzle notte.gif")
if meteo == "Thunderstorm" and giorno:
    turtle.addshape("IMG/thunderstorm giorno.gif")
    t.shape("IMG/thunderstorm giorno.gif")
if meteo == "Thunderstorm" and not giorno:
    turtle.addshape("IMG/thunderstorm notte.gif")
    t.shape("IMG/thunderstorm notte.gif")
if meteo == "Fog":
    turtle.addshape("IMG/fog.gif")
    t.shape("IMG/fog.gif")

#Stampa dati su interfaccia grafica
te="Temperatura "+str(temperatura)+"°"
temin= "Temperatura minima "+str(temperatura_min)+"°"
temax="Temperatura massima "+str(temperatura_max)+"°"
press="Pressione "+str(pressione)+" hPa"
um="Umidità "+str(umidita)+"%"
vel= "Velocità vento "+str(velocita_vento)+"m/s"
turtle.goto(-435,-300)
turtle.write(te,font=("arial",10),align="left")
turtle.goto(-435,-350)
turtle.write(temin,font=("arial",10),align="left")
turtle.goto(-435,-400)
turtle.write(temax,font=("arial",10),align="left")
turtle.goto(235,-300)
turtle.write(press,font=("arial",10),align="left")
turtle.goto(235,-350)
turtle.write(um,font=("arial",10),align="left")
turtle.goto(235,-400)
turtle.write(vel,font=("arial",10),align="left")
turtle.done()
