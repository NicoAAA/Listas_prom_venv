"""
CENTRO DE BIOTECNOLOGIA AGROPECUARIO SENA

FICHA:    2877795
APRENDIZ: NICOLAS ANDRES ACOSTA HIGUERA
FECHA:    06 / 06 / 2024
PROGRMA:  Lista de números aleatorios
VERSION:  5.0
"""

# Importaciones de libreria local
from modules.fnc import  *

def main():
    """
    Función principal que ejecuta el flujo del programa.

    Esta función muestra el título del programa, realiza las operaciones
    de generación y manipulación de listas aleatorias, y pregunta al usuario
    si desea repetir el proceso. Si el usuario decide no continuar, se muestra
    un mensaje de agradecimiento y el programa termina.
    """
    titulo()
    while True:
        operaciones_listas()
        if not pregunta_usuario():
            print('\n¡Gracias por usar el programa!\n')
            break
        
   
# Llamar a la función main    
if __name__ == '__main__':
    main()
