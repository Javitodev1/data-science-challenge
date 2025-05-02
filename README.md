## Objetivos

- Predecir la demanda diaria de productos en las tiendas utilizando datos históricos de ventas e inventario. ¿Es posible crear un modelo de pronóstico basado en LSTM que supere a métodos clásicos como ARIMA?

- Optimice los niveles de inventario analizando las tendencias de ventas y minimizando los desabastecimientos a la vez que reduce las situaciones de sobrestock.

- Desarrollar una estrategia de precios basada en la demanda, los precios de la competencia y los descuentos para maximizar los ingresos.

- Desarrollar una aplicación que integre las soluciones de los desafios en un entorno que simulande el inventario de un retail

- Trabajar en un entorno colaborativo de modo que la aplicación se ejecute en un entorno de producción.

## Project Structure

- core: interfaces y estructura de datos

- db: modelos, controladores y conectores a la base de datos.

- config: configuración inicial de las tablas de la base de datos.

- data: dataset y población inicial de registros en la base de datos.

- doc: archivos de Júpyter documentando los algoritmo de procesamiento de datos y algoritmos para el entrenamiento de modelos LSTM.

- proc: algoritmos de análisis y procesamiento de datos para la generación de reportes y la toma de decisiones.

- lstm: modelos LSTM y objetos para su uso.

- view: archivos de configuración para los reportes en Power BI.

- test: pruebas automatizadas.

- logging: logging service

- app: integra el resto de módulos para crear la aplicación que solucionará los desafíos del dataset.

- model: modelos con información de la app y eventos.

- controller: controladores para el manejo de eventos y lógica de la app.


## Ramas de git

- Prod: Rama de Producción. Paralela a la rama Master nunca hace merge a esta. Cuando nuevo código es integrado en la rama Master, crea una pull request para desplegar el nuevo código en el servidor. Crea el entorno de producción. (requirements-prod.txt)

- Dev: Rama de Desarrollo o trabajo local. Integra codigo nuevo a la rama Master. Crea el entorno de desarrollo.(requirements.txt)

- Master: Rama que se visualizará en Github por defecto.

- Features: ramas individuales teniendo como origen la rama Dev para la integración de código al proyecto.

## Requisitos

- Python3 [Descargar](https://www.python.org/downloads/)
- Docker Engine [Descargar](https://www.docker.com/products/docker-desktop/)

## Dependencias de python3

- jupyter
- numpy
- matplotlib
- pytest
- seaborn
- scikit-learn
- sqlalchemy
- ruff

## Configuración del entorno de desarrollo

Primero clonamos el repositorio

`git clone https://github.com/Javitodev1/data-science-challenge.git`

Luego entramos a la carpeta del proyecto

`cd data-science-challenge`

Luego debemos crear el entorno virtual en python donde instalaremos las dependencias

`python3 -m venv venv`

Luego debemos activar el nuevo entorno virtual

`source ./venv/bin/activate`

Una vez activado el entorno virtual, instalaremos las dependencias

`pip3 install -r requirements.txt`

Finalmente descargamos las imagenes del servidor SQL, recuerden ejecutar este comando con permisos de administrador

`docker compose -f ./sql/docker-compose.yml pull`

## Windows

cambiar policies

`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

activar venv

`.\venv\Scripts\Activate.ps1`


## Ejecución del entorno de desarrollo

para ejecutar el proyecto utilizaremos el script dev.py que se encargara de levantar el servidor SQL, correr las pruebas unitarias y ejecutar la aplicacion en modo desarrollo.

`python3 dev.py`
