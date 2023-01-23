# DATA E ORA
import datetime
print("DATETIME")

# Stampare la data attuale
# datetime.now()
data_attuale = datetime.datetime.now()
print("Data attuale >>>>>>", data_attuale)

# Stampare data personalizzata
# datetime()
data_custom = datetime.datetime(1994, 8, 27, 6, 0, 0)
print("Data personalizzata >>>>>", data_custom)

# Formattare una data con strftim()
# %a	Giorni della settimana abbreviati                                           Sun, Mon, ...
# %A	Giorno della settimana intero.	                                            Sunday, Monday, ...
# %w	Giorno della settimana come numero.	                                        0, 1, ..., 6
# %d	Giorno del mese a zero-padded decimal.	                                    01, 02, ..., 31
# %-d	Giorno del mese a numero decimale.	                                        1, 2, ..., 30
# %b	Nome del mese abbreviato.	                                                Jan, Feb, ..., Dec
# %B	Nome del mese completo.	                                                    January, February, ...
# %m	Mesi a zero-padded decimal number.	                                        01, 02, ..., 12
# %-m	Mesi a numeri decimali.	                                                    1, 2, ..., 12
# %y	Anno senza secolo a zero-padded decimal number.	                            00, 01, ..., 99
# %-y	Anno senza secolo come numero decimale.	                                    0, 1, ..., 99
# %Y	Anno con secolo a numeri decimali.	                                        2013, 2019 etc.
# %H	Ora (24-ore) a zero-padded numeri decimali.	                                00, 01, ..., 23
# %-H	Ora (24-ore) a numeri decimali.	                                            0, 1, ..., 23
# %I	Ora (12-ore) a zero-padded numeri decimali.                                	01, 02, ..., 12
# %-I	Ora (12-ore) a numeri decimali.	                                            1, 2, ... 12
# %p	AM, PM
# %M	Minuti a zero-padded numeri decimali.	                                    00, 01, ..., 59
# %-M	Minuti a numeri decimali.	                                                0, 1, ..., 59
# %S	Secondi a zero-padded numeri decimali.	                                    00, 01, ..., 59
# %-S	Secondi a numeri decimali.	                                                0, 1, ..., 59
# %f	Microsecondi a numeri decimali, zero-padded sulla sinistra.	                000000 - 999999
# %z	UTC offset in the form +HHMM or -HHMM.
# %Z	Time zone name.
# %j	Giorno dell'anno a zero-padded come numeri decimali.	                    001, 002, ..., 366
# %-j	Giorno dell'anno come numero decimale.	                                    1, 2, ..., 366
# %U	Settimana numerica dell'anno (Lunedi come primo giorno della settimana).	00, 01, ..., 53
# %W	Settimana numerica dell'anno (Martedi come primo giorno della settimana).	00, 01, ..., 53
# %c	Data e ora locale.	Mon Sep 30 07:06:05 2013
# %x	Data locale.	09/30/13
# %X	Ora locale.	07:06:05
# %%	A literal '%' character.	%
data_mod = data_custom.strftime("%d/%m/%Y, %H:%M:%S")
print("Data formattata secondo i canoni italiani >>>>>>", data_mod)
