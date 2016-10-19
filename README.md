# Prueba de Hanoi

Hanoi es un problema bastante conocido en el mundo de la informática y un referente en muchos libros de texto, debido a su complejidad de 2^n-1 constituyr un reto interesante para un desarrollador

# Instrucciones

Implemente Hannoi para n = 4 mostrando todos los pasos seguidos por el algoritmo, para esto:

* Debe compartir pantalla con el entrevistador
* Cree un fork de este repositorio
* Desarrolle su implementación en el lenguaje seleccionado.
* Haga commit y push cuantas al menos 2 veces durante el tiempo de la entevista
* Imprima casa paso del algoritmo en la pantalla como por ejemplo

    43
    2
    1


# Descripción del problema

El juego, en su forma más tradicional, consiste en tres varillas verticales. En una de las varillas se apila un número indeterminado de discos (elaborados de madera) que determinará la complejidad de la solución, por regla general se consideran ocho discos. Los discos se apilan sobre una varilla en tamaño decreciente. No hay dos discos iguales, y todos ellos están apilados de mayor a menor radio en una de las varillas, quedando las otras dos varillas vacantes. El juego consiste en pasar todos los discos de la varilla ocupada (es decir la que posee la torre) a una de las otras varillas vacantes. Para realizar este objetivo, es necesario seguir tres simples reglas:

* Sólo se puede mover un disco cada vez.
* Un disco de mayor tamaño no puede descansar sobre uno más pequeño que él mismo.
* Sólo puedes desplazar el disco que se encuentre arriba en cada varilla.