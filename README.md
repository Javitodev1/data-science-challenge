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