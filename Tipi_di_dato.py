# String : x = "ciao"
# Integer : x = 20
# Float : x = 20.5
# List : x = ["roma", "milano", "napoli"]
# Tuple : x = ("roma", "milano", "napoli")
# Range : x = range(6)
# Dict : x = {"nome": "Luca", "eta": 25}
# Set : x = {"roma", "milano", "napoli"}

# CASTING
#
# Castare significa prendere un numero e convertirlo in una stringa per esempio
#
# In Python non è possibile concatenare una stringa ad'un numero, per farlo dovremmo ricorrere al casting

stringaCasting = "Concatenami"
numeroCasting = 25

print("CASTING")  # Questo print serve solo per ordinare la console in basso

print(stringaCasting + str(numeroCasting))  # concatenazione di una stringa e un numero tramite casting

print()  # semplice separatore

# STRINGHE

# Le stringhe possono essere scritte con i "" oppure con i ''
#
# Le stringhe multi righe vengono inserite con """""" oppure con ''''''

# Per passare una variabile all'interno di una stringa possiamo inserire la f prima degli apici f""
#
# Per accedere all'indice di una stringa si utilizza []

print("STRINGHE")

stringaIndice = "Indice"

print(f"Stampo il carattere i della {stringaIndice} >>>>>", stringaIndice[3])  # verra stampata la i

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

print(f"Costruisco una stringa con lo string format >>>>>>",
      articolo + frase.format(stringaSeparata[:len(stringaSeparata) - 1]))

# BOOLEANI

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

# Esistono 3 tipi di numeri in python, int, float e complex

x = 1  # int
u = 2.8  # float
z = 1j  # complex

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


# LISTE
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

# con il metodo clear() la lista viene svuotata
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

# TUPLE

# Una tupla è una collezione ordinata non modificabile

# packing di una tupla:

tuploide = ("Wasabi", "Bruciore")

# unpacking di una tupla:

(mangiare, sentire) = tuploide

print()
print("TUPLE")
print("Effettuato unpacking di tuploide", mangiare, sentire)

# SET

# Collezioni di dati non ordinati, non indicizzati e non modificabli. Non permettono duplicati.
print()
print("SET")

settino_cittadino = {"milano", "napoli", "roma"}
settino_altre_citta = {"firenze", "torino"}

# printare elementi in un set con il for
for citta in settino_cittadino:
    if citta == "napoli":
        print("Se trova la stringa napoli la printa >>>>", citta)

# Aggiungere elementi a un SET
# .add()
settino_cittadino.add("bari")
print("Ho aggiunto un nuovo elemento al set con il metodo add >>>>", settino_cittadino)

# .update ----> modifica il set esistente aggiungendo gli elementi di un'altro set
settino_cittadino.update(settino_altre_citta)
print("Aggiunte altre città con il metodo update >>>>", settino_cittadino)

# Rimuovere elementi da un SET
# .remove() ---> se l'elemento non esiste ci darà un errore
try:
    settino_cittadino.remove("jj")
except:
    print(">>>> Errore generato ai fini dell'esempio <<<<<")

# .discard() ----> se l'elemento non esiste semplicemente non farà nulla
settino_cittadino.discard("bari")
print("Ho eliminato bari dal set >>>>>,", settino_cittadino)

# .pop() ----> rimuove casualmente un elemento dal set
settino_cittadino.pop()
print("Ho eliminato un elemento a caso all'interno del set >>>>>", settino_cittadino)

# .clear ----> svuota completamente il set
settino_cittadino.clear()
print("Ho svuotato il set >>>>>>>", settino_cittadino)

# del settino_cittadino si elimina il set

# Come unire due SET
# .union() ----> verrà creato un nuovo set a partire dall'unione di altri set
settino_union = settino_cittadino.union(settino_altre_citta)
print("Ho unito due set in uno >>>>>>", settino_union)  # ricordiamoci che il set settino_cittadino è stato svuotato

# .intersection_update() ----> modifica il set già dichiarato con gli elementi in comune di un'altro set
settino_cittadino.add("firenze")
settino_cittadino.intersection_update(settino_altre_citta)
print("Ho unito due set in uno, prendendo solo gli elementi uguali >>>>>>", settino_cittadino)

# .intersection() -----> ritorna un nuovo set con gli elementi in comune di due set
settino_intersecato = settino_cittadino.intersection(settino_altre_citta)
print("Ho creato un nuovo set, partendo dall'unione degli elementi in comune di due set >>>>>", settino_intersecato)

# symmetric_difference ----> ritorna un nuovo set partendo da due set ed eliminando i valori in comune
settino_simmetrico = settino_cittadino.symmetric_difference(settino_altre_citta)
stringa_settino_simmetrico = "Ho creato un nuovo set, partendo dall'unione degli elementi di due set, eliminando gli " \
                             "elementi in comune"
print(stringa_settino_simmetrico, ">>>>>>", settino_simmetrico)

# symmetric_difference_update -----> modifica un set esistente con gli elementi di un altro set eliminando gli elementi
# in comune
settino_cittadino.symmetric_difference_update(settino_altre_citta)
stringa_settino_simmetrico_update = "Modifico settino_cittadino aggiungendo gli elementi di un'altro set ignorando " \
                                    "gli elementi in comune"
print(stringa_settino_simmetrico_update, ">>>>>>", settino_cittadino)

# DICTIONARY

print()
print("DICTIONARY")

# Collezioni di dati ordinati, modificabili ma non permettono duplicati (equivalente di un oggetto in JavaScript)

brutta_persona = {
    "nome": "Grinch",
    "cognome": "Madhouse",
    "eta": 75
}

# Accedere a un elemento tramite []
print("Accedo alla chiave tramite l'utilizzo delle [] >>>>>", brutta_persona["nome"])

# Accedere a un elemento tramite .get()
print("Accedo alla chiave tramite l'utilizzo del metodo get() >>>>>", brutta_persona.get("cognome"))

# Accedere alle chiavi tramite .keys()
print("Accedo alle chiavi tramite il metodo keys() >>>>>", brutta_persona.keys())

# Accedere ai valori delle chiavi tramite .values
print("Accedo ai valori tramite il metodo values() >>>>>", brutta_persona.values())

# Accedere alle chiavi e ai valori tramite il metodo .items()
print("Accedo alle chiavi e ai valori tramite il metodo items() >>>>>", brutta_persona.items())

# Controllare se una chiave esiste
print("Esiste?", "franco" in brutta_persona)


# Modificare gli elementi in un DICTIONARY(migliore)
brutta_persona["cognome"] = "Badhouse"
print(f"Ho modificato il cognome del {brutta_persona['nome']} in >>>>>", brutta_persona["cognome"])

# Modificare gli elementi in un DICT con il metodo .update()
brutta_persona.update({"eta": 340})
print(f"Ho modificato l'età del {brutta_persona['nome']} >>>>>>", brutta_persona['eta'])

# Aggiungere elementi a un DICT
brutta_persona["particolarita"] = "Sempre arrabbiato! Grrrrrrr -.-''"
print("Aggiunta nuova chiave al dict >>>>>", brutta_persona['particolarita'])

# Rimuovere elementi da un DICT
# .pop() -----> rimuove la chiave specificata
brutta_persona.pop("particolarita")
print("Ho eliminato la chiave 'particolarita' dal DICT >>>>>>", brutta_persona)

# .popitem() ------> rimuove l'ultimo item dal DICT
brutta_persona.popitem()
print("Ho rimosso l'ultimo item nel DICT >>>>>>", brutta_persona)

# .clear() -----> svuota completamente il DICT
brutta_persona.clear()
print("Ho svuotato completamente il DICT >>>>>>", brutta_persona)

# del brutta_persona -----> elimina completamente il DICT

# Ciclare gli elementi di un dict
# tramite le keys
brutta_persona["eta"] = 25
brutta_persona["nome"] = "Augustus"
brutta_persona["cognome"] = "Slurp"

print("Ciclo le chiavi del dict:")
for key in brutta_persona.keys():
    print(">>>", key)

print("Ciclo i valori del dict:")
for value in brutta_persona.values():
    print(">>>", value)

print("Ciclo le coppie chiave valore del dict:")
for k, v in brutta_persona.items():
    print(">>>", k, ": ", v)

# Copiare un dict
# .copy() per creare una copia a sè stante di un dict
brutta_copia = brutta_persona.copy()
print("Questa è una copia >>>>", brutta_copia)

