#classe per la gestione della coda in cassa
#c'è un numero massimo di pers che possono stare in cassa
#questo viene gestito quando viene aggiunto o rimossa una persona

class Cassa_generica:
    def __init__(self, array = []):
        self.max = 5
        self.coda_cassa = array
    
    def enqueue_cassa(self, cliente):
        if len(self.coda_cassa) <= self.max:# in coda possono esserci al massimo un numero di 5 persone 
            self.coda_cassa.append(cliente)
            return True
        return False

    def dequeue_cassa(self):# se la coda ha persone tolgo altimenti ritorna falso
        if len(self.coda_cassa) > 0:
            self.coda_cassa.pop(0)# FIFO :pop rimuove l ultimo elem della coda ma se passo l indice 0 lo toglie dall'inizio della coda
            return True
        return False
    

