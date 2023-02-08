# Scraping sobre Amazon

Código para hacer web scraping de Amazon sobre los ejemplos de "productos para perro" y "whisky". Se obtienen 303 y 281 productos, respectivamente, al realizar la búsqueda simple en el buscador de Amazon en aproximadamente 1 minuto y 40 segundos por cada uno.

Cada elemento extraído consta de:
* Nombre del producto.
* Precio.
* URL.
* Calificación.
* Número de calificaciones.
* Porcentaje por cantidad de estrellas de calificación.

El código permite realizar el scraping sin importar la búsqueda, como se puede observar en las categorías diametralmente opuestas. Asimismo, si se requiere hacer ajustes en los datos extraídos, como comentarios, imágenes, etc., simplemente deben especificarse en el código los objetivos y extraerlos con el resto de datos.

Finalmente, se anexan los resultados en formato JSON y CSV para que puedan utilizarse como base de datos en aplicaciones varias, como una aplicación web o análisis y manipulación de datos con Pandas y NumPy.