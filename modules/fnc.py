"""
CENTRO DE BIOTECNOLOGIA AGROPECUARIO SENA

FICHA:    2877795
APRENDIZ: NICOLAS ANDRES ACOSTA HIGUERA
FECHA:    06 / 06 / 2024
PROGRMA:  Lista de números aleatorios(Funciones)
VERSION:  5.0
"""

# Importaciones de la biblioteca estándar
from random import randint

# Importaciones de terceros
from tabulate import tabulate



def titulo():
    """
    Imprime el título y la introducción del programa.
    
    Esta función muestra una serie de mensajes al usuario,
    explicando el propósito del programa y esperando que el
    usuario presione Enter para continuar.
    """
    print('*-'*35)
    print('\n                   Bienvenido a Listas Aleatorias\n')
    print('*-'*35)
    print(input('\nPresione enter para continuar . . . '))
    print('-'*60)
    print('\nEste programa genera un lista de números aleatorios,\nluego  muestra  los  numeros pares e impartes  y el\npromedio de la lista completa.\n')
    print('-'*60)
    print(input('\nPresione enter para continuar . . . '))


def pregunta_usuario():
    """
    Pregunta al usuario si desea generar una lista de números aleatorios.
    
    Esta función muestra un mensaje al usuario y espera una respuesta. 
    Si el usuario responde con 's' (para sí) o 'n' (para no), la función 
    retorna True o False, respectivamente. Si la entrada no es válida, 
    se le pedirá al usuario que ingrese una opción válida.
    
    Returns:
        bool: True si el usuario desea generar la lista, False en caso contrario.
    """
    print('-'*60)
    while True:

        r = input('\n\n¿Desea generar una lista de números aleatorios?\nResponda con "s" para si o "n" para no (s/n): \n').strip().lower()
        if  r  in  ['s','n'] :  
            return r == 's'
        else :
            print('\n¡INGRESE UNA OPCION VALIDA!')


def listas_aleatorias():
    """
    Genera una lista de números aleatorios entre 0 y 20.

    La función genera números aleatorios entre 0 y 20 y los agrega a una lista
    hasta que se genere un 0, en cuyo caso se detiene y retorna la lista generada.
    
    Returns:
        list: Lista de números aleatorios generados.
    """
    lista= []
    while True:
        n= randint(0,20)
        if n != 0:
            lista.append(n)
        elif n == 0:
                break
    
    return lista

def datos_generados(lista):
    contador = 0
    for i in lista:
        contador += 1
    
    return contador


def operaciones_listas():
    """
    Realiza operaciones con una lista de números aleatorios.

    La función genera una lista de números aleatorios, luego separa los números
    pares e impares en listas diferentes. Calcula el promedio de la lista completa
    y muestra los datos en una tabla con el formato 'fancy_grid'.
    """
    # Se definen listas para números pares e impares
    listas= listas_aleatorias()
    pares= [x for x in listas if x % 2 == 0]
    impar= [x for x in listas if x % 2 == 1]

    # Se establecen variables para asignar los  generados, la suma de estos y sus promedios.
    generados= datos_generados(listas)
    suma= sum(listas)
    promedio= round(sum(listas) / len(listas),2)
    
    
    # Calcular la longitud máxima entre las listas
    elementos_max = max(len(listas), len (pares), len(impar))

    # Rellenar las listas más cortas con None
    listas += [None] * (elementos_max - len(listas))
    pares += [None] * (elementos_max - len(pares))
    impar += [None] * (elementos_max - len(impar))

    datos= list(zip(listas,pares,impar))
    
    # Definir los encabezados de las columnas
    encabezados= ['Números Generados', 'Números Pares', 'Números Impares']

    # Imprimir la tabla usando tabulate
    print('Se generaron {0} números'.format(generados))
    print (tabulate(datos,headers= encabezados, tablefmt= 'fancy_grid'))
    print ('\nEl promedio de los números generados es: ',promedio)
    print ('\nLa suma de los números generados es: ',suma)

      




   
