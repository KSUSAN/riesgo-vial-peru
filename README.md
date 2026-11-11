# riesgo-vial-peru
Proyecto Final Data Engineering - Riesgo Vial Perú
Sistema Analítico de Riesgo Vial del Perú
Descripción
Proyecto de Data Engineering orientado a identificar regiones con mayor riesgo vial mediante el análisis de datos históricos de siniestros de tránsito.

Problema de Negocio
Las entidades responsables de la seguridad vial requieren identificar las regiones con mayor concentración de siniestros para priorizar acciones preventivas y optimizar recursos.

Objetivo
Desarrollar una solución de Ingeniería de Datos utilizando Databricks y Power BI para integrar, transformar y visualizar información relacionada con la seguridad vial en el Perú.

Arquitectura
Datos Abiertos ONSV
        |
        v
GitHub
        |
        v
Databricks

Bronze
 |
 v

Silver
 |
 v

Gold
 |
 v

Power BI
Tecnologías Utilizadas
Python
PySpark
Databricks
SQL
GitHub
Power BI
YAML
Fuente de Datos
Observatorio Nacional de Seguridad Vial (ONSV)

https://www.onsv.gob.pe/datosabiertos

Capas de Datos
Bronze
Datos originales provenientes del archivo Excel.

Tablas:

bronze_siniestros_region
bronze_causas_region
bronze_siniestros_tipo
Silver
Datos transformados y estandarizados.

Tablas:

silver_siniestros_region
Gold
Indicadores de negocio.

Tablas:

gold_riesgo_vial
gold_tendencia_siniestros
Principales Indicadores
Riesgo Vial por Región
Total de accidentes.
Ranking regional.
Clasificación del nivel de riesgo.
Tendencia Histórica
Evolución anual de siniestros.
Comparación histórica por región.
Data Quality
Validaciones implementadas:

Control de valores nulos.
Validación de estructura.
Verificación de agregaciones.
Consistencia de datos.
DataOps
Versionamiento mediante GitHub.
Control de configuraciones YAML.
Organización por capas Bronze, Silver y Gold.
Dashboard
Power BI conectado directamente a Databricks.

Visualizaciones:

KPI de siniestros.
Ranking de regiones.
Evolución histórica.
Clasificación de riesgo.
Autor: Kelly Melo

Herramientas
GitHub
Databricks
PySpark
SQL
Power BI
