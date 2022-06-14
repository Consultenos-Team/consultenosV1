class Tique:
    __idTique = 0
    __idCliente = 0
    __idUsuario = 0
    __idArea = 0
    __asuTique = ""
    __detServicio = ""
    __detProblema = ""
    __estTique = 0
    __criticidad = 0
    __tipTique = ""
    __fecCreacion = ""
    __ejeMesa = ""

    def __init__(self):
        pass

    def getIdTique(self):
        return self.__idTique
    
    def setIdTique(self, idTique):
        self.__idTique = idTique

    def getIdCliente(self):
        return self.__idCliente
    
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente
    
    def getIdUsuario(self):
        return self.__idUsuario

    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getIdArea(self):
        return self.__idArea
    
    def setIdArea(self, idArea):
        self.__idArea = idArea

    def getAsuTique(self):
        return self.__asuTique
    
    def setAsuTique(self, asuTique):
        self.__asuTique = asuTique

    def getDetServicio(self):
        return self.__detServicio
    
    def setDetServicio(self, detServicio):
        self.__detServicio = detServicio

    def getDetProblema(self):
        return self.__detProblema
    
    def setDetProblema(self, detProblema):
        self.__detProblema = detProblema

    def getEjeArea(self):
        return self.__ejeArea
    
    def setEjeArea(self, ejeArea):
        self.__ejeArea = ejeArea

    def getEstTique(self):
        return self.__estTique
    
    def setEstTique(self, estTique):
        self.__estTique = estTique

    def getCriticidad(self):
        return self.__criticidad
    
    def setCriticidad(self, criticidad):
        self.__criticidad = criticidad

    def getTipTique(self):
        return self.__tipTique
    
    def setTipTique(self, tipTique):
        self.__tipTique = tipTique

    def getFecCreacion(self):
        return self.__fecCreacion
    
    def setFecCreacion(self, fecCreacion):
        self.__fecCreacion = fecCreacion

    def getEjeMesa(self):
        return self.__ejeMesa
    
    def setEjeMesa(self, ejeMesa):
        self.__ejeMesa = ejeMesa