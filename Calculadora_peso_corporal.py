def calcular_imc(peso,estatura):
    imc = peso / (estatura ** 2)
    return imc
def main():
    while True:
        nombre = input ("Ingrese su nombre: ")
        if not nombre:
            print("El campo nombre no puede estar vacío.")
            continue
        apellido_paterno = input("Ingrese su apellido paterno: ")
        if not apellido_paterno:
            print("El campo apellido paterno no puede estar vacío.")
            continue
        apellido_materno = input ("Ingrese su apellido materno: ")
        if not apellido_materno: 
            print("El campo apellido materno no puede estar vacío.")
            continue
        while True:
            try:
                edad = int(input("Ingrese su edad: "))
                if edad <= 0: 
                    print ("La edad debe ser un número positivo.")
                    continue
                break 
            except ValueError:
                print ("El edad debe ser un número entero.")    
        while True:
            try:
                peso = float(input("Ingrese su peso (en kg): "))
                if peso <= 0:
                    print("El peso debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("El peso debe ser un número.")        
        while True:
            try: 
                estatura = float (input("Ingresa su estatura(en metros): "))
                if estatura <= 0:
                    print("La estatura debe ser un numero positivo.")
                    continue
                break 
            except ValueError:
                print("La estatura debe ser un numero.")
                
        imc = calcular_imc(peso, estatura)
        print ("\nDatos del usuario:")
        print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
        print(f"edad:{edad} años")
        print(f"Estatura: {estatura} m")
        print(f"IMC: {imc:.2f}")
        
        if imc < 18.5:
            print("Clasificación: Bajo peso")
        elif imc < 25:
            print("Clasificación: Peso normal")
        elif imc < 30: 
            print("Clasificación: Sobrepeso")
        else:
            print("Clasificación: Obesidad")
            
        respuesta = input("\n¿Desea calcular el IMC de otra persona?: ")
        
        if respuesta.lower() != "si":
            break
    
if __name__ == "__main__":
    main()
            
              
                    
