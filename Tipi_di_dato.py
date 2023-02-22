# String : x = "ciao"
# Integer : x = 20
# Float : x = 20.5
# List : x = ["roma", "milano", "napoli"]
# Tuple : x = ("roma", "milano", "napoli")
# Range : x = range(6)
# Dict : x = {"nome": "Luca", "eta": 25}
# Set : x = {"roma", "milano", "napoli"}

#########
# CASTING
#########
#
# Castare significa prendere un numero e convertirlo in una stringa per esempio
#
# In Python non è possibile concatenare una stringa ad'un numero, per farlo dovremmo ricorrere al casting

stringaCasting = "Concatenami"
numeroCasting = 25

print("CASTING") # Questo print serve solo per ordinare la console in basso

print(stringaCasting + str(numeroCasting)) # concatenazione di una stringa e un numero tramite casting

print() # semplice separatore

##########
# STRINGHE
#########

# Le stringhe possono essere scritte con i "" oppure con i ''
#
# Le stringhe multi righe vengono inserite con """""" oppure con ''''''
#
# Per accedere all'indice di una stringa si utilizza []


print("STRINGHE")

stringaIndice = "Indice"

print(f"Stampo il carattere i della {stringaIndice} >>>>>", stringaIndice[3]) # verra stampata la i

# Per ricevere la lunghezza di una stringa(cioè la quantità di caratteri, compreso lo spazio) si utilizza len(stringa)

print(f"La lunghezza della {stringaIndice} è >>>>>", len(stringaIndice))

# Per selezionare una porzione di una stringa si utilizza lo slice [indiceStart:IndiceEnd]
    # L'indice start specifica la porzione di partenza da selezionare, se non specificato di default è 0
    # L'indice end specifica la porzione finale (non inclusa) finale selezionata, se non specificato di dafault è
        # l'ultima posizione

print(f"Selezione la porzione 'ind' nella {stringaIndice} >>>>>", stringaIndice[:3])
    # partenza omessa quindi 0
    # fine uguale a 3 quindi da indice 0 a indice 2 (il 3 non è compreso)

print(f"Seleziono la porzione 'ice' nella {stringaIndice} >>>>>", stringaIndice[3:])
    # partenza 3
    # fine omessa quindi fino all'ultima posizione

# Con i valori negativi è possibile selezionare partendo dalla fine

print(f"Seleziono la porzione 'ce' nella {stringaIndice} usando valori negativi >>>>>", stringaIndice[-2:])
    # partenza -2 quindi dalla penultima posizione fino alla fine

# Il terzo argomento per estrarre una parte di stringa viene chiamato step, il cui indica la quantità di carattere da
# prendere ogni a ogni passo

print(f"Faccio il reverse della stringa {stringaIndice} >>>>>", stringaIndice[::-1])
print(f"Seleziono ogni 2 caratteri della stringa {stringaIndice} >>>>>", stringaIndice[: len(stringaIndice) - 1: 2])

# METODI
# IL metodo ord() accetta un carattere unicode e ritorna un numero corrispondente
print(f"Visualizzo il numero unicode corrispondente del primo carattere della stringa >>>>>, {stringaIndice[0]} = ", ord(stringaIndice[0]))

# Il metodo chr() accetta un numero unicode e ritorna un carattere unicode corrispondente
print("Visualizzo il carattere unicode corrispondente al numero >>>>> 73 = ", chr(73))

# Il metodo upper() trasforma una stringa tutta in maiuscolo, mentre il metodo lower() la trasforma in minuscolo

print(f"Trasformo la {stringaIndice} tutta in maiuscola >>>>>", stringaIndice.upper())
print(f"Trasformo la {stringaIndice} tutta in minuscola >>>>>", stringaIndice.lower())


# Con il metodo strip() è possibile eliminare gli spazzi contenuti in una stringa all'inizio e alla fine
stringaSeparata = " Programmatore "

print(f"Elimino gli spazzi dalla stringa {stringaSeparata} >>>>", stringaSeparata.strip())

# Con il metodo replace() è possibile sostituire un carattere con un'altro
    # il metodo replace() accetta due parametri il primo è il carattere da trovare, il secondo è il carattere
        # che rimpiazzerà il carattere trovato

print(f"Rendo plurale la stringa {stringaSeparata} >>>>>>", stringaSeparata.replace("e", "i"))

articolo = "Il"
frase = "{} è un bellissimo lavoro"

print(f"Costruisco una stringa con lo string format >>>>>>", articolo + frase.format(stringaSeparata[:len(stringaSeparata) - 1]))



#########
#BOOLEANI
#########

# I booleani sono di due tipi, True e False

# tipi di bolleani False:
    # bool(false)
    # bool(None)
    # bool(0)
    # bool("")
    # bool(())
    # bool([])
    # bool({})

# Tutto il resto viene considerato True


# NUMERI
#######

# Esistono 3 tipi di numeri in python, int, float e complex

x = 1 # int
u = 2.8 # float
z = 1j # complex

# OPERAZIONI ARITMETICHE
    # + somma
    # - sottrazione
    # / divisione
    # % resto
    # ** potenza
    # // floor division


# Con type() è possibile controllare il tipo di dato
print()
print("NUMERI")
print("Controlliamo il tipo di dato di z >>>>", type(z))

# METODI
 # min() ritorna il valore minimo dei numeri passati
 # max() ritorna il valore massimo dei numeri passati
 # abs() ritorna il valore assoluto di un numero
 # pow() potenza


#######
# LISTE
#######

print()
print("LISTE")
# La lista è una collezione di dati ordinata e modificabile, ordinata perchè è possibile accedere agli elementi
    # tramite indice, modificabile perchè è possibile aggiungere, modificare e rimuovere gli elementi

listaccia = ["qualcosa", "niente", "tutto quello che vuoi"]
listina = ["qualcosina", 0.1]

# Si accede agli elementi nello stesso modo delle stringhe e si selezionano gli elementi nello stesso modo

print("Stampo il secondo elemento della listaccia >>>>>", listaccia[1])
print("Stampo i primi due elementi della listaccia >>>>>", listaccia[:2])

# CONCATENARE DUE LISTE
#     Con il metodo extend() si aggiunge alla coda un'altra lista
#     Con l'operatore + si possono concatenare due liste
listaccia.extend(listina)
print("Concateno le due liste con extend >>>>", listaccia)
print("Concateno le due liste con l'operatore + >>>>>", listaccia + listina)

# AGGIUNGERE elementi alla lista, si utilizza il metodo append()
listina.append("granellino di sabbia")
print("Aggiungo un elemento a listina >>>>>", listina)

# RIMUOVERE elementi da una lista
    # Con il metodo remove() è possibile eliminare l'elemento specificato
listina.remove(0.1)
print("Rimuovo 0.1 dalla listina >>>>>", listina)

    # Con il metodo pop() è possibile rimuovere l'elemento che si trova nell'indice specificato, se non specificato
    # verrà eliminato l'ultimo elemento
listina.pop(0)
print("Elimino il primo elemento dalla listina >>>>>>", listina)

    #con il metodo clear() la lista viene svuotata
listina.clear()
print("Svuoto la listina >>>>>", listina)


# CICLARE UNA LISTA

    # Per ciclare una lista si utilizza il for in
print("Stampo tutti gli elementi della listaccia con il ciclo for in: ")
for elemento in listaccia:
    print("  >>", elemento)

print("Stampo tutti gli elementi della listaccia con il ciclo for in attraverso l'indice:")
for i in range(len(listaccia)):
    print(f" Indice {i} >>", listaccia[i])

# ORDINARE UNA LISTA

    # Per ordinare una lista si utilizza il metodo sort(), le stringe verranno ordinate alfabeticamente e i numeri in
    # ordine crescente

listaNumerica = [5, 1, 4, 7]
listaAlfabetica = ["F", "Z", "A", "K"]

listaAlfabetica.sort()
listaNumerica.sort()

print("Ecco le due liste ordinate >>>>", listaAlfabetica, listaNumerica)

# COPIARE UNA LISTA
    # Il metodo copy() serve per creare una copia di una lista

listacciaCopia = listaccia.copy()
print("Questa è una copia di listaccia >>>>", listacciaCopia)

#######
# TUPLE
######

    # Una tupla è una collezione ordinata non modificabile

    # packing di una tupla:

tuploide = ("Wasabi", "Bruciore")

    # unpacking di una tupla:

(mangiare, sentire) = tuploide

print()
print("TUPLE")
print("Effettuato unpacking di tuploide", mangiare, sentire)


