class Ordenador:
    def __init__(self, procesador, memoria_ram, almacenamiento_total, sistema_operativo):
        self.__procesador=procesador
        self.__memoria_ram=memoria_ram
        self.__sistema_operativo=sistema_operativo
        self.__almacenamiento_total=almacenamiento_total
        self.__encendido=False 
    
    def get_procesador(self):
        return self.__procesador
    
    def get_memoria_ram(self):
        return self.__memoria_ram
    
    def get_almacenamiento_total(self):
        return self.__almacenamiento_total
    
    def get_sistema_operativo(self):
        return self.__sistema_operativo
    
    def get_encendido(self):
        return self.__encendido
    
    def set_procesador(self, procesador):
        self.__procesador=procesador
    
    def set_memoria_ram(self, memoria_ram):
        self.__memoria_ram=memoria_ram

    def set_almacenamiento_total(self, almacenamiento_total):
        self.__almacenamiento_total=almacenamiento_total

    def set_sistema_operativo(self, sistema_operativo):
        self.__sistema_operativo=sistema_operativo

    def encender(self):
        if self.__encendido == False:
            self.__encendido = True
            print("Ordenador encendido")
        else:
            print("El ordenador ya está encendido")

    def apagar(self):
        if self.__encendido == True:
            self.__encendido = False
            print("Ordenador apagado")
        else:
            print("El ordenador ya esta apagado")
    
    def reiniciar(self):
        if self.__encendido==True:
            print("Reiniciando el ordenador")
            self.apagar()
            self.encender()
        else:
            print("El ordenador esta apagado")
    
    def aumentar_memoria_ram(self, cantidad):
        self.__memoria_ram+=cantidad
    
    def calcular_valor(self):
        return (self.__almacenamiento_total / 2)* self.__memoria_ram 
    
    def __str__(self):
        return f"Procesador {self.__procesador} y {self.__procesador}GB de ram" 
    
    def ordenadores_iguales(self, otro_pc):
        return  "Son iguales" if self.__str__() == otro_pc.__str__() and self.__sistema_operativo == otro_pc.__sistema_operativo else "No son iguales"
    
    def ordenar_valor(self, *args):
        lista_valores=[]
        lista_valores.append(self.calcular_valor())
        for i in args:
            lista_valores.append(i.calcular_valor())
        return sorted(lista_valores, reverse=True)

pc1 = Ordenador("Intel i7", 16, 512, "Windows 10")
pc2 = Ordenador("Intel i7", 16, 1024, "Windows 10")
pc3 = Ordenador("Ryzen 5", 16, 512, "Windows 10")
pc4 = Ordenador("Ryzen 5", 8, 512, "Windows 10")

print(pc1.ordenadores_iguales(pc2))
print(pc1.ordenadores_iguales(pc3)) 

print(pc1.ordenar_valor(pc2, pc3, pc4))

        

