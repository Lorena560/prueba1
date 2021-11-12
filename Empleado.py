from Persona import Persona

class Empleado(Persona):
    cod=0
    usuario=""
    contraseña=""

    def setCod(self, cod):
        self.cod = cod
    def getCod(self):
        return self.cod
    
    def setUsuario(self, usuario):
        self.usuario = usuario
    def getUsuario(self):
        return self.usuario
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña
    def getContraseña(self):
        return self.contraseña