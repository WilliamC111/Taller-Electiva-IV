import json

# Función para cargar los datos del archivo JSON
def cargar_datos():
    with open("Unidad1_Reto.json","r") as j:
        return json.load(j)

# Función para calcular la nota promedio por asignatura
def calcular_promedio_por_asignatura(data):
    promedio_asignaturas = {}
    conteo_asignaturas = {}

    for estudiante in data:
        for asignatura in estudiante["asignaturas"]:
            nombre_asignatura = asignatura["nombre"]
            nota = asignatura["nota"]
            if nombre_asignatura not in promedio_asignaturas:
                promedio_asignaturas[nombre_asignatura] = nota
                conteo_asignaturas[nombre_asignatura] = 1
            else:
                promedio_asignaturas[nombre_asignatura] += nota
                conteo_asignaturas[nombre_asignatura] += 1

    for asignatura, total_notas in promedio_asignaturas.items():
        promedio_asignaturas[asignatura] = total_notas / conteo_asignaturas[asignatura]

    return promedio_asignaturas

# Función para calcular la nota promedio por estudiante de las asignaturas cursadas (No retiradas)
def calcular_promedio_por_estudiante(data):
    promedio_estudiantes = {}

    for estudiante in data:
        total_notas = 0
        conteo_asignaturas = 0
        for asignatura in estudiante["asignaturas"]:
            if asignatura["retirada"] == "No":
                total_notas += asignatura["nota"]
                conteo_asignaturas += 1
        promedio_estudiantes[(estudiante["apellidos"]["primer_apellido"], estudiante["apellidos"].get("segundo_apellido", ""))] = total_notas / conteo_asignaturas if conteo_asignaturas > 0 else 0

    return sorted(promedio_estudiantes.items())

# Función para generar el correo institucional de los estudiantes
def generar_correos(data):
    correos = []
    for estudiante in data:
        primer_nombre = estudiante["nombres"]["primer_nombre"]
        segundo_nombre = estudiante["nombres"].get("segundo_nombre", "")
        primer_apellido = estudiante["apellidos"]["primer_apellido"]
        segundo_apellido = estudiante["apellidos"]["segundo_apellido"]

        if segundo_nombre:
            correo = f"{primer_nombre[0]}{segundo_nombre[0]}.{primer_apellido}{str(estudiante['documento'])[-2:]}@uptc.edu.co"
        else:
            correo = f"{primer_nombre[0]}{primer_apellido[0]}.{segundo_apellido}{str(estudiante['documento'])[-2:]}@uptc.edu.co"

        correos.append((f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}", correo))

    return correos
# Funcion para determinar si un caracter es vocal o no
def es_vocal(caracter):
    vocales = 'aeiouAEIOU'
    if caracter in vocales:
        return True
    else:
        return False
# Funcion Cuadratica
def ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        return "No hay soluciones reales"
# Funcion para imprimir un histograma
def histograma(lista):
    for num in lista:
        print('H' * num)
# Funciones para manejo de cadenas

# Funcion replace
# Esta función reemplaza todas las ocurrencias de una subcadena con otra subcadena dentro de una cadena. 
# Por ejemplo:
def replace(cadena, viejo, nuevo):
    return cadena.replace(viejo, nuevo)   

# Funcion Find
# Esta función devuelve la posición de la primera ocurrencia de una subcadena dentro de una cadena. 
# Por ejemplo:
def find(cadena, subcadena):
    return cadena.find(subcadena)

# Funcion Count
# Esta función devuelve el número de ocurrencias de una subcadena dentro de una cadena.
# Por ejemplo:
def count(cadena, subcadena):
    return cadena.count(subcadena)

# Funcion capitalize
# Esta función devuelve una copia de la cadena con la primera letra en mayúscula y el resto en minúscula.
# Por ejemplo:
def capitalize(cadena):
    return cadena.capitalize()

# Funcion title
# Esta función devuelve una copia de la cadena con la primera letra de cada palabra en mayúscula y el resto en minúscula.
# Por ejemplo:
def title(cadena):
    return cadena.title()

# Funcion rstrip
# Esta función elimina los espacios en blanco al final de una cadena. 
# Por ejemplo:
def rstrip(cadena):
    return cadena.rstrip()

# Funcion index
# Esta función devuelve la posición de la primera ocurrencia de una subcadena dentro de una cadena.
# Por ejemplo:
def index(cadena, subcadena):
    return cadena.index(subcadena)

# Funcion casefold
# Esta función devuelve una versión en minúsculas de la cadena.
# Por ejemplo:
def casefold(cadena):
    return cadena.casefold()

# Funcion division de frases
def process_string(input_string):
    # Split the string into a list of words
    words = input_string.split()

    # Create a string with each character separated by a hyphen
    hyphenated_chars = '-'.join(input_string)

    # Create a string with each word separated by a hyphen
    hyphenated_words = '-'.join(words)

    return words, hyphenated_chars, hyphenated_words        
# Funcion mostrar informacion de empleados con formato especifico
def print_employee_info(employees):
    nombres, edades, pesos = employees
    for i in range(len(nombres)):
        print(f"Empleado # {i + 1}: Nombre: {nombres[i]}, Edad: {edades[i]}, Peso: {pesos[i]}")



# 1.copy(): 
# Crea una copia superficial de la lista, lo que significa que crea una nueva lista con los mismos elementos que la lista original.
# Esto significa que los elementos de la nueva lista son los mismos objetos que los elementos de la lista original.

# 2.remove(): 
# Elimina la primera ocurrencia de un valor específico en la lista. 
# Si el valor no está presente, se genera un error ValueError.

# 3.del: Elimina un elemento o una sección de elementos de una lista utilizando el índice.

# 4.clear(): Elimina todos los elementos de la lista, dejándola vacía.

# 5.in: Se utiliza para verificar si un elemento está presente en la lista. Retorna `True` si el elemento está en la lista, `False` de lo contrario.

# 6.Diferencia entre append() y extend():
#    - append(): Agrega un solo elemento al final de la lista. Si el elemento es una lista, 
#                la lista se agrega como un solo elemento, no se desempaqueta.
#    - extend(): Agrega todos los elementos de una lista (u otro iterable) al final de la lista. 
#               Esto significa que se desempaqueta la lista y sus elementos individuales se agregan a la lista original.



# Funcion para determinar si una lista tiene duplicados
def has_duplicates(lst):
    return len(lst) != len(set(lst))
# Funcion para eliminar duplicados de una lista
def remove_duplicates(lst):
    return list(set(lst))


# La diferencia entre `set` y `frozenset` en Python radica en su mutabilidad. Aquí está la explicación:

# 1. set:
#    - set es una colección de elementos únicos y no ordenados.
#    - Los conjuntos (set) son mutables, lo que significa que se pueden modificar después de su creación. Puedes agregar y eliminar elementos de un conjunto.
#    - Los conjuntos no admiten elementos duplicados, por lo que automáticamente eliminan cualquier duplicado al insertar elementos.
#    - Los conjuntos no son hashables, lo que significa que no se pueden utilizar como elementos en otro conjunto, pero se pueden modificar.

# 2. frozenset:
#    - frozenset es una versión inmutable de un conjunto.
#    - A diferencia de los conjuntos (set), los conjuntos congelados (frozenset) no pueden ser modificados después de su creación. No es posible agregar o eliminar elementos de un frozenset.
#    - Los conjuntos congelados son hashables, lo que significa que se pueden utilizar como elementos en otro conjunto, diccionario, o incluso como claves en un diccionario.
#    - Los elementos de un frozenset también deben ser hashables.


# Funcion intersection_update()
def intersection_update(set1, set2):
    set1.intersection_update(set2)
    return set1

# Funcion isdisjoint()
def isdisjoint(set1, set2):
    return set1.isdisjoint(set2)

# Funcion issubset()
def issubset(set1, set2):
    return set1.issubset(set2)

# Funcion issuperset()
def issuperset(set1, set2):
    return set1.issuperset(set2)

# Funcion pop()
def pop(set1):
    return set1.pop()

# Funcion remove()
def remove(set1, element):
    set1.remove(element)
    return set1

# Funcion symmetric_difference()
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Funcion symmetric_difference_update()
def symmetric_difference_update(set1, set2):
    set1.symmetric_difference_update(set2)
    return set1

# Funcion union()
def union(set1, set2):
    return set1.union(set2)

# Funcion update()
def update(set1, set2):
    set1.update(set2)
    return set1
# Funcion para clasificar palabras por la primera letra
def classify_words(words):
    word_dict = {}
    for word in words:
        if word[0] in word_dict:
            word_dict[word[0]].append(word)
        else:
            word_dict[word[0]] = [word]
    return word_dict

# Funcion para contar las vocales y consonantes en una cadena
def count_letters(cad):
    cad = cad.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "Consonantes": 0}

    for char in cad:
        if char in vowels:
            letter_counts[char] += 1
        elif char.isalpha():
            letter_counts["Consonantes"] += 1

    return letter_counts

# Funcion de cadena a diccionario
def cadena_a_diccionario(cadena):
    # Dividir la cadena por saltos de línea para obtener una lista de clientes
    clientes = cadena.strip().split('\n')
    
    # Obtener los nombres de los campos del encabezado
    campos = clientes[0].split(';')
    
    # Inicializar el diccionario de salida
    diccionario = {}
    
    # Iterar sobre cada cliente y agregarlo al diccionario
    for cliente in clientes[1:]:
        datos_cliente = cliente.split(';')
        datos = {}
        for i, campo in enumerate(campos[1:]): 
            datos[campo] = datos_cliente[i+1]
        diccionario[datos_cliente[0]] = datos
    
    return diccionario


# Función para mostrar menú y ejecutar las actividades
def menu():
    data = cargar_datos()
    opcion = 0
    while opcion != 5:
        print("""\nMENU
     1. Calcular la nota promedio por asignatura
     2. Calcular la nota promedio por estudiante de las asignaturas cursadas (No retiradas)
     3. Generar lista de estudiantes y correos institucionales
-------------------------- 5 Punto  --------------------------------------------
Cuadernillo operaciones y funciones             
     4. Determinar si un caracter es vocal o no
     5. Resolver ecuación cuadrática
     6. Imprimir un histograma
Cuadernillo manejo de cadenas
     7. Funcion replace
     8. Funcion Find
     9. Funcion Count
     10. Funcion capitalize
     11. Funcion title
     12. Funcion rstrip
     13. Funcion index
     14. Funcion casefold
     15. Division de frases  
Cuadernillo de listas
     16. Mostrar informacion de empleados con formato especifico 
     17. Determinar si una lista tiene duplicados
     18. Eliminar duplicados de una lista
Cuadernillo de conjuntos
     19. intersection_update()
     20. isdisjoint()
     21. issubset()
     22. issuperset()
     23. pop()
     24. remove()
     25. symmetric_difference()
     26. symmetric_difference_update()
     27. union()
     28. update()
Cuadernillo de diccionarios
     29. Clasificar palabras por la primera letra
     30. Contar las vocales y consonantes en una cadena
     31. Convertir una cadena a un diccionario
     32. Salir""")

        opcion = int(input("Ingrese el número de la opción que desea ejecutar: "))
        set1 = set([1, 2, 3, 4, 5])
        set2 = set([4, 5, 6, 7, 8])
        if opcion == 1:
            promedio_asignaturas = calcular_promedio_por_asignatura(data)
            print("\nNota promedio por asignatura:")
            for asignatura, promedio in promedio_asignaturas.items():
                print(f"{asignatura}: {promedio:.2f}")

        elif opcion == 2:
            promedio_estudiantes = calcular_promedio_por_estudiante(data)
            print("\nNota promedio por estudiante de las asignaturas cursadas (No retiradas), ordenado por apellido:")
            for estudiante, promedio in promedio_estudiantes:
                print(f"{estudiante}: {promedio:.2f}")

        elif opcion == 3:
            correos = generar_correos(data)
            print("\nLista de estudiantes y correos institucionales:")
            for estudiante, correo in correos:
                print(f"{estudiante}: {correo}")
        elif opcion == 4:
            caracter = input("Ingrese un caracter: ")
            if len(caracter) == 1:
                if es_vocal(caracter):
                    print(f"{caracter} es una vocal")
                else:
                    print(f"{caracter} no es una vocal")
            else:
                print("Por favor, ingrese un solo caracter.")       
        elif opcion == 5:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
            c = float(input("Ingrese el valor de c: "))
            print(f"Las soluciones de la ecuación cuadrática son: {ecuacion_cuadratica(a, b, c)}")
        elif opcion == 6:
            lista = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            histograma(lista)
        elif opcion == 7:
            cadena = input("Ingrese una cadena: ")
            viejo = input("Ingrese la subcadena a reemplazar: ")
            nuevo = input("Ingrese la subcadena de reemplazo: ")
            print(replace(cadena, viejo, nuevo))
        elif opcion == 8:
            cadena = input("Ingrese una cadena: ")
            subcadena = input("Ingrese la subcadena a buscar: ")
            print(find(cadena, subcadena))
        elif opcion == 9:
            cadena = input("Ingrese una cadena: ")
            subcadena = input("Ingrese la subcadena a contar: ")
            print(count(cadena, subcadena))
        elif opcion == 10:
            cadena = input("Ingrese una cadena: ")
            print(capitalize(cadena))
        elif opcion == 11:
            cadena = input("Ingrese una cadena: ")
            print(title(cadena))
        elif opcion == 12:
            cadena = input("Ingrese una cadena: ")
            print(rstrip(cadena))
        elif opcion == 13:
            cadena = input("Ingrese una cadena: ")
            subcadena = input("Ingrese la subcadena a buscar: ")
            print(index(cadena, subcadena))
        elif opcion == 14:
            cadena = input("Ingrese una cadena: ")
            print(casefold(cadena))
        elif opcion == 15:
            input_string = "Gestion de Datos"
            words, hyphenated_chars, hyphenated_words = process_string(input_string)
            print(f"Lista de palabras: {words}")
            print(f"Cadena de caracteres separados por guiones: {hyphenated_chars}")
            print(f"Cadena de palabras separadas por guiones: {hyphenated_words}")
        elif opcion == 16:
            nombres=['Luis','Pedro','Lucia']
            edades=[20,18,30]
            peso=[55.6,60,65.8]
            empleados=[nombres,edades,peso]
            print_employee_info(empleados)
        elif opcion == 17:
            lista = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            if has_duplicates(lista):
                print("La lista tiene duplicados")
            else:
                print("La lista no tiene duplicados")
        elif opcion == 18:
            lista = [int(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            print(remove_duplicates(lista))
        elif opcion == 19:
            print(intersection_update(set1, set2))
        elif opcion == 20:
            print(isdisjoint(set1, set2))
        elif opcion == 21:
            print(issubset(set1, set2))
        elif opcion == 22:
            print(issuperset(set1, set2))
        elif opcion == 23:
            print(pop(set1))
        elif opcion == 24:
            element = int(input("Ingrese el elemento a eliminar: "))
            print(remove(set1, element))
        elif opcion == 25:
            print(symmetric_difference(set1, set2))
        elif opcion == 26:
            print(symmetric_difference_update(set1, set2))
        elif opcion == 27:
            print(union(set1, set2))
        elif opcion == 28:
            print(update(set1, set2))
        elif opcion == 29:
            words = input("Ingrese una lista de palabras separadas por espacios: ").split()
            print(classify_words(words))  
        elif opcion == 30:
            cadena = input("Ingrese una cadena: ")
            print(count_letters(cadena))
        elif opcion == 31:
            # Cadena de entrada
            cadena_entrada = "id;nombre;correo;movil;salario\n3412;Pepe Perez;pepeperez@yahoo.com;300281234;150000\n45342;Maria Melo;mariamelo@yahoo.com;315434223;300000\n5673321;Fernando Jimenez;ferjim@gmail.com;312342234;230000\n4545231;Carlos Cardenas;carloscardenas@hotmail.com;3156754323;345000"
            # Llamar a la función con la cadena de entrada y mostrar el resultado
            resultado = cadena_a_diccionario(cadena_entrada)
            print(resultado)
        elif opcion == 32:
            exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el menú
menu()


#Ejercicio 3 Diccionarios
def convertir_cadena_a_diccionario(cadena):
  """Convierte una cadena con datos de empleados en un diccionario.

  Args:
    cadena: La cadena de texto con los datos de los empleados.

  Returns:
    Un diccionario donde la clave es el ID del empleado y el valor es un diccionario
    con los demás datos.
  """

  lineas = cadena.splitlines()
  encabezados = lineas[0].split(";")
  resultado = {}

  for linea in lineas[1:]:
    campos = linea.split(";")
    empleado = {}
    for i in range(len(campos)):
      empleado[encabezados[i]] = campos[i]
    resultado[empleado['id']] = empleado

  return resultado

# Ejemplo:
cadena_ejemplo = """id;nombre;correo;movil;salario
3412;Pepe Perez;pepeperez@yahoo.com;300281234;150000
45342;Maria Melo;mariamelo@yahoo.com;315434223;300000
5673321;Fernando Jimenez;ferjim@gmail.com;312342234;230000
4545231;Carlos Cardenas;carloscardenas@hotmail.com;3156754323;345000"""

resultado = convertir_cadena_a_diccionario(cadena_ejemplo)
print(resultado)