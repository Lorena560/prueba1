from Persona import Persona

class Cliente(Persona):
    nit=0

    def setNit(self, nit):
        self.nit = nit
    def getNit(self):
        return self.nit
    