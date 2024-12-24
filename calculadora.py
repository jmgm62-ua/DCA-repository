def calculadora():
    def mostrar_menu():
        print("\n--- Bienvenido a la Calculadora Interactiva ---")
        print("Seleccione la operación que desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

    def obtener_numero(prompt):
        while True:
            try:
                numero = float(input(prompt))
                if abs(numero) > 1e6:
                    print("Advertencia: El número ingresado es muy grande y podría causar problemas de precisión.")
                return numero
            except ValueError:
                print("Error: Entrada no válida. Por favor, ingrese un número válido (por ejemplo, 10, -5, o 3.14).")

    while True:
        mostrar_menu()

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

            num1 = obtener_numero("Ingrese el primer número: ")
            num2 = obtener_numero("Ingrese el segundo número: ")

            if opcion == 1:
                num1 = num1 + 1
                resultado = num1 + num2
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == 2:
                resultado = num1 - num2
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == 3:
                resultado = num1 * num2
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == 4:
                if num2 == 0:
                    print("Error: No se puede dividir entre cero. Intente ingresar un divisor diferente a cero.")
                    continue
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")

        except ValueError:
            print("Error: Por favor, ingrese un número válido para la operación (por ejemplo, 1, 2, 3, etc.).")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo de la calculadora. ¡Hasta luego!")
            break

if __name__ == "__main__":
    calculadora()

