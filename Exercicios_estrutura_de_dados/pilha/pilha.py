class Pilha:

    def __init__(self):
        self.storage = []

    def pushPilha(self, newValue):
        self.storage.append(newValue)

    def getPilha(self):
        return self.storage