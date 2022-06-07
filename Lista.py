
from NodoNumero import numero

class listaNumeros():
    
    def __init__(self):
        self.primero: numero = None #Cabecera
        self.ultimo = None
    
    def verificarContenido(self): #Función que verifica si hay elementos
        return self.primero == None #Retorna True si es None o False

    def buscar(self,dato): #Método que recorre de principio a fin hasta encontrar el número
        tmp = self.primero
        verificador = False

        while tmp != None:
            if tmp.numero == dato:
                print('Numero actual:',tmp.numero)

                data1 :numero = tmp.anterior
                data2 :numero = tmp.siguiente
                print('Numero anterior:',data1.numero,'-','Numero siguiente:',data2.numero)
                verificador = True
            
            tmp = tmp.siguiente
            if tmp == self.primero:
                break
        
        if verificador == False:
            print('No se encontró el número')

    def mostrarDatos(self):
        tmp = self.primero
        print('--- Lista de números ingresados ---')
        while tmp != None:
            print(tmp.numero)
            
            tmp = tmp.siguiente
            if tmp == self.primero:
                break

    def insertarFinal(self,num):
        verificador = self.verificarContenido()

        if verificador == True:
            self.primero = self.ultimo = numero(num)
        else:
            tmp = self.ultimo
            self.ultimo = tmp.siguiente = numero(num)
            
            self.ultimo.anterior = tmp
        
        self.enlazarNodos()
     
    def enlazarNodos(self): #Método para unir los nodos ultimo y primero
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero