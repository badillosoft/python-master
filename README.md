# Curso de Python

## Contenido

* Tipos de Datos y Variables
* Sintaxis del Lenguaje y Control de Flujo
* Módulos y Funciones
* Listas, Arreglos y Diccionarios
* Clases y Objetos
* Librerías externas
* Numpy y Scipy
* Generación de Gráficos y Estadísticas

## Enlaces de interés

* __Try Python - Code School__ (https://www.codeschool.com/courses/try-python) - Curso de python gratuito donde puedes practicar y aprender.
* __Sitio oficial de Python__ (https://www.python.org/) - Sitios oficial donde puedes descargar python y usar la terminal interactiva desde el navegador.
* __Visual Studio Code__ (https://code.visualstudio.com/) - Es un entorno de desarrollo ligero con terminal incluida y opciones de debug y soporta más de 60 lenguajes.

## Noticias

* Se concluyó la [Sesión 1](https://github.com/badillosoft/python-master/tree/master/sesion_1) dónde se revisaron los componentes básicos de python.
* Se añadió el libro [Python para todos](https://github.com/badillosoft/python-master/blob/master/recursos/python_para_todos.pdf) en la sescción de recursos.

## Sesión 1

* __Tipos de datos__: _python_ soporta los siguientes tipos de datos: `números`, `cadenas`, `booleanos`. Los números se dividen en los tipos `int` y `float` para almacenar _enteros_ y _decimales_ respectivamente. Debemos recordar que si dividimos dos enteros la división también será entera, ejemplo, `a = 7 / 2 # a = 3` si sabemos que ambos números son enteros entonces tenemos que hacer una _conversión_ (_cast_) de entero a decimal para forzar a que la división sea decimal, ejemplo `a = 7.0 / 2 # a = 3.5`, sin embargo, supongamos que tenemos dos números enteros `a = 7` y `b = 2`, entonces no es tan fácil como poner un `.0`, ejemplo `c = a / b # c = 3`, `c = a.0 / b # ERROR` lo que necesitamos hacer es convertir uno o ambos valores a decimales para forzar la división a decimal, ejemplo `c = float(a) / b`, así utilizando la función `float(...)` convierte (si puede) el valor `...` a un número decimal. También puede convertir cadenas, ejemplo `x = float("1.23") # a = 1.23`, si quiere convertir a un número a entero use `int(...)` y si quiere una cadena use `str(...)`. Las cadenas pueden definirse por comilla simple o doble indistintamente, ejemplo `s = 'Hola' # s = 'Hola'` o `s = "Hola" # s = 'Hola'`. Para saber que tipo de dato es una variable usamos la función `type(...)`, ejemplo `print type(a)`.
* __Variables__: las variables son cajas que ocupan un lugar en la memoria donde podemos guardar datos sobre alguno de los tipos de datos soportados por _python_. Para crear o modificar una variable basta asignarla mediante un nombre, ejemplo `mi_variable = valor`. Si la `mi_variable` no existe la crea y si ya existe la reemplaza. para recuperar el valor de una variable simplemente colocamos su nombre, ejemplo `print mi_variable`. Los nombres de variables válidos son todas las combinaciones de letras mayúsculas y minúsculas, guiones bajos `_` y números, pero no pueden empezar por un número (creerá que es un número), ni tampoco tener nombres especiales (`for`, `if`, `in`, `def`, `import`, `self`, entre otros).
* __Leer variables desde el teclado__: podemos llamar al método `raw_input(...)` para capturar una cadena de texto leída desde la entrada estándar (usualmente el teclado y la terminal). El método toma como parámetro una cadena que le mostrará al usuario para saber que está esperando el programa que ingrese, ejemplo `nombre = raw_input("Ingresa tu nombre:")`, en la salida estándar (usualmente la terminal) se muestra el mensaje y el cursor se queda en espera que el usuario escriba algo. Cuando el usuario escribe una cadena y pulsa `enter` entonces la cadena es devuelta por el método y en este caso asignada a la variable `nombre`. Si queremos leer un número usamos los métodos de conversión para transformar la cadena al número, ya sea entero o decimal, ejemplo `edad = int(raw_input("Ingresa tu edad:"))` o `estatura = float(raw_input("Ingresa tu altura:"))`.
