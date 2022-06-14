class Cliente:
    __idCliente = 0
    __nomCliente = ""
    __rutCliente = ""
    __direccion = ""
    __contacto = ""

    def __init__(self):
        pass

    def getIdCliente(self):
        return self.__idCliente
    
    def setIdCliente(self, idCliente):
        self.__idCliente = idCliente

    def getNomCliente(self):
        return self.__nomCliente
    
    def setNomCliente(self, nomCliente):
        self.__nomCliente = nomCliente
    
    def getRutCliente(self):
        return self.__rutCliente

    def setRutCliente(self, rutCliente):
        self.__rutCliente = rutCliente

    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getContacto(self):
        return self.__contacto
    
    def setContacto(self, contacto):
        self.__contacto = contacto

