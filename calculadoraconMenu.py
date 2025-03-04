def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def division(a, b):
    if b == 0:
        return "Error: division por cero"
    return a/b

def mostrar_menu():
    print("Calculadora Basica Aragon y Dominguez")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. SALIR")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-5): ")
        if opcion == "5":
            print("Estas saliendo de la calculadora ¡Hasta Luego!")
            break
        if opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Introduce el primer número"))
            num2  = float(input("Introduce el segundo número"))
            if opcion == "1":
                resultado = suma(num1, num2)
                print(f"El resultado de {num1} + {num2} es: {resultado}")
            elif opcion == "2":
                resultado = resta(num1, num2)
                print(f"El resultado de {num1} - {num2} es: {resultado}")
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
                print(f"El resultado de {num1} * {num2} es: {resultado}")
            elif opcion == "4":
                resultado = division(num1, num2)
                print(f"El resultado de {num1} / {num2} es: {resultado}")
        else:
            print("Opción no valida. Por favor, selecciona una opción del 1 al 5")
if __name__ == "__main__":
    calculadora()

