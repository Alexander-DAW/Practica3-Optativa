class Libro:
    def __init__(self, titulo, autor, ISBN, edad_minima_requerida, numero_paginas, numero_copias_disponibles):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.edad_minima_requerida=edad_minima_requerida
        self.numero_paginas=numero_paginas
        self.numero_copias_disponibles=numero_copias_disponibles

    def __str__(self):
        return f"{self.titulo} ({self.autor})"
    
    def mostrar_info(self, libro):
        lista=[libro]
        print(f"{self.titulo} - {self.autor}")
        for i in lista:
            print(f"{i.titulo} - {i.autor}")

    def comparar_ISBN(self, otro_libro):
        return True if self.ISBN==otro_libro.ISBN else False
    
    def ordenar_libros(self, *args):
        lista_num_paginas=[x.numero_paginas for x in (self, *args)]
        lista_ordenada=sorted(lista_num_paginas, reverse=True)
        for i in (self, *args):
            lista_ordenada=[i.titulo if num_paginas == i.numero_paginas else num_paginas for num_paginas in lista_ordenada]
        return lista_ordenada
    
class Cliente:
    def __init__(self, nombre, edad, dni, libros_prestados, libros_devueltos):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        self.es_vip=False
        self.libros_prestados=libros_prestados
        self.libros_devueltos=libros_devueltos

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
        
    def membresia_VIP(self):
        if self.es_vip:
            self.es_vip=False
        else:
            self.es_vip=True

    def mostrar_info(self, otro_cliente):
        lista=[otro_cliente]
        print(f"{self.nombre} - {self.edad}")
        for i in lista:
            print(f"{i.nombre} - {i.edad}")
    
    def __eq__(self, otro_cliente):
        return self.dni == otro_cliente.dni
    
    def ordenar_clientes(self, *args):
        libros_clientes=[len(x.libros_devueltos) + len(x.libros_prestados) for x in (self, *args)]
        lista_ordenada=sorted(libros_clientes, reverse=True)
        for i in (self, *args):
            lista_ordenada=[i.nombre if num_libros == len(i.libros_devueltos) + len(i.libros_prestados) else num_libros for num_libros in lista_ordenada]
        return lista_ordenada

class Biblioteca:
    def __init__(self, nombre, clientes, lista_libros):
        self.nombre=nombre
        self.clientes=clientes
        self.lista_libros=lista_libros

    def añadir_libro(self, libro):
        self.lista_libros.append(libro)
    
    def buscar_libro(self, libro):
        return libro if libro in self.lista_libros else "No se ha encontrado ese libro"
        
    def buscar_cliente(self, cliente):
        return cliente if cliente in self.clientes else "No se ha encontrado ese cliente"
    
    '''def añadir_cliente(self, cliente):
        self.clientes.append(cliente)
        for cliente.libros_prestados in self.lista_libros:'''
    
    def copias_totales_libro(self, libro):
        return libro.numero_copias_disponibles+self.lista_libros.count(libro)
    
    def reservar_libro(self, cliente, libro):
        if libro.numero_copias_disponibles>0 and libro not in cliente.libros_prestados:
            cliente.libros_prestados.append(libro)
            libro.numero_copias_disponibles-=1
    
    def devolver_libro(self, cliente, libro):
        cliente.libros_prestados.remove(libro)
        libro.numero_copias_disponibles+=1
    
    def mostrar_lista_clientes(self):
        for cliente in sorted(self.clientes, key=lambda cliente: cliente.nombre):
            print(cliente)
        
    def mostrar_lista_libros(self):
        for libro in sorted(self.lista_libros, key=lambda libro: libro.titulo):
            print(libro)
           

'''libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "1111", 7, 100, 4)
libro2 = Libro("It", "Stephen King", "2222", 18, 1200, 2)
libro3 = Libro("Harry Potter", "J.K. Rowling", "3333", 10, 500, 8)
lista_libros=[libro1,libro3]
libro2.mostrar_info(lista_libros)
print(libro1.comparar_ISBN(libro2))
print(libro1.ordenar_libros(libro2,libro3))'''
