class Persona():
    nombres=""
    apellidos=""
    telefono=0
    direc=""
    genero=""

    def setNombres(self, nombres):
        self.nombres = nombres
    def getNombres(self):
        return self.nombres

    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def getApellidos(self):
        return self.apellidos
    
    def setTelefono(self, telefono):
        self.telefono = telefono
    def getTelefono(self):
        return self.telefono
    
    def setDirec(self, direc):
        self.direc = direc
    def getDirec(self):
        return self.direc
    
    def setGenero(self, genero):
        self.genero = genero
    def getGenero(self):
        return self.genero