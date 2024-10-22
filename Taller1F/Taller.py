#Taller Unidad1
#William cely López     202012319
#Nicolás Esteban Peña   202010609

import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, ttk
import math
from datetime import datetime

# Función para cargar los datos del archivo JSON
def cargar_datos():
    try:
        with open("Unidad1_Reto.json", "r") as j:
            return json.load(j)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo JSON no se encontró.")
        return []

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

# Función para resolver la ecuación cuadrática 
def ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return f"Las soluciones son: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Hay una única solución: x = {x}"
    else:
        return "No hay soluciones reales."

# Función para resolver la ecuación cuadrática - Funciones
def formula_cuadratica(a, b, c):
    if a == 0:
        return "El valor de 'a' no puede ser 0."
    
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales."
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Hay una única solución: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones son: x1 = {x1}, x2 = {x2}"

# Función para manejar el botón de Operadores
def resolver_ecuacion_operadores(entry_a, entry_b, entry_c):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        resultado = ecuacion_cuadratica(a, b, c)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# Función para manejar el botón de Funciones
def resolver_ecuacion_funciones(entry_a, entry_b, entry_c):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        resultado = formula_cuadratica(a, b, c)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# Función para determinar si un carácter es vocal o no
def es_vocal(entry_caracter):
    caracter = entry_caracter.get()
    if len(caracter) != 1:
        messagebox.showerror("Error", "Por favor ingresa solo un carácter.")
    else:
        vocales = 'aeiouAEIOU'
        if caracter in vocales:
            messagebox.showinfo("Resultado", f"'{caracter}' es una vocal.")
        else:
            messagebox.showinfo("Resultado", f"'{caracter}' no es una vocal.")

# Función para imprimir un histograma con letras 'H'
def histograma(lista):
    histograma_resultado = ""
    for num in lista:
        histograma_resultado += 'H' * num + "\n"
    messagebox.showinfo("Histograma", histograma_resultado)

# Función para generar y mostrar el histograma
def generar_histograma():
    data = [5, 7, 8, 5, 7, 5, 10, 9, 6, 5]  # Datos de ejemplo
    histograma(data)

# Reemplaza todas las ocurrencias de una subcadena por otra.
def ejemplo_replace():
    frase = "Analítica de Datos"
    resultado = frase.replace("Datos", "Información")
    messagebox.showinfo("Replace", f"Original: {frase}\nReplace: {resultado}")

#Devuelve el índice de la primera ocurrencia de una subcadena. Si no se encuentra, devuelve -1
def ejemplo_find():
    frase = "Analítica de Datos"
    posicion = frase.find("Datos")
    messagebox.showinfo("Find", f"Original: {frase}\nPosición de 'Datos': {posicion}")
    
#Devuelve el número de ocurrencias de una subcadena dentro de una cadena.
def ejemplo_count():
    frase = "Gestión de Datos"
    contador = frase.count("Datos")
    messagebox.showinfo("Count", f"Original: {frase}\nCantidad de 'Datos': {contador}")
    
#Retorna una copia de la cadena con la primera letra en mayúscula y el resto en minúscula.
def ejemplo_capitalize():
    frase = "gestión de datos"
    capitalizado = frase.capitalize()
    messagebox.showinfo("Capitalize", f"Original: {frase}\nCapitalizado: {capitalizado}")

def ejemplo_title():
    frase = "gestión de datos"
    titulo = frase.title()
    messagebox.showinfo("Title", f"Original: {frase}\nTitle Case: {titulo}")
    
#Elimina los espacios en blanco al final de una cadena.
def ejemplo_rstrip():
    frase = "Gestión de Datos   "
    resultado = frase.rstrip()
    messagebox.showinfo("Rstrip", f"Original con espacios: '{frase}'\nRstrip: '{resultado}'")
    
#Devuelve la posición de la primera ocurrencia de una subcadena dentro de una cadena.
def ejemplo_index():
    frase = "Analítica de Datos"
    indice = frase.index("Datos")
    messagebox.showinfo("Index", f"Original: {frase}\nÍndice de 'Datos': {indice}")
    
#Retorna una versión en minúsculas de la cadena.
def ejemplo_casefold():
    frase = "GESTIÓN DE DATOS"
    resultado = frase.casefold()
    messagebox.showinfo("Casefold", f"Original: {frase}\nCasefold (minúsculas): {resultado}")
    
#Función para dividir la cadena en palabras y devolver una lista de palabras.
def ejemplo_manipulacion_cadenas():
    frase = "Gestión de Datos"
    palabras = frase.split()
    letras_unidas = '-'.join(frase)
    frase_reemplazada = frase.replace(' ', '-')
    
    resultado = f"Entrada: {frase}\n\nDividido en palabras: {palabras}\nFusionado en letras: {letras_unidas}\nReemplazo de espacios: {frase_reemplazada}"
    messagebox.showinfo("Manipulación de Cadenas", resultado)

def ejemplo_fecha():
    fecha_actual = datetime.now()
    mes = fecha_actual.strftime("%m")
    messagebox.showinfo("Fecha Actual", f"Fecha: {fecha_actual.date()}\nMes: {mes}")

# Funciones relacionadas con listas
def mostrar_empleados(nombres, edades, peso):
    empleados = list(zip(nombres, edades, peso))
    resultado = "\n".join([f"Empleado #{i + 1}: Nombre: {nombre}, Edad: {edad}, Peso: {peso_}" 
                           for i, (nombre, edad, peso_) in enumerate(empleados)])
    messagebox.showinfo("Información de Empleados", resultado)

def tiene_duplicados(lista):
    return len(lista) != len(set(lista))

def eliminar_duplicados(lista):
    return list(set(lista))

# Definición de las funciones para cada operación de conjuntos

def intersection_update(conjunto1, conjunto2):
    conjunto1.intersection_update(conjunto2)
    return f"Resultado de intersection_update: {conjunto1}"

def isdisjoint(conjunto1, conjunto2):
    return f"¿Son disjuntos?: {conjunto1.isdisjoint(conjunto2)}"

def issubset(conjunto1, conjunto2):
    return f"¿Es subconjunto?: {conjunto1.issubset(conjunto2)}"

def issuperset(conjunto1, conjunto2):
    return f"¿Es superconjunto?: {conjunto1.issuperset(conjunto2)}"

def pop_element(conjunto1):
    elemento = conjunto1.pop()
    return f"Elemento extraído con pop: {elemento}\nConjunto restante: {conjunto1}"

def symmetric_difference_update(conjunto1, conjunto2):
    conjunto1.symmetric_difference_update(conjunto2)
    return f"Resultado de symmetric_difference_update: {conjunto1}"

def union(conjunto1, conjunto2):
    union_set = conjunto1.union(conjunto2)
    return f"Resultado de union: {union_set}"

def update(conjunto1, conjunto2):
    conjunto1.update(conjunto2)
    return f"Resultado de update: {conjunto1}"

def remove(conjunto1, elemento):
    conjunto1.remove(elemento)
    return f"Resultado de remove ({elemento}): {conjunto1}"

def symmetric_difference(conjunto1, conjunto2):
    sim_diff = conjunto1.symmetric_difference(conjunto2)
    return f"Resultado de symmetric_difference: {sim_diff}"

# Función para agrupar palabras que comienzan con la misma letra
def agrupar_por_inicial():
    words = ['apple', 'bat', 'bar', 'atom', 'book', 'cat']
    diccionario = {}
    for palabra in words:
        letra_inicial = palabra[0].lower()
        if letra_inicial not in diccionario:
            diccionario[letra_inicial] = []
        diccionario[letra_inicial].append(palabra)
    resultado = "\n".join([f"{letra}: {', '.join(diccionario[letra])}" for letra in diccionario])
    messagebox.showinfo("Agrupar por Inicial", resultado)

# Función para contar vocales y consonantes y devolver un diccionario
def contar_vocales_consonantes_diccionario(cadena):
    vocales = 'aeiouAEIOU'
    contador_vocales = {v: 0 for v in 'aeiou'}
    contador_consonantes = 0
    for letra in cadena:
        if letra.lower() in vocales:
            contador_vocales[letra.lower()] += 1
        elif letra.isalpha():
            contador_consonantes += 1
    contador_vocales['Consonantes'] = contador_consonantes
    resultado = str(contador_vocales)
    messagebox.showinfo("Conteo de Vocales y Consonantes", resultado)

# Función para convertir la información de clientes en un diccionario
def convertir_cadena_a_diccionario():
    cadena = """id;nombre;correo;movil;salario
3412;Pepe Perez;pepeperez@yahoo.com;300281234;150000
45342;Maria Melo;mariamelo@yahoo.com;315434223;300000
5673321;Fernando Jimenez;ferjim@gmail.com;312342234;230000
4545231;Carlos Cardenas;carloscardenas@hotmail.com;3156754323;345000"""
    
    lineas = cadena.split("\n")
    encabezados = lineas[0].split(";")
    diccionario_empleados = {}
    
    for linea in lineas[1:]:
        datos = linea.split(";")
        id_empleado = datos[0]
        diccionario_empleados[id_empleado] = {encabezados[i]: datos[i] for i in range(1, len(encabezados))}
    
    resultado = str(diccionario_empleados)
    messagebox.showinfo("Diccionario de Empleados", resultado)
    
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para mostrar el menú de notas
def mostrar_menu_notas():
    ventana_notas = tk.Toplevel(ventana)
    ventana_notas.title("Notas y Estudiantes")

    data = cargar_datos()
    if not data:
        return  # Si no se pueden cargar los datos, salir de la función

    opciones = ['Promedio por Asignatura', 'Promedio por Estudiante', 'Generar Correos']

    combo = ttk.Combobox(ventana_notas, values=opciones)
    combo.pack()

    def ejecutar_opcion_notas():
        seleccion = combo.get()
        if seleccion == 'Promedio por Asignatura':
            resultado = calcular_promedio_por_asignatura(data)
            messagebox.showinfo("Promedio por Asignatura", str(resultado))
        elif seleccion == 'Promedio por Estudiante':
            resultado = calcular_promedio_por_estudiante(data)
            messagebox.showinfo("Promedio por Estudiante", str(resultado))
        elif seleccion == 'Generar Correos':
            resultado = generar_correos(data)
            messagebox.showinfo("Generar Correos", str(resultado))

    tk.Button(ventana_notas, text="Ejecutar", command=ejecutar_opcion_notas).pack()

# Función para mostrar el menú de operadores
def mostrar_menu_operadores():
    ventana_operadores = tk.Toplevel(ventana)
    ventana_operadores.title("Operadores - Ecuación Cuadrática")

    tk.Label(ventana_operadores, text="Valor de a:").pack()
    entry_a = tk.Entry(ventana_operadores)
    entry_a.pack()

    tk.Label(ventana_operadores, text="Valor de b:").pack()
    entry_b = tk.Entry(ventana_operadores)
    entry_b.pack()

    tk.Label(ventana_operadores, text="Valor de c:").pack()
    entry_c = tk.Entry(ventana_operadores)
    entry_c.pack()

    tk.Button(ventana_operadores, text="Resolver", command=lambda: resolver_ecuacion_operadores(entry_a, entry_b, entry_c)).pack()

# Función para mostrar el menú de funciones
def mostrar_menu_funciones():
    ventana_funciones = tk.Toplevel(ventana)
    ventana_funciones.title("Funciones")

    tk.Label(ventana_funciones, text="Seleccione una función:").pack()

    opciones = ['¿Es Vocal?', 'Resolver Ecuación Cuadrática', 'Generar Histograma']

    # Lista desplegable (combobox)
    combo = ttk.Combobox(ventana_funciones, values=opciones)
    combo.pack()

    # Función para manejar la opción seleccionada
    def ejecutar_funcion_seleccionada():
        seleccion = combo.get()

        if seleccion == '¿Es Vocal?':
            ventana_vocal = tk.Toplevel(ventana_funciones)
            ventana_vocal.title("¿Es Vocal?")
            tk.Label(ventana_vocal, text="Ingrese un carácter:").pack()
            entry_caracter = tk.Entry(ventana_vocal)
            entry_caracter.pack()
            tk.Button(ventana_vocal, text="Verificar", command=lambda: es_vocal(entry_caracter)).pack()
        elif seleccion == 'Resolver Ecuación Cuadrática':
            ventana_ecuacion = tk.Toplevel(ventana_funciones)
            ventana_ecuacion.title("Resolver Ecuación Cuadrática")
            tk.Label(ventana_ecuacion, text="Valor de a:").pack()
            entry_a = tk.Entry(ventana_ecuacion)
            entry_a.pack()
            tk.Label(ventana_ecuacion, text="Valor de b:").pack()
            entry_b = tk.Entry(ventana_ecuacion)
            entry_b.pack()
            tk.Label(ventana_ecuacion, text="Valor de c:").pack()
            entry_c = tk.Entry(ventana_ecuacion)
            entry_c.pack()
            tk.Button(ventana_ecuacion, text="Resolver", command=lambda: resolver_ecuacion_funciones(entry_a, entry_b, entry_c)).pack()
        elif seleccion == 'Generar Histograma':
            generar_histograma()

    # Botón para ejecutar la opción seleccionada
    tk.Button(ventana_funciones, text="Ejecutar", command=ejecutar_funcion_seleccionada).pack()

# Función para mostrar el menú de cadenas con las opciones
def mostrar_menu_cadenas():
    ventana_cadenas = tk.Toplevel(ventana)
    ventana_cadenas.title("Funciones de Cadenas")

    tk.Label(ventana_cadenas, text="Seleccione una función de cadenas:").pack()

    opciones = [
        'replace', 'find', 'count', 'capitalize', 'title',
        'rstrip', 'index', 'casefold', 'Dividir y manipular cadenas', 'Obtener mes de la fecha'
    ]

    combo = ttk.Combobox(ventana_cadenas, values=opciones)
    combo.pack()

    # Función para ejecutar según la opción seleccionada
    def ejecutar_funcion_cadenas():
        seleccion = combo.get()

        if seleccion == 'replace':
            ejemplo_replace()
        elif seleccion == 'find':
            ejemplo_find()
        elif seleccion == 'count':
            ejemplo_count()
        elif seleccion == 'capitalize':
            ejemplo_capitalize()
        elif seleccion == 'title':
            ejemplo_title()
        elif seleccion == 'rstrip':
            ejemplo_rstrip()
        elif seleccion == 'index':
            ejemplo_index()
        elif seleccion == 'casefold':
            ejemplo_casefold()
        elif seleccion == 'Dividir y manipular cadenas':
            ejemplo_manipulacion_cadenas()
        elif seleccion == 'Obtener mes de la fecha':
            ejemplo_fecha()

    tk.Button(ventana_cadenas, text="Ejecutar", command=ejecutar_funcion_cadenas).pack()

# Función para mostrar el menú de listas
def mostrar_menu_listas():
    ventana_listas = tk.Toplevel(ventana)
    ventana_listas.title("Funciones de Listas")

    tk.Label(ventana_listas, text="Seleccione una opción:").pack()

    opciones = ['Mostrar Empleados', 'Verificar Duplicados', 'Eliminar Duplicados']

    combo = ttk.Combobox(ventana_listas, values=opciones)
    combo.pack()

    # Función para manejar la opción seleccionada
    def ejecutar_opcion_lista():
        seleccion = combo.get()
        if seleccion == 'Mostrar Empleados':
            nombres = ["Juan", "Ana", "Luis"]
            edades = [25, 30, 35]
            peso = [70, 60, 80]
            mostrar_empleados(nombres, edades, peso)
        elif seleccion == 'Verificar Duplicados':
            lista = [1, 2, 3, 4, 5, 1, 2]
            resultado = tiene_duplicados(lista)
            messagebox.showinfo("Verificar Duplicados", f"¿Tiene duplicados?: {resultado}")
        elif seleccion == 'Eliminar Duplicados':
            lista = [1, 2, 3, 4, 5, 1, 2]
            resultado = eliminar_duplicados(lista)
            messagebox.showinfo("Eliminar Duplicados", f"Lista sin duplicados: {resultado}")

    tk.Button(ventana_listas, text="Ejecutar", command=ejecutar_opcion_lista).pack()

# Función para mostrar el menú de conjuntos
def mostrar_menu_conjuntos():
    ventana_conjuntos = tk.Toplevel(ventana)
    ventana_conjuntos.title("Funciones de Conjuntos")

    tk.Label(ventana_conjuntos, text="Seleccione una función de conjuntos:").pack()

    # Opciones para conjuntos
    opciones = [
        'intersection_update()', 'isdisjoint()', 'issubset()', 'issuperset()', 'pop()',
        'symmetric_difference_update()', 'union()', 'update()', 'remove()', 'symmetric_difference()'
    ]

    combo = ttk.Combobox(ventana_conjuntos, values=opciones)
    combo.pack()

    # Función para manejar la opción seleccionada
    def ejecutar_funcion_conjunto():
        seleccion = combo.get()

        conjunto1 = {1, 2, 3, 4, 5}
        conjunto2 = {4, 5, 6, 7, 8}

        # Llamar a la función correcta dependiendo de la selección
        if seleccion == 'intersection_update()':
            resultado = intersection_update(conjunto1, conjunto2)
        elif seleccion == 'isdisjoint()':
            resultado = isdisjoint(conjunto1, conjunto2)
        elif seleccion == 'issubset()':
            resultado = issubset(conjunto1, conjunto2)
        elif seleccion == 'issuperset()':
            resultado = issuperset(conjunto1, conjunto2)
        elif seleccion == 'pop()':
            resultado = pop_element(conjunto1)
        elif seleccion == 'symmetric_difference_update()':
            resultado = symmetric_difference_update(conjunto1, conjunto2)
        elif seleccion == 'union()':
            resultado = union(conjunto1, conjunto2)
        elif seleccion == 'update()':
            resultado = update(conjunto1, conjunto2)
        elif seleccion == 'remove()':
            resultado = remove(conjunto1, 4)
        elif seleccion == 'symmetric_difference()':
            resultado = symmetric_difference(conjunto1, conjunto2)

        messagebox.showinfo("Resultado", resultado)

    # Botón para ejecutar la función seleccionada
    tk.Button(ventana_conjuntos, text="Ejecutar", command=ejecutar_funcion_conjunto).pack()

# Función para mostrar el menú de diccionarios
def mostrar_menu_diccionarios():
    ventana_diccionarios = tk.Toplevel(ventana)
    ventana_diccionarios.title("Funciones de Diccionarios")

    tk.Label(ventana_diccionarios, text="Seleccione una función:").pack()

    opciones = [
        'Agrupar palabras por inicial',
        'Contar vocales y consonantes',
        'Convertir cadena de clientes a diccionario'
    ]

    # Lista desplegable (combobox)
    combo = ttk.Combobox(ventana_diccionarios, values=opciones)
    combo.pack()

    # Entrada para la cadena (inicialmente oculta)
    tk.Label(ventana_diccionarios, text="Ingrese una cadena:", name="label_cadena").pack()
    entrada_cadena = tk.Entry(ventana_diccionarios, name="entrada_cadena")
    entrada_cadena.pack()

    # Ocultar la entrada de cadena por defecto
    ventana_diccionarios.children["label_cadena"].pack_forget()
    ventana_diccionarios.children["entrada_cadena"].pack_forget()

    # Función para manejar la opción seleccionada
    def mostrar_entrada_cadena(*args):
        seleccion = combo.get()

        if seleccion == 'Contar vocales y consonantes':
            ventana_diccionarios.children["label_cadena"].pack()
            ventana_diccionarios.children["entrada_cadena"].pack()
        else:
            ventana_diccionarios.children["label_cadena"].pack_forget()
            ventana_diccionarios.children["entrada_cadena"].pack_forget()

    # Función para ejecutar la opción seleccionada
    def ejecutar_funcion_diccionarios():
        seleccion = combo.get()
        cadena = entrada_cadena.get()

        if seleccion == 'Agrupar palabras por inicial':
            agrupar_por_inicial()
        elif seleccion == 'Contar vocales y consonantes':
            contar_vocales_consonantes_diccionario(cadena)
        elif seleccion == 'Convertir cadena de clientes a diccionario':
            convertir_cadena_a_diccionario()

    combo.bind("<<ComboboxSelected>>", mostrar_entrada_cadena)

    tk.Button(ventana_diccionarios, text="Ejecutar", command=ejecutar_funcion_diccionarios).pack()

# Ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal")

style = ttk.Style()
style.configure("Neon.TButton",
                borderwidth=2,
                relief="flat",
                padding=10,
                background="#282c34",  
                foreground="#61afef", 
                font=("Helvetica", 12, "bold"))

style.map("Neon.TButton",
          background=[("active", "#61afef")],  
          foreground=[("active", "#282c34")])  

# Botones 
for i in range(7):
    if i == 0:
        ttk.Button(ventana, text=f"Botón {i + 1}: Notas", style="Neon.TButton", command=mostrar_menu_notas).pack(pady=10)
    elif i == 1:
        ttk.Button(ventana, text=f"Botón {i + 1}: Operadores", style="Neon.TButton", command=mostrar_menu_operadores).pack(pady=10)
    elif i == 2:
        ttk.Button(ventana, text=f"Botón {i + 1}: Funciones", style="Neon.TButton", command=mostrar_menu_funciones).pack(pady=10)
    elif i == 3:
        ttk.Button(ventana, text=f"Botón {i + 1}: Cadenas", style="Neon.TButton", command=mostrar_menu_cadenas).pack(pady=10)
    elif i == 4:
        ttk.Button(ventana, text=f"Botón {i + 1}: Listas", style="Neon.TButton", command=mostrar_menu_listas).pack(pady=10)
    elif i == 5:
        ttk.Button(ventana, text=f"Botón {i + 1}: Conjuntos", style="Neon.TButton", command=mostrar_menu_conjuntos).pack(pady=10)
    elif i == 6:
        ttk.Button(ventana, text=f"Botón {i + 1}: Diccionarios", style="Neon.TButton", command=mostrar_menu_diccionarios).pack(pady=10)
    else:
        ttk.Button(ventana, text=f"Botón {i + 1}", style="Neon.TButton").pack(pady=10)

ventana.geometry("300x500")
ventana.configure(bg="#21252b")  

ventana.mainloop()