import random 

class Kryptonite(object):
    
    def __init__(self, value):
        self.Q = 10000019
        self.value = value
        self.field = self.encode(value)
        self.embeddings = self.share(self.field)
    
        
    def encode(self, rational):
        upscaled = int(rational * 10**6)
        field_element = upscaled % self.Q
        return field_element

    
    def decode(self, shares):
        e = self.reconstruct(shares)
        upscaled = e if e <= self.Q/2 else e - self.Q
        rational = upscaled / 10**6
        return rational

    
    def share(self, x):
        x0 = random.randrange(self.Q)
        x1 = random.randrange(self.Q)
        x2 = (x - x0 - x1) % self.Q
        return [x0, x1, x2]

    def reconstruct(self, list_vals):
        return sum(list_vals) % self.Q
    
    
    def __add__(self, other):
        C = Kryptonite(0)
        C.embeddings =[(xi + yi) % self.Q for xi, yi in zip(self.embeddings, other.embeddings)]
        return C
    
    
    def __repr__(self):
        return str(self.embeddings)
    
    def get_plain_text(self):
        return self.decode(self.embeddings)