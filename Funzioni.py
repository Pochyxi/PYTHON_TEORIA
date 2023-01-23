# FUNZIONI
# Una funzione è un blocco di codice che viene eseguito quando richiamato.
def prima_funzione(tipo_pasta="spaghetti", metti_sugo=False):  # il parametro
    print(f"Pasta buonissima, tipologia {tipo_pasta}")
    if metti_sugo:
        print("Ho aggiunto il sugo!!")
        return "Sono il valore di ritorno"


prima_funzione("Fusilli", True)
# In questo caso è importante rispettare l'ordine in cui vengono definiti i parametri

prima_funzione(metti_sugo=False, tipo_pasta="Maccheroni")
# In questo caso non è importante l'ordine dato che siamo più specifici

prima_funzione()  # in questo caso verranno inseriti i valori di default

print(prima_funzione(metti_sugo=True))  # in questo caso stiamo stampando il valore che ritorna la funzione


def fai_somma(num1, num2):
    somma = num1 + num2
    return somma


una_somma = fai_somma(6, 8)
print("Ho inizializzato una variabile con il valore di ritorno di una funzione fai_somma(6, 8) >>>>>", una_somma)
