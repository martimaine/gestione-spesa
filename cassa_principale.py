class Coda_principale:
    
    def __init__(self, array = []):
        self.queue = array
    
    def enqueue_coda_pri(self, cliente):
        self.queue.append(cliente)

    def dequeue_coda_pri(self):

        return self.queue.pop(0)