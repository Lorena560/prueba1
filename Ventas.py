from Empleado import Empleado

class Ventas(Empleado):
    totalVent = 0.0
    porComision = 0.0

    def setTotalVent(self, totalVent):
        self.totalVent = totalVent
    def getTotalVent(self):
        return self.totalVent
    
    def setPorComision(self, porComision):
        self.porComision = porComision
    def getPorComision(self):
        return self.porComision

    def getSuelLiquido(self):
        return self.totalVent * 0.03
