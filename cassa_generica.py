class Cassa_generica:
    def __init__(self, array = []):
        self.max = 5
        self.coda_cassa = array
    
    def enqueue_cassa(self, cliente):
        if len(self.coda_cassa) <= self.max:
            self.coda_cassa.append(cliente)
            return True
        return False

    def dequeue_cassa(self):
        if len(self.coda_cassa) > 0:
            self.coda_cassa.pop(0)
            return True
        return False
    

