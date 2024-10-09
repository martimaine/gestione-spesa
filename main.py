from cassa_generica import Cassa_generica
from cassa_principale import Coda_principale
import time
import random
import string

#classe che contine un 'altra classe la classe CODA PRINCIPALE
class Creare_modifica_coda(Coda_principale):
    
    def __init__(self, array = [], num_iniziale = 0):
        
        super().__init__(array)
        
        self.num_iniziale = num_iniziale
        self.num_ticket = num_iniziale
    
    def enqueue(self):
        
        super().enqueue_coda_pri(self.num_ticket)
        self.num_ticket += 1
        
    def dequeue_coda_pri(self):
        if(len(self.queue)>0):
            return super().dequeue_coda_pri()
        return False

class Creare_modifica_casse(Cassa_generica):

    def __init__(self, array_cassa = []):
        super().__init__(array_cassa)

    def chiamata_cassa(self,cliente):
        super().enqueue_cassa(cliente)
    
    def isEmpty(self):
        return len(self.coda_cassa)<=self.max


                        #MAIN
alphabet = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']
digits = list(string.digits)  # ['0', '1', ..., '9']

combined_sequence = [f"{letter}{number}" for letter in alphabet for number in digits]
#persone in coda con identificativo lettera e numero
array_coda_principale = [combined_sequence[i % len(combined_sequence)] for i in range(100)]

#creo la coda principale modificata che aggiunge delle utilità da usare dopo
codaPrincipale = Creare_modifica_coda(array_coda_principale,0)
print(codaPrincipale.queue)
#creo le casse senza persone in coda
casse = []
for i in range(3):
    casse.append(Creare_modifica_casse([]))

print("coda principale:", codaPrincipale.queue)
print("Persone in coda", len(codaPrincipale.queue))
#ciclo sulla lunghezza della coda principale finchè ci sono persone in coda
while len(array_coda_principale)>0:
    #ciclo su tutte le casse e per ogni cassa ciclo finchè non è piena
    for cassa in casse:
        while cassa.isEmpty():
            persona= codaPrincipale.dequeue_coda_pri()
            if(persona):
                #la persona tolta dalla cassa princip viene aggiunta alla coda della cassa
                cassa.chiamata_cassa(persona)
    print("Persone in coda", len(codaPrincipale.queue))
    #stampo la situazione della coda in cassa
    for index, cassa in enumerate(casse):
        print(f"Cassa {index}", cassa.coda_cassa)

    time.sleep(1)
    
    for cassa in casse:
        if random.random() < 0.6:  # x% chance
            cassa.dequeue_cassa()

    print("Situazione dopo turno cassa")
    for index, cassa in enumerate(casse):
        print(f"Cassa {index}", cassa.coda_cassa)
    print("Persone in coda", len(codaPrincipale.queue))


print("*** REPORT FINALE ***")
print("Cassa principale:")
print(codaPrincipale.queue)

print("Persone in cassa pronte ad essere servite")
for index, cassa in enumerate(casse):
    print(f"Cassa {index}", cassa.coda_cassa)