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

## Tareas

1. Crear un programa que defina la función llamada `stats(arr)` la cual recibe el arreglo (o tupla) `arr` y devuelve una tupla `(min, max, sum, prom, sum2, desv)` con el valor mínimo, máximo, la suma de los valores, el promedio de estos, la suma de cuadrados y la desviación estándar `desv² = ∑(xi - ẋ)` donde `ẋ` es el promedio. Puede basarse en el programa [min_max.py](https://github.com/badillosoft/python-master/blob/master/sesion_2/min_max.py) de la sesión 2
2. Crear un programa que solicite el número de puntos a ingresar, luego para cada punto guardar en un arreglo la tupla `(x, y)` donde `x` es el i-ésimo punto en su coordenada `x` y `y` en su coordenada `y` (también deben ingresarse), intente utilizar `line = raw_input("Ingresa X y Y separados por ',', ejemplo '1, 2': ")` luego `aux = line.split(",")`, finalmente `x = float(aux[0])` y `y = aux[1]`, sino solicite cada valor por separado `x = float(raw_input("ingresa X: "))`. Cada punto se guardará en el arreglo llamado `points` inicialmente vacío `points = []`. Una vez que tenga los puntos complete el siguiente programa:
> __python__ - fast_interpol.py

~~~py
points = []

# COMPLETAR LECTURA DE poits
# N = int(raw_input("Ingresa el numero de puntos: "))
# for i in range(0, N):
#   # ... LEER x, y
#   points.append((x, y))

def lin(x0, y0, x1, y1, x):
    return y0 + float(y1 - y0) / (x1 - x0) * (x - x0)

def interpol(P, x):
    n = len(P)
    for k in range(0, n - 1):
        x0, y0 = P[k]
        x1, y1 = P[k + 1]
        if x < x1:
            return lin(x0, y0, x1, y1, x)
    return lin(x0, y0, x1, y1, x)

def x_bounds(points):
  min = points[0][0]
  max = points[0][0]
  for x, y in points:
    if min < x:
      min = x
    elif max > x:
      max = x
  return (int(min) - 1, int(max) + 1)
  
x_min, x_max = x_bounds(points)

for x in range(x_min, x_max):
    print x, interpol(points, x)

~~~

## Sesión 1

* __Tipos de datos__: _python_ soporta los siguientes tipos de datos: `números`, `cadenas`, `booleanos`. Los números se dividen en los tipos `int` y `float` para almacenar _enteros_ y _decimales_ respectivamente. Debemos recordar que si dividimos dos enteros la división también será entera, ejemplo, `a = 7 / 2 # a = 3` si sabemos que ambos números son enteros entonces tenemos que hacer una _conversión_ (_cast_) de entero a decimal para forzar a que la división sea decimal, ejemplo `a = 7.0 / 2 # a = 3.5`, sin embargo, supongamos que tenemos dos números enteros `a = 7` y `b = 2`, entonces no es tan fácil como poner un `.0`, ejemplo `c = a / b # c = 3`, `c = a.0 / b # ERROR` lo que necesitamos hacer es convertir uno o ambos valores a decimales para forzar la división a decimal, ejemplo `c = float(a) / b`, así utilizando la función `float(...)` convierte (si puede) el valor `...` a un número decimal. También puede convertir cadenas, ejemplo `x = float("1.23") # a = 1.23`, si quiere convertir a un número a entero use `int(...)` y si quiere una cadena use `str(...)`. Las cadenas pueden definirse por comilla simple o doble indistintamente, ejemplo `s = 'Hola' # s = 'Hola'` o `s = "Hola" # s = 'Hola'`. Para saber que tipo de dato es una variable usamos la función `type(...)`, ejemplo `print type(a)`.
* __Variables__: las variables son cajas que ocupan un lugar en la memoria donde podemos guardar datos sobre alguno de los tipos de datos soportados por _python_. Para crear o modificar una variable basta asignarla mediante un nombre, ejemplo `mi_variable = valor`. Si la `mi_variable` no existe la crea y si ya existe la reemplaza. para recuperar el valor de una variable simplemente colocamos su nombre, ejemplo `print mi_variable`. Los nombres de variables válidos son todas las combinaciones de letras mayúsculas y minúsculas, guiones bajos `_` y números, pero no pueden empezar por un número (creerá que es un número), ni tampoco tener nombres especiales (`for`, `if`, `in`, `def`, `import`, `self`, entre otros).
* __Leer variables desde el teclado__: podemos llamar al método `raw_input(...)` para capturar una cadena de texto leída desde la entrada estándar (usualmente el teclado y la terminal). El método toma como parámetro una cadena que le mostrará al usuario para saber que está esperando el programa que ingrese, ejemplo `nombre = raw_input("Ingresa tu nombre:")`, en la salida estándar (usualmente la terminal) se muestra el mensaje y el cursor se queda en espera que el usuario escriba algo. Cuando el usuario escribe una cadena y pulsa `enter` entonces la cadena es devuelta por el método y en este caso asignada a la variable `nombre`. Si queremos leer un número usamos los métodos de conversión para transformar la cadena al número, ya sea entero o decimal, ejemplo `edad = int(raw_input("Ingresa tu edad:"))` o `estatura = float(raw_input("Ingresa tu altura:"))`.
* __Bloques__: _python_ interpreta las líneas continuas con la misma identación como un bloque, ejemplo

~~~py
1. ...
2. ...
3. A:
4.    ...
5.    ...
6. ...
7. ...
8. B:
9.    ...
10.   ...
11.   ...
12. ...
~~~

> En el ejemplo anterior vemos que las líneas `1, 2, 3, 6, 7, 8, 12` pertenecen al bloque de instrucciones principal, las líneas `4, 5` pertenecen al bloque de `A` y las líneas `9, 10, 11` pertenecen al bloque de `B`.

* __Control de flujo__: se podría pensar que _python_ lee línea a línea cada instrucción y la evalua, sin embargo, podemos cambiar la dirección del flujo mediante las estructuras de control de flujo que son principalmente las `condicionales` y los `ciclos`.
* __Condicional IF__: una condición es un valos booleano que puede ser verdadero `True` o falso `False`, una condicional evalua la condición y determina si ejecuta o no un bloque de instrucciones en base al resultado de la condición (si es verdadero), la condicional propuesta en _python_ es la sentencia `if` la cual evalua si la condición es verdadera y ejecuta su bloque anidado, ejemplo

~~~py
a = 10
if a < 100:
  print "El numero es menor estricto que 100"
print "Adios"
~~~

> El código anterior imprime el mensaje `El numero es menor estricto que 100` sólo cuando el valor de la variable `a` no es mayor o igual que `100`, intente cambiar el valor a `120` y analice los resultados.

Opcionalmente se puede ejecutar un bloque cuando no se cumple la condición, esto se hace mediante la sentencia `else` que sigifica `sino, entonces ...`, ejemplo

~~~py
edad = int(raw_input("Ingresa tu edad:"))
if edad >= 18:
  print "Ya eres mayor de edad, puedes votar :)"
else:
  print "Eres menor de edad, no entras al bar :'("
print "Adios"
~~~

> Si el número ingresado por el usuario es mayor o igual a `18` entonces se mostrará el mensaje `Ya eres mayor de edad, puedes votar :)`, sino se mostrará el mensaje `Eres menor de edad, no entras al bar :'(`. Observe que el mensaje `Adios` siempre se muestra ya pertenece al bloque principal de ejecución.

Opcionalmente además del bloque `else` se pueden anidar indeterminadamente subcondiciones `elif` las cuales se evaluarán sólo si la anterior no se cumple, ejemplo

~~~py
edad = int(raw_input("Ingresa tu edad:"))
if edad < 4:
  print "Eres un bebe -_-"
elif edad < 12:
  print "Eres un bambino XD"
elif edad < 18:
  print "Eres un adolescente :/"
elif edad < 30:
  print "Eres un joven :O"
elif edad < 60:
  print "Eres un adulto :)"
else:
  print "Seguiras siendo adulto ;)"
print "Adios"
~~~

> También podemos crear condiciones complejas usando los operadores `and`, `or` y `not`, ejemplo `edad >= 18 and sexo == 'Mujer'`, `dia == "Lunes" or mes == 'marzo'`, `not dia in ["Lunes", "Jueves"]`, `a > 3 and (b < 6 or c >= 8)`. Observe que el operador `==` determina si dos elementos son iguales, no lo confunda con el operador de asignación `=`.

* __Ciclo FOR-IN__: un ciclo nos permite repetir un conjunto de instrucciones, ya sea mediante una condición que se cumpla o iterando un arreglo. La sentencia `for-in` nos permite repetir un bloque utilizando una variable que almacena el valor iterado (el valor recorrido) en un arreglo, ejemplo `for x in [1, 2, 3]: print x` imprimirá la variable `x` para cada elemento en el arreglo, es decir, que _python_ tomará cada elemento del arreglo y lo irá guardando en la variable `x`, luego ejecutará el bloque anidado, ejemplo

~~~py
s = 0
for x in [1, 3, 5, 7, 9]:
  s = s + x
print "La suma de 1, 3, 5, 7, 9 es:", s
~~~

> Observe que la sentencia `print` está fuera del bloque, por lo que se ejecutará hasta que se rompa el ciclo (hasta que se hayan iterado/recorrido todos los elementos del arreglo), en cada iteración, la variable `s` reemplazará su valor por el que ya tenía más el iterado `x`, a este proceso se le conoce como acumulación. Finalmente se imprimirá la lenyenda entre comillas y el valor de `s`.

Cuando en un `print` ponemos varios valores separados por comas, los imprimirá en la misma línea y cada valor lo convertirá a una cadena. Cada coma representará también un espacio en blanco, ejemplo `print "Hola", "mundo"` imprime `Hola mundo`, `print "Hola:", 5` imprime `Hola: 5`, si nosotros hacemos `print "Hola: " + 5` provocaremos un error ya que estamos intentando sumar una cadena y un número, lo correcto en tal caso sería convertir primero el número a una cadena `print "Hola: " + str(5)` sin embargo este proceso es más artificioso.

La función `range(a, b)` genera un equivalente al arreglo desde el valor `a`, hasta el valor `b - 1`, ambos deben ser enteros, ejemplo `range(0, 3) # [0, 1, 2]`, `range(3, 6) # [3, 4, 5]`, `range(1, 10, 2) # [1, 3, 5, 7, 9]`, `range(1, 9, 2) # [1, 3, 5, 7]`, debemos tener cuidado con el finalizador, ejemplo `Sumar los primeros 100 números naturales`

~~~py
s = 0
for x in range(1, 101):
  s = s + 1
print "La suma los primeros 100 numeros naturales (1, 2, 3, ...., 100) es", s
~~~

## Sesión 2

* __Listas__: las listas son conjuntos de datos que pueden ser accedidos por un solo nombre de variable y nos permiten guardar arreglos de datos. Las listas se dividen en _Tuplas_ y _Arreglos_.
* __Tuplas__: las tuplas son arreglos fijos de datos, similar a los arreglos con la diferencia que son de dimensión fija, es decir, no podemos agregar o eliminar elementos, sin embargo, si podemos modificar sus valores mediante su índice. Para declarar una tupla usaremos los paréntesis `()` y dentro de ellos los valores, ejemplo `a = (1, 2, "Hola mundo")`. Para recuperar o modificar un valor lo haremos mediante su índice comenzando en 0, ejemplo `a[0] = 3 # a := (3, 2, "Hola mundo")`. Las tuplas son de gran utilidad para devolver datos agrupados como retorno de una función, ejemplo `def ans_next(n): return (n - 1, n + 1)` o `def swap(a, b): return (b, a)`. Las tuplas poseen una sintaxis de _empaquetado/desempaquetado_ el cual es útil para asignarle variables a una tupla, ejemplo `(x, y) = (1, 2)` de esta forma se asignará `x = 1` y `y = 2`, esto se puede utilizar para desempaquetar los datos provenientes de una tupla devuelta por una función, ejemplo `(i, j) = ans_next(10)`, así `i = 9` y `j = 11`. Las tuplas son iterables por lo que podemos iterar sus valores mediante `for-in`, ejemplo `for x in (1, 2, 3): ...`.
* __Arreglos__: los arreglos son valores ordenados guardados en una variable similar a la tupla, con la diferencia que podemos seguir añadiendo o quitando valores y además podemos realizar algunas operaciones entre ellas. Para declarar un arreglo literal lo podemos hacer mediante los corchetes `[]`, ejemplo `a = [1, 2, "Hola mundo"]`, el método `append` nos permite añadir un elemento al final del arreglo, ejemplo `a.append(4) # a := [1, 2, "Hola mundo", 4]`. El método `pop` nos permite eliminar el último elemento del arreglo y lo devuelve, ejemplo `b = a.pop() # b := 4, a := [1, 2, "Hola mundo"]`, también podemos eliminar el índice deseado mediante `pop(i)`, ejemplo `b = a.pop(1) # b := 2, a := [1, "Hola mundo"]`, `a.pop(-1) # a := [1]`. Otros métodos que se pueden aplicar a los arreglos los puede consultar en https://docs.python.org/2/library/array.html. Finalmente podemos sumar `a = [1, 2] + [3 + 4] # a := [1, 2, 3, 4]` y multiplicar (replicar) `a = [1, 2, 3] * 2 # a := [1, 2, 3, 1, 2, 3]`. La dimensión (longitud) de un arreglo se obtiene usando `len`, ejemplo `l = len(a) # l := 6`.
* __Matrices__: python no soporta matrices nativas ni sus operaciones, pero podemos considerar una matriz como un arreglo de arreglos, ejemplo `A = [[1, 2, 3], [4, 5, 6]]` representaría una matriz de 2 filas (2 vectores) y cada fila de 3 columnas. Para acceder a la posición específica hacemos `A[i][j]`, observando que `A[i]` devuelve el i-ésimo arreglo de la matriz, es decir toda la fila i (el arreglo/vector asociado a la fila i), ejemplo `vec = A[1] # vec := [4, 5, 6]`, `a12 = A[1][2] # a12 := 5 (vec[2])`.
* __Módulos__: los módulos pueden considerarse como _bibliotecas_ de variables y funciones que pueden ser reutilizados en otro programa para no reescribir esa funcionalidad, en python todos los archivos `.py` pueden ser utilizados como módulos. Existen varias formas de incluir un módulo en nuestro programa: `import archivo` importa el archivo `archivo.py` (ubicado en el mismo directorio o en las librerías estándares) y toda variable y función puede ser utilizada mediante el nombre del módulo `.` (periodo) y el nombre de la variable o función, ejemplo `import archivo; print archivo.a, archivo.foo("Hola")` suponiendo que existe `archivo.py` que define a la variable `a` y al método `foo(s)`. También podemos importar un módulo y asignarle un _alias_ lo cual permite trabar el módulo de forma más compacta, ejemplo `import archivo as ar; print ar.a, ar.foo(":O")`, observe que ahora nos referimos al módulo mediante su alias `archivo` pasa a ser `ar`. La tercera forma es incluir sólo algunos elementos del módulo en nuestro programa, esto nos permite utilizar las variables y métodos como si los hubieramos definido en nuestro programa, ejemplo `from archivo import a, foo; print a, foo(";)")`, observe que utilizamos la variable `a` y al método `foo` como sin usar el nombre del módulo, como si estuvieran declarados ahí mismo. La última forma es incluir todas las definiciones, la diferencia con antes es que podemos utilizar todos los mátodos y variables como si estuvieran declarados en nuestro archivo, pero debemos tener cuidado al asignar nombres de variables o métodos ya que invalidaremos los ya cargados, ejemplo `from math import *; print cos(3.1416)`. Al importar un módulo python evaluará el módulo, por lo que instrucciones como `print` y demás serán ejecutadas igualmente, para evitar esto podemos colocar todo lo que no queramos que ejecute en un `if __name__ == "__main__": ...` esto hará que python sólo ejecute lo que está en el `if` cuando se manda a ejecutar mediante `python archiv.py`, pero que no lo ejecute cuando se importa `import archivo` o su variante de importación.


