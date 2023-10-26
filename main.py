from tp5 import*

#Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

#Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

#Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor. Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

#Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.

#Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

#Escribir una función que calcule el módulo de un vector.

#Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

#Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

#Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.

#Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.

print("Trabajo practico N°5")
exit=False

while exit==False:
  option=int(input("Ingrese un ejercicio: 1 a 17; (0 para salir): "))
  if option<0 or option>17:
    print("Opcion no valida")
  else:
    if option==1:
      print("Ejercicio 1")
      n_ID=input("Ingrese su DNI: ")
      if validate_ID(n_ID)==True:
        print("DNI Correncto")
      else:
        print("DNI Incorrecto")
    elif option==2:
      print("Ejercicio 2")
      phrase=input("Ingrese una frase: ")
      print(f"La ultima palabra de su frase tiene {return_last_word_len(phrase)} letras")
    elif option==3:
      print("Ejercicio 3")
      cont=1
      while True:
        id_member=club_ID(cont)
        if id_member==None:##si el primer nombre es vacio, caso para salir
          break
        else:
          print(f"ID del miembro N°{cont}: {id_member}")
          cont+=1
    elif option==4:
      print("Ejercicio 4")
      res=calculate_multiples(int(input("Ingrese un numero: ")),int(input("Ingrese otro numero: ")))
      if res==True:
        print("El primero es multiplo del segundo")
      elif res==False:
        print("El segundo es multiplo del primero")
      else:
        print("Ninguno es multiplo del otro")
    elif option==5:
      print("Ejercicio 5")
      days=int(input("Introduce el numero de dias: "))
      for i in range(days):
        max=int(input("Introduce la temperatura maxima del dia: "))
        min=int(input("Introduce la temperatura minima del dia: "))
        mid=medium_temperature(max,min)
        print(f"La temperatura media del dia {i+1} es: {mid}")
    elif option==6:
      print("Ejercicio 6")
      text=add_spaces(input("Ingrese una frase: "))
      print("Su Frase con espacios es: ",text)
    elif option==7:
      print("Ejercicio 7")
    elif option==8:
      print("Ejercicio 8")
    elif option==9:
      print("Ejercicio 9")
    elif option==10:
      print("Ejercicio 10")
    elif option==11:
      print("Ejercicio 11")
    elif option==12:
      print("Ejercicio 12")
    elif option==13:
      print("Ejercicio 13")
    elif option==14:
      print("Ejercicio 14")
    elif option==15:
      print("Ejercicio 15")
    elif option==16:
      print("Ejercicio 16")
    elif option==17:
      print("Ejercicio 17")
    elif option==0:
      print("Salir")
      exit=True