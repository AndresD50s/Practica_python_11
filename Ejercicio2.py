# Menú de selección de programas

def programa1():
    # Saludo personalizado
    nombre = input("Por favor, escribe tu nombre: ")
    print(f"¡Hola {nombre}! Es un placer conocerte.")

def programa2():
    # Cálculo de perímetro y área de un círculo
    import math
    radio = float(input("Ingrese el radio del círculo: "))
    perimetro = 2 * math.pi * radio
    area = math.pi * (radio ** 2)
    print(f"El perímetro del círculo es: {perimetro}")
    print(f"El área del círculo es: {area}")

def programa3():
    # Promedio de 4 notas
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    nota4 = float(input("Ingrese la cuarta nota: "))
    
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"El promedio de las notas es: {promedio}")

def programa4():
    # Conversor de centímetros a pulgadas
    centimetros = float(input("Ingrese la medida en centímetros: "))
    pulgadas = centimetros / 2.54
    print(f"{centimetros} centímetros equivalen a {pulgadas} pulgadas")

def programa5():
    # Invertir un número de 3 dígitos
    numero = input("Ingrese un número entero de tres dígitos: ")
    if len(numero) != 3 or not numero.isdigit():
        print("Error: Debe ingresar un número de exactamente 3 dígitos")
    else:
        numero_invertido = numero[::-1]
        print(f"El número invertido es: {numero_invertido}")

def mostrar_menu():
    print("\n=== MENÚ DE PROGRAMAS ===")
    print("1. Programa de saludo personalizado")
    print("2. Programa para calcular perímetro y área de un círculo")
    print("3. Programa para calcular promedio de 4 notas")
    print("4. Programa para convertir centímetros a pulgadas")
    print("5. Programa para invertir número de 3 dígitos")
    print("6. Salir")
    return input("Seleccione una opción (1-6): ")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            programa1()
        elif opcion == "2":
            programa2()
        elif opcion == "3":
            programa3()
        elif opcion == "4":
            programa4()
        elif opcion == "5":
            programa5()
        elif opcion == "6":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()