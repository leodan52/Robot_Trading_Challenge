# Robot_Trading_Challenge

Este proyecto es mi solución al 1er Challenge del BootCamp en Data Science ofrecido por [Alura Latam](https://www.aluracursos.com/). El objetivo de este primer reto es poner a prueba los conocimientos obtenidos en el primer módulo, qué consisten en la obtención y tratamiento de datos.

*Robot Trading* obtiene y trata el costo histórico del valor del Bitcoin (BTC) en dólares estadounidenses (USD), así como el valor actual y su tendencia —a la baja o a la alta— de la última hora. Los datos se muestran en un gráfico, acompañado del costo promedio, además de tomar decisiones de los posibles movimientos a realizar —compra, venta o mantener.

## Requerimientos

El proyecto se realizó usando los siguientes módulos de [Python](https://www.python.org/):

* [Pandas](https://pandas.pydata.org/) >= 1.4.3
* [Matplotlib](https://matplotlib.org/) >= 3.7.1
* [Seaborn](https://seaborn.pydata.org/) >= 0.12.2
* [yfinance](https://pypi.org/project/yfinance/) >= 0.2.31
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) >= 4.12.2
* [requests](https://pypi.org/project/requests/) >= 2.31.0
* [PyQt5](https://pypi.org/project/PyQt5/) >= 5.14.1

Python se trabajó en la versión 3.8.10, y solo fue probado para OS Linux.

## Desglose del proyecto

El reto consiste de 5 pasos, cada una encargada de realizar una tarea referente a los datos, creando una serie de funciones:

1. `importar_base_bitcoin()`: Para extraer el historial de los precios del Bitcoin (BTC-USD) de los últimos 7 días en intervalos de 5 minutos, usando `yfinance`.
2. `extraer_tendencias()`: Para extraer el precio actual y la tendencia del Bitcoin usando Web Scraping del sitio https://coinmarketcap.com/.
3. `limpieza_datos()`: Para el tratamiento de valores nulos y ceros donde no sean necesarios.
4. `tomar_decisiones()`: Para analizar los datos y decidir si vender, comprar o mantener.
5. `visualizacion()`: Para mostrar los datos en una gráfica `lineplot` de `Seaborn`.

En el notebook [Robot_Trading.ipynb](notebook/Robot_Trading.ipynb) se muestra la solución tal como se pedía el Challenge. Sin embargo, se decidió reestructurar el proyecto usando PyQt5 para ejecutarlo desde escritorio con entorno gráfico; **las funciones anteriores pasaron a ser métodos** de la clase [`RobotTrading`](models/robot.py).

## Challenge completado

Mis más sinceros agradecimientos a [Alura Latam](https://www.aluracursos.com/). Este primer Challenge ha sido aprobado, y como muestra he obtenido la Insignia correspondiente.

![Insignia del 1er Challenge del BootCamp para Data Science por Alura latam](assets/images/challenge_1.png)