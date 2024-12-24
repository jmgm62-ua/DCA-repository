def calculadora():
    while True:
        print("\n--- Bienvenido a la Calculadora Interactiva ---")
        print("Seleccione la operación que desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese el número de la operación: "))

            if opcion == 5:
                confirmar = input("¿Está seguro de que desea salir? (s/n): ").strip().lower()
                if confirmar == 's':
                    print("Saliendo de la calculadora. ¡Adiós!")
                    break
                else:
                    print("Operación cancelada. Volviendo al menú principal.")
                    continue

            if opcion not in [1, 2, 3, 4]:
                print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
                continue

            try:
                num1 = float(input("Ingrese el primer número: "))
                if abs(num1) > 1e6:
                    print("Advertencia: El número ingresado es muy grande y podría causar problemas de precisión.")
                num2 = float(input("Ingrese el segundo número: "))
                if abs(num2) > 1e6:
                    print("Advertencia: El número ingresado es muy grande y podría causar problemas de precisión.")
            except ValueError:
                print("Error: Entrada no válida. Por favor, ingrese números válidos.")
                continue

            if opcion == 1:
                resultado = num1 + num2
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == 2:
                resultado = num1 - num2
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == 3:
                resultado = num1 * num2
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == 4:
                try:
                    resultado = num1 / num2
                    print(f"El resultado de la división es: {resultado}")
                except ZeroDivisionError:
                    print("Error: No se puede dividir entre cero.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la operación.")

if __name__ == "__main__":
    calculadora()

