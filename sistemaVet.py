class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__medicamento=""

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarMedicamento(self,n):
        self.__medicamento = n 


class sistemaV:
    def __init__(self):
        #self.__lista_mascotas = []
        # self.__lista_mascotas = {}
        self._Felinos = {}
        self._Caninos = {}

    def verificarExisteFelinos(self,historia):
        if historia in self._Felinos:
                 return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verificarExisteCaninos(self,historia):
        for m in self._Caninos:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroFelinos(self):
        return len(self._Felinos) 
    def verNumeroCaninos(self):
        return len(self._Caninos) 

    def ingresarFelinos(self,mascota):
        #self.__lista_mascotas.append(mascota) 
        self._Felinos[mascota.verHistoria()]=mascota
    def ingresarCaninos(self,mascota):
        #self.__lista_mascotas.append(mascota) 
        self._Caninos[mascota.verHistoria()]=mascota

    def verFechaIngresoFelinos(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self._Felinos:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None
    def verFechaIngresoCaninos(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self._Caninos:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamentoFelinos(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self._Felinos:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None
    
    def verMedicamentoCaninos(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self._Caninos:
            if historia == masc.verHistoria():
                return masc.ver_Medicamento() 
        return None

    def eliminarFelinos(self, historia):
        for masc in self._Felinos:
            if historia == masc.verHistoria():
                del self._Felinos[masc]
                #self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 
    
    def eliminarCaninos(self, historia):
        for masc in self._Caninos:
            if historia == masc.verHistoria():
                del self._Canino[masc]
                #self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 


class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        