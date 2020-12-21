# Actividad Bonus - regex con `pyrematch`

El archivo `test-correccion.py` incluye los *tests* que se utilizaron para la corrección automática de la Actividad Bonus. Estos *tests* se obtienen de las páginas:

```
TEXTOS_WIKIPEDIA = ["Chile", "Argentina", "Peru", "Brazil",
                    "Colombia", "United States", "France", "China"]
```

Para cada consulta, se evalúa su resultado con cada uno de estos sitios. Si todos los *tests* coinciden con la solución esperada, se otorga **1pto** en la consulta.
Si el 75% de los *tests* (6 *tests*) coinciden con lo esperado, se otorga **0.5pts**.

Para verificar el puntaje con la batería de *tests*, deben tener en su carpeta su archivo `consultas.py`,
y los archivos entregados `test-correccion.py`, `solucion.py`, `solution_dump.txt`, y ejecutar:

```
python test-correccion.py
```

Este les entregará el puntaje de acuerdo a la verificación automática de los resultados.

Adicionalmente se verificaron las siguientes restricciones respecto del uso de la biblioteca `pyrematch`:

* El objetivo de utilizar *regex* es que el patrón indicado permita capturar **TODAS** las coincidencias (*match*) presentes.
* Una implementación se considera correcta si es que se usa **UNA** *regex* para obtener las respuestas, y luego iterar sobre los resultados para pasarlos a tuplas o eventualmente modificar su formato.
* Las soluciones que manipulan las coincidencias detectadas por la *regex* para descartar algunas coincidencia o realizar ajustes de índices o *matches*, 
que sean atribuibles a algo que se podía obtener a partir de una *regex* más completa, se consideran como soluciones incorrectas.

Esto significa que el puntaje asignado puede no coincidir con lo obtenido al ejecutar `test-correccion.py`, en caso que la solución no cumpla con las restricciones anteriores.
En caso que estén seguros que esto se debe a un error, les pedimos que lo indiquen durante la sesión de recorrección.
