import random

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
        return f"Procesador {self.__procesador} y {self.__sistema_operativo}GB de ram" 
    
    def ordenadores_iguales(self, otro_pc):
        return  "Son iguales" if self.__str__() == otro_pc.__str__() and self.__sistema_operativo == otro_pc.__sistema_operativo else "No son iguales"
    
    def ordenar_valor(self, *args):
        valores = [pc.calcular_valor() for pc in (self, *args)]
        return sorted(valores, reverse=True)

'''pc1 = Ordenador("Intel i7", 16, 512, "Windows 10")
pc2 = Ordenador("Intel i7", 16, 1024, "Windows 10")
pc3 = Ordenador("Ryzen 5", 16, 512, "Windows 10")
pc4 = Ordenador("Ryzen 5", 8, 512, "Windows 10")

print(pc1.ordenadores_iguales(pc2))
print(pc1.ordenadores_iguales(pc3)) 

print(pc1.ordenar_valor(pc2, pc3, pc4))'''


class Sobremasa(Ordenador):
    def __init__(self, dimension_caja, almacenamiento_total, tarjeta_grafica, procesador, memoria_ram, sistema_operativo):
        super().__init__(procesador, memoria_ram, almacenamiento_total, sistema_operativo)
        self.dimension_caja=dimension_caja
        self.almacenamiento_actual=almacenamiento_total-20
        self.tarjeta_grafica=tarjeta_grafica

    def calcular_volumen_caja(self):
        resultado=1
        for i in self.dimension_caja:
            resultado*=i
        return resultado
        
    def descargar_archivos(self):
        self.almacenamiento_actual-=20
        
    ''''def ordenar_valor(self, *args):
        lista_valores=[]
        lista_valores.append(self.calcular_valor())
        for i in args:
            lista_valores.append(i.calcular_valor( ))
        for i in lista_valores:
            if 
        return sorted(lista_valores, reverse=True)'''
    
class Portatil(Ordenador):
    def __init__(self, porcentaje_bateria_actual, modelo, procesador, memoria_ram, almacenamiento_total, sistema_operativo):
        super().__init__(procesador, memoria_ram, almacenamiento_total, sistema_operativo)
        self.porcentaje_bateria_actual=porcentaje_bateria_actual
        self.modelo=modelo

    def usar_ordenador(self):
        self.porcentaje_bateria_actual-=15*random.randint(1,4)
        if self.porcentaje_bateria_actual<=0:
            print("Ordenador sin bateria")

    def cargar_ordenador(self, horas_carga):
        self.porcentaje_bateria_actual+=30*horas_carga
        if self.porcentaje_bateria_actual>=100:
            print("Ordenador al 100 de bateria")
            self.porcentaje_bateria_actual=100
    
pc1 = Ordenador("Intel i7", 16, 512, "Windows 10")
pc2 = Ordenador("Ryzen 5", 8, 1024, "Windows 11")
pc3_sobremesa = Sobremasa((40, 20, 50), 1024, "NVIDIA RTX 3060", "Intel i5", 16, "Ubuntu")
pc4_sobremesa = Sobremasa((50, 25, 60), 2048, "AMD RX 6600", "Ryzen 7", 32, "Windows 10")
pc5_portatil = Portatil(80, "HP Envy", "Intel i7", 16, 512, "Windows 10")
pc6_portatil = Portatil(45, "Asus ROG", "Ryzen 5", 32, 1024, "Windows 11")





    

        
