# in python create un ciclo for con numerazione da 1 a 100
# fermate il loop a 10
for x in range(1, 100):
    if x < 10:
        print(x)

        # utilizzo del comando continue(poteva anche essere omessa)
        continue

    # utilizzate la keyword "else"
    else:
        print("Fermo il ciclo a", x, "iterazioni")

        # utilizzo della formattazione single line del for
        print("Farcio partire il single line for")
        for y in range(1, 100): print(y)
        break

# fare la stessa cosa con il ciclo while (senza single line)

i = 1

while i < 100:
    if i == 10:
        break
    else:
        print(i)
        i += 1
        continue

# scrivere la motivazione per preferire il for al while

# Una delle motivazioni per cui penso che il for sia preferibile al while potrebbe essere ad esempio che nel while
# abbiamo bisogno di definire una variabile che rappresenterà l'iteratore e all'interno del while se non lo si
# incrementa si rischia il loop infinito. Nel for sia la l'iteratore che la condizione sono definiti in partenza(
# Lista o range). Personalmente credo che il for a livello di performance sia migliore del while proprio a causa
# delle suddette motivazioni

# ESEMPIO 1 CICLO FOR CON CONTINUE

for xy in range(1, 20):
    # Stampa tutti i numeri pari da 1 a 20(20 non compreso), nel caso in cui xy sia uguale a 2 il ciclo verrà saltato
    if xy == 2:
        continue
    if xy % 2 == 0:
        print(xy)
else:
    print("finito!")
