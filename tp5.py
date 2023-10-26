#Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def validate_ID(n):
  if len(n)>=7 and len(n)<=8:
    return True
  else:
    return False
#Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
def return_last_word_len(string):
  palabra=string.split()
  return len(palabra[-1])
#Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio. Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno. Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto. Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo: Nombre: María Ines Rosales; DNI: 25469648; ID -> Maria7254
def club_ID(cont):
  print("Miembro N°",cont,"(Si no hay mas miembros, ingrese un nombre vacio) :")
  name1=input("Ingrese su nombre: ")
  ###Caso para salir
  if name1=="":
    print("*Finalizado*")
    return None
  ###
  name2=input("Ingrese su segundo nombre (si tiene): ")
  last_name=input("Ingrese su apellido: ")
  flag=False##Para dejar de pedir el dni en caso de que no sea valido
  while flag==False:
    dni=input("Ingrese su DNI: ")
    if validate_ID(dni)!=True:
      print("DNI incorrecto")
    else:
      flag=True
  return(name1+str(len(last_name))+dni[:3])

#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
def calculate_multiples(n1,n2):
  if n1 % n2 == 0:
    #print(f"{n1} es multiplo de {n2}")
    return True
  elif n2 % n1 == 0:
    #print(f"{n2} es multiplo de {n1}")
    return False
  else:
    #print("Ninguno es multiplo del otro")
    return None

#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
def medium_temperature(max,min):
  return ((max-min)/2)+min

#Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.
def add_spaces(text):
  return " ".join(text)