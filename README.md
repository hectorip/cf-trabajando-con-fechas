# Trabajando con fechas

Trabajar con representaciones de fechas y horas es algo que todos los desarrolladores vamos a tener que hacer por lo menos una vez en un nuestra vida.

Sin embargo, hacerlo bien es algo difícil, necesitamos el conocimiento básico.

En este repositorio tienes ejemplos de cómo trabajar con fechas en Python. Entenderás los conceptos básicos para aplicarlos en tus proyectos, pero también podrás aplicar ese conocimiento a otros lenguajes, ya que los principios son los mismos.

## Representación de información

Representar información es una de las tareas fundamentales de todos los desarrolladores de software.

¿Pero qué es?

Es convertir un dato del mundo real a un dato que pueda ser interpretado pero sobre todo almacenado por una computadora.

Pongamos como ejemplo los números enteros.

Cuando pones un `5` estas representando un número entero, que es un concepto de cantidad, pero que la computadora almacena como un conjunto de bits.

Pero el concepto del número 5 puede ser representado de múltiples maneras que ni siquiera tenemos en cuenta muchas veces:

- `5`
- `V`
- `cinco`
- `five`
- `101`
- `0b101`
- `0x5`
- `0o5`
- `|||||`
- `⚄`
- `🖐`

Todos los tipos de datos que conocemos, son guías para **representaciones de información**.

El tipo de dato que mejor sirve para representar
fechas y horas es el tipo de dato `datetime`.


## Referencias

Bibliotecas de la biblioteca estándar de Python:

- [Documentación oficial de Python](https://docs.python.org/3/library/datetime.html)
- [Documentación de time](https://docs.python.org/3/library/time.html)
- [Documentación de ZoneInfo](https://docs.python.org/3/library/zoneinfo.html)

## Librerías de terceros

- [Documentación oficial de Arrow](https://arrow.readthedocs.io/en/latest/)
- [Documentación oficial de Pendulum](https://pendulum.eustace.io/docs/)

## Otros recursos

- [Documentación de ISO 8601 - Datetime](https://es.wikipedia.org/wiki/ISO_8601)
- [Documentación de RFC 3339 - Timestamps](https://tools.ietf.org/html/rfc3339)
- [Falsehoods programmers believe about time](https://gist.github.com/timvisee/fcda9bbdff88d45cc9061606b4b923ca)

## Licencia

MIT
