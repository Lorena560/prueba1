from Empleado import Empleado

class Administracion(Empleado):
    sueldoBa = 0.0
    boni = 0.0
    puesto = ""


    def setSueldoBa(self, sueldoBa):
        self.sueldoBa = sueldoBa
    def getSueldoBa(self):
        return self.sueldoBa
    
    def setBoni(self, boni):
        self.boni = boni
    def getBoni(self):
        return self.boni

    def setPuesto(self, puesto):
        self.puesto = puesto
    def getPuesto(self):
        return self.puesto

    def getSueldoLi(self):
        return self.sueldoBa + self.boni - (self.sueldoBa * 0.0483)