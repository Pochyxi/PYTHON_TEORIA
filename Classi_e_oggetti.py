# La programmazione a oggetti è quel tipo di programmazione che va a prendere entità del mondo reale che sono
# rappresentazioni derivate sotto forma di oggetto

class Persona:
    # Questo è il costruttore
    def __init__(self, nome, cognome):
        # Nel momento in cui creiamo una nuova istanza di Persona, specifichiamo che il primo parametro sarà
        # il nome, e il secondo sarà il cognome, self si riferisce alla classe stessa(questa Persona)
        self.nome = nome
        self.cognome = cognome

    # Metodo di una classe
    def presentati(self):
        print(f"Piacere {self.nome} {self.cognome} !")


# quest'oggetto è un'istanza della classe Persona
persona1 = Persona("Luca", "Rossi")
persona2 = Persona("Franco", "Airami")

# in questo modo si accede alle proprietà di un'istanza
print("Accedo alla proprietà nome in persona1 >>>>>", persona1.nome)
print("Accedo alla proprietà cognome in persona2 >>>>>", persona2.cognome)

# Richiamare i metodi di una classe
persona1.presentati()
persona2.presentati()

# Modificare le proprietà di un oggetto
nome_precedente = persona1.nome
persona1.nome = "Maria"
print(f"Il nome di persona1 è stato modificato da {nome_precedente} a >>>>>", persona1.nome)


# EREDITARIETA'
# Specifichiamo che Insegnante è una sottoclasse di Persona
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    # Eseguo l'overraide del metodo presentato() che si trova nella classe genitore Persona
    def presentati(self):
        print("Buongiorno sono " + self.nome + " " + self.cognome + ".")

    def insegnamento(self):
        print(f"Sono un docente di {self.materia}")


insegnante1 = Insegnante("Anna", "Maggi", "Storia")
insegnante1.presentati()
insegnante1.insegnamento()
