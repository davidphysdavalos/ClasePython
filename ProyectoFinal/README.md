Proyecto Final
=================

Bitacora:

-Se trado de calcular la funcion zeta de riemann directo de las definiciones obteniendo resultados negativos.

-Se construyeron clases para intervalos complejos en coordenadas cartesianas y polares.

-Se construyo el metodo de newton compatible con estas clases.

Notas: Se presenta un funcionamiento extraño del metodo de Newton en coordenadas
polares, por lo cual se estan perfeccionando los intervalos en coordenadas cartesianas, sin embargo ahora se señala que el error puede estar en iterator

-Intervalos cartesianos ahora tienen un mejor funcionamiento, sin embargo se observa que cuando no se da un intervalo
simetrico en los reales, el metodo de Newton no colapsa el intervalo.

-Ademas los intervalos no colapsan cuando se tienen funciones con muchas raices, sera cosa de generalizar Newton.


Cosas para hacer el dia 5-7 de noviembre de 2013 --Intervalos en polares--:

-modificar la funcion contains de cpintervalo--- Hecho.

-Perfeccionar la rutina NewtonOperator e iterator, asi como corregir el error en el notebook-- Se corrigio el error, solo falta hacer compatible todo para raices en la parte inferior del plano complejo.

-Ademas seria bueno tratar de implementar correctamente la division entre cero, es decir, en lugar de que mande un hull que sea una union
y se realicen operaciones por separado.--- Sigue en pie la pregunta si esto realmente afecta.

-Corregir el problema de los radios negativos.

Cosas para hacer el dia 11-13 de noviembre de 2013 --Intervalos en cartesianas--:

-Implementar pow en intervalos cartesianos, me ha dado weba.



