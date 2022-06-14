class Area:
    __idArea = 0
    __nomArea = ""
    __nomEje = ""

    def __init__(self):
        pass

    def getIdArea(self):
        return self.__idArea
    
    def setIdArea(self, idArea):
        self.__idArea = idArea

    def getNomArea(self):
        return self.__nomArea
    
    def setNomArea(self, nomArea):
        self.__nomArea = nomArea
    
    def getNomEje(self):
        return self.__nomEje

    def setNomEje(self, nomEje):
        self.__nomEje = nomEje

