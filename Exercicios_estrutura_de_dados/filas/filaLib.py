class Fila:

    def __init__(self):
        self.data = []

    def getFila(self):
        return self.data


class Infos:
    def __init__(self):
        self.data = []

    def getInfos(self):
        return self.data

    def insertInfo(self, info):
        self.data.append(info)

