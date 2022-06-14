class Usuario:
    __idUsuario = 0
    __nomUsuario = ""
    __pasUsuario = ""
    __emaUsuario = ""
    __rolUsuario = 0

    def __init__(self):
        pass

    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getNomUsuario(self):
        return self.__nomUsuario
    
    def setNomUsuario(self, nomUsuario):
        self.__nomUsuario = nomUsuario
    
    def getApeUsuario(self):
        return self.__apeUsuario

    def setApeUsuario(self, apeUsuario):
        self.__apeUsuario = apeUsuario

    def getPasUsuario(self):
        return self.__pasUsuario
    
    def setPasUsuario(self, pasUsuario):
        self.__pasUsuario = pasUsuario

    def getEmaUsuario(self):
        return self.__emaUsuario
    
    def setEmaUsuario(self, emaUsuario):
        self.__emaUsuario = emaUsuario

    def getRolUsuario(self):
        return self.__rolUsuario
    
    def setRolUsuario(self, rolUsuario):
        self.__rolUsuario = rolUsuario