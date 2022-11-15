___
## CE. A: 

Debéis comparar los tres ejercicios con otros lenguajes de programación, debéis explicar las características principales de cada uno, y compararlo con al menos 2 lenguajes de programación diferentes al usado en la actividad. 



  

## Python/PHP: 

En este ejercicio podemos ver que en Python se le pueden meter los números mediante un input en el propio código mientras que en PHP sería necesario un HTML el cual este vinculado al archivo PHP, el cual sea el que le de los números introducidos en él. Tampoco es necesario poner punto y coma al acabar cada sentencia en Python mientras que en PHP si, la indentación es lo que permite a Python saber el que va dentro de un if, for, while y lo que va fuera, en PHP eso se haría abriendo y cerrando llaves, tampoco es necesario poner $ en Python para declarar variables cuando en PHP es imprescindible. 

Ejemplo de PHP: Ej 2.05
~~~
array1=[1,2,3,4];
sum($array1){
suma=0;
foreach($array1 as $num){
  $suma+=$num;
}
print $suma;
}
mult($array1){
    mult=1;
foreach($array1 as $num){
  $mult*=$num;
}
print $mult;
}
~~~
Ejemplo de Python: Ej 2.05
~~~
lista=(1,2,3,4)
def sum(lista):
    suma=0
    for b in lista:
        suma+=b
    print(f"Esta es la suma: {suma}")

def multi(lista):
    multiplicacion = 1
    for b in lista:
        multiplicacion *= b
    print(f"Esta es la multiplicación: {multiplicacion}")


sum(lista)
multi(lista)

~~~

  

## Python/C++: 

El tipado de C++ es estático por lo que cuando una variable es definida no es posible cambiar el tipo más adelante, mientras que en Python es dinámico siendo posible su cambio más adelante, Python es un lenguaje interprete por lo cual el código fuente se traduce al momento de ejecutar el código a su vez C++ tiene que traducir todo el código antes de poder ejecutarlo. C++ utiliza bloques y punto y coma, al contrario que Python, este a su vez no los utiliza 

Ejemplo de C++: 
~~~
namespace Namespace {
    
    public static class Module {
        
        public static object vocal = input("Ponga una palabra: ").ToString();
        
        public static object contar_vocales() {
            var vocalo = vocal.count("o");
            Console.WriteLine("Hay {vocalo} o");
            var vocale = vocal.count("e");
            Console.WriteLine("Hay {vocale} e");
            var vocala = vocal.count("a");
            Console.WriteLine("Hay {vocala} a");
            var vocali = vocal.count("i");
            Console.WriteLine("Hay {vocali} i");
            var vocalu = vocal.count("u");
            Console.WriteLine("Hay {vocalu} u");
        }
        
        static Module() {
            contar_vocales(vocal);
        }
    }
}
~~~

Y este sería el mismo ejercicio en Python
~~~
vocal=str(input("Ponga una palabra: "))
def contar_vocales():
    vocalo = vocal.count("o")
    print(f"Hay {vocalo} o")
    vocale = vocal.count("e")
    print(f"Hay {vocale} e")
    vocala = vocal.count("a")
    print(f"Hay {vocala} a")
    vocali = vocal.count("i")
    print(f"Hay {vocali} i")
    vocalu = vocal.count("u")
    print(f"Hay {vocalu} u")


contar_vocales(vocal)
~~~

## Python/JavaScript: 

Para definir variables en Python no es necesario nada, solo el nombre de la variable, seguido de un igual y el valor, en JavaScript es necesario que se agreguen var o let y un punto y coma al final de la línea. Para tomar un valor ingresado por el usuario solo es necesario poner input() en Python a través de la terminal mientras que en JavaScript es necesario que le salga una ventana en el navegador  

Ejemplo de variable Javascript:
~~~
var nombre = 'Madison'
~~~
Ejemplo de variable Python:
~~~
nombre='madison'
~~~
___
## Ce. B

  
## ● ¿Qué diferencias habría en el desarrollo del programa?  

C es capaz de declarar variables para uso futuro mientras que Python no admite declaraciones de variables vacías, estas tienen que tener ya un valor asignado, como podemos ver en el ejercicio 2.13 si no le pusiéramos valor 0 a la variable mayus el ejercicio no funcionaría 

Cuando ocurre algún error Python es capaz de saber cuál fue ese error ya que compila línea a línea, C en su lugar te dice en el segmento del código donde ocurrió el error, en Python aparecería de la siguiente forma. 

 
Diciéndote el error, la línea en la que esta y el tipo de error que es. 

En Python las listas se pueden hacer de forma muy ágil, en cambio C necesitan hacerse a mano y/o se deben de utilizar librerías para poder usarlas. 

En Python no es necesario el abrir y cerrar llaves para definir las funciones ya que estas van por tabulaciones y tampoco son necesarios los puntos y coma al acabar la línea. 

## ● ¿Qué diferencias existen entre los dos lenguajes?

> C es un lenguaje de programación estructural, mientras que Python es un lenguaje de programación orientado a objetos. 

>C es un lenguaje compilado y Python es un lenguaje interpretado. 

>La ejecución de código es más rápida en C que en Python. 

>Python no admite la funcionalidad de puntero, pero los punteros están disponibles en C. 

>C tiene una biblioteca limitada de funciones integradas, mientras que Python es más extensa. 

>En C, es obligatorio declarar tipos de variables, pero esto no es necesario en Python. 

>C permite la asignación de líneas, mientras que da errores en Python. 

>La sintaxis de Python es más fácil de entender que la de C. 

## ● ¿Para qué tipo de programa puede servir cada lenguaje?  

Python se puede usar de forma general en ámbitos científicos, mientras que C se usa principalmente para aplicaciones relacionadas con hardware y código de bajo nivel. 

## ● ¿Cómo sería el proceso de lectura del código fuente de cada programa? 

Python utiliza una forma de lectura llamada interprete mientras que C utiliza lo que se llama un compilador, estos son los procesos de lectura de cada uno de ellos 

La compilación de C se realiza en varias fases que normalmente son automatizadas y ocultadas por los entornos de desarrollo: 

### Preprocesado:
 ~~~

 Consiste en modificar el código fuente en C según una serie de  instrucciones (denominadas directivas de preprocesado) simplificando de esta forma el trabajo del compilador. Por ejemplo, una de las acciones más importantes es la modificación de las inclusiones (#include) por las declaraciones reales existentes en el archivo indicado. 
 
 ~~~

### Compilación:
 ~~~

 Genera el código objeto a partir del código ya preprocesado. 

 ~~~
### Enlazado:
~~~ 
Une los códigos objeto de los distintos módulos y bibliotecas externas (como las bibliotecas del sistema) con el código objeto generado en el paso anterior para generar el programa ejecutable final. 
~~~

Un intérprete es un programa que directamente ejecuta instrucciones especificadas escrito en un lenguaje de alto nivel lo que significa que hace lo que el programa dice. Procesa el programa poco a poco, alternando la lectura de líneas de código y la realización de cálculos. 

Por lo general, el intérprete de Python viene instalado con el propio lenguaje. 

___
## Ce. C 

**Listas**:  

Las listas son una forma de almacenar varios datos dentro de una variable, los elementos de la lista están ordenados, se pueden cambiar y no tienen que ser valores únicos, estos elementos también están indexados. A continuación explico que significa cada cosa.
~~~
Ordenado:

Esto significa que los elementos tienen un orden definido y ese orden no cambiará. 

Si se agregan nuevos elementos a la lista, estos nuevos elementos se colocarán al final de la lista. 

Cambio:

La lista se puede cambiar, lo que significa que podemos cambiar, agregar y eliminar elementos en una lista después de que se haya creado. 

Indexados:

El primer elemento tiene índice [0], el segundo índice [1], y así sucesivamente 

Valores duplicados:

Dado que las listas están indexadas, las listas pueden tener elementos con el mismo valor. 
~~~
 Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:7, 9, 10, 12, 16
~~~

**Tuplas**:  

Las tuplas son iguales a las listas con la única diferencia de que estas no permiten el cambio una vez creadas, pero conserva las demás características. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:15
~~~

**For**: 

Un bucle for se usa para iterar sobre los distintos tipos de almacén de datos de Python como, por ejemplo, una lista o una tupla. Este bucle se usa más para iterar dentro de estos almacenes, con esto podemos ejecutar un conjunto de codigo una vez por cada elemento del almacén. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:3,5,6,7,9,10,11,12,13,14,15,16
~~~
**For anidado**: 

 Un for anidado es un for realizado dentro de un bucle, permitiendo por ejemplo si lo utilizamos en una lista de palabras ejecutar el conjunto de código a cada letra en vez de a cada palabra entera. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:7,9,13
~~~

**While**: 

Con el bucle While, podemos ejecutar un conjunto de código mientras la condición que le asignemos sea verdadera. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:3
Parte 2:8
~~~
**Funciones**: 

Una función es un bloque de código que solo se ejecuta cuando es llamada, puedes pasarle datos a la función mediante argumentos, la función puede devolver datos como resultado. 

Al declarar la función se ponen unos parámetros, esos parámetros son sustituidos con los valores de los argumentos al llamar a la función. 

 Esto se utiliza en los ejercicios:
~~~
Parte 1:1,2,3
Parte 2:1,2,3,4,5,6,7,8,9,10,11,12,16,17,18
~~~

 

**Variables**: 

Las variables son contenedores que se usan para guardar un valor, estas son creadas en el momento en el que le asignas por primera vez un valo. 

 Esto se utiliza en los ejercicios:
~~~
Parte 1:Todos
Parte 2:Todos
~~~
 

**Indentación:** Es el uso de tabulaciones para poder identificar cuando empieza y cuando acaba un bloque de codigo, indicando tambien el orden de ejecución dentro del mismo bloque.

 Esto se utiliza en los ejercicios:
~~~
Parte 1:Todos
Parte 2:Todos
~~~

**If**: 

La estructura de control if, permite que un programa ejecute unas instrucciones cuando se cumplan una condición. Si esta condición se cumple la estructura manda un TRUE, y si no se cumple manda un FALSE. Aunque esta no es la única forma que tiene ya que también se pueden hacer bifurcaciones con la sentencia if … else … de la siguiente forma que si se cumple la condicion se ejecuta el primer bloque de códigos, si no se cumple se ejecutara el segundo, esto se puede aumentar en escala utilizando elif. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:1,2,3
Parte 2:3,4,7,8,10,11,12,13,15,16,18
~~~
**Input:** 

Esta es la forma que utilizamos para que el usuario nos de los valores que él quiera. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:1,2
Parte 2:1,2,4,13,16,17,18
~~~
 

**Append:** 

Append es un método que tiene toda lista de Python el cual permite agregar un elemento al final de la lista, pero no retorna ningún elemento ni valor. 

Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:13
~~~

**Isupper():**

 Isupper es un método que devuelve verdadero si todos los caracteres estan en mayúscula, si este no es el caso devuelve falso. Este método solo examina los caracteres del alfabeto.

 Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:13
~~~

**Print:** 

Esta función se usa para que python nos muestre texto o variables, para mostrar texto se haria de la siguiente forma. 

Print(“Prueba”) 

Pero si quisiéramos que nos diera el valor de una variable tendríamos que hacerlo de esta otra forma: 

Print(f”{variable_de_prueba}”) 

 Esto se utiliza en los ejercicios:
~~~
Parte 1:Todos
Parte 2:Todos
~~~

**Return:** 

La palabra reservada return indica el final de la función, pero también el valor que devuelve la función. La ejecución del programa continúa tras la llamada a la función.   
Esto se utiliza en los ejercicios:
~~~
Parte 1:N/A
Parte 2:3,8,14
~~~

**Comentarios:** 

Esto se usa para dejar explicaciones en el programa pero sin que este los llegue a interpretar. Esto seria solo para dejar claridad en el programa a la hora de examinarlo. Aunque no los he utilizado, a la hora de hacer programas mas grandes son muy necesarios para no perderte.
Esto se utiliza en los ejercicios:
~~~
Parte 1:Ninguno
Parte 2:Ninguno
:(
~~~
**Enumerate:**

Esta función toma una colleción(tupla, lista) y las transforma en un objeto enumerado. Tambien le añade un contador como la clave del objeto.


~~~
Parte 1:N/A
Parte 2:14
~~~