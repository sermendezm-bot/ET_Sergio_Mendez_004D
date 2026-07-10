def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion"))
        except ValueError:
            print("Debe ingresar un digito correcto")
        else: 
            if opcion >=1  and opcion <= 6 :
                return opcion
            else:
                print("Debe ingresar in digito del 1 al 6")


def nombre():
    if nombre.strip() != " ":
        return True
    else:
        return False
    
def categoria():
    if categoria.strip() != " ":
        return True
    else:
        return False

def marca():
    if marca.strip() != " ":
        return True
    else:
        return False

def peso_kg():
    peso_kg == float.peso_kg = 0
    if peso_kg > 0:
        return True
    else:
        return False
    
def es_para_cachorro():
    if es_para_cachorro.lower() == "s" or es_para_cachorro.lower() == "n":
        return True
    else: 
        return False


def es_importado():
    if es_importado.lower() == "s" or es_importado.lower() == "n":
        return True
    else: 
        return False



def precio(valor):
    valor = int(precio)
    if precio > 0:
        return True
    else:
        return False


def unidades(categoria):
    categoria = categoria.upper()
    if codigo(categoria):
        return True
    else:
        return False



def busqueda_precio(p_min, p_max):
    
    
def buscar_codigo(codigo):

    

    
def actualizar_precio(codigo, nuevo_precio):

    
def eliminar_producto(codigo, producto,)
    if buscar_codigo(codigo,)
        producto.pop(codigo)
        return True
    else:
        return False


lista=[]

productos = {
'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
}



stock = {
'M001': [32990, 12],
'M002': [9990, 0],
'M003': [5490, 25],
'M004': [7990, 5],
'M005': [11990, 7],
'M006': [24990, 3],
}

def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion
        if opcion == 1:
            print("Ingrese categoría a consultar: ")
        
        elif opcion ==2:
            print("Ingrese precio mínimo: ")


            print("Ingrese precio mínimo: ")
            print("Ingrese precio máximo: ")
        
        elif opcion ==3:
            print("Ingrese código del producto:")
            print("Ingrese nuevo precio:")

            print("¿Desea actualizar otro precio (s/n)?: n")

        
        elif opcion ==4:
            print("Ingrese código del producto: ")
            print("Ingrese nombre: ")
            print("Ingrese categoría: ")
            print("Ingrese marca: ")
            print("Ingrese peso (kg): ")
            print("¿Es importado? (s/n): ")
            print("¿Es para cachorro? (s/n): ")
            print("Ingrese precio: ")
            print("Ingrese unidades: ")
            print("Producto agregado")
        
        elif opcion ==5:
            print("Ingrese código del producto: ")
            print("Ingrese nombre: ")
            print("Ingrese categoría: ")
            print("Ingrese marca: ")
            print("Ingrese peso (kg): ")
            print("¿Es importado? (s/n): ")
            print("¿Es para cachorro? (s/n): ")
            print("Ingrese precio: ")
            print("Ingrese unidades: ")
            print("Producto eliminado")
        
        elif opcion ==6: 
            print("Programa finalizado.")


