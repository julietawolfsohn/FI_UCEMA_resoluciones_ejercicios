# Workshops/[ES]Scripting.md at master · WomenBioinfoDataScLA/Workshops · GitHub

- <os> → operative system
	Biblioteca que permite mover/ejecutar cosas
- <sys> → biblioteca que toma parámetros entre terminales

# ARCHIVOS DE LECTURA
> Se puede leer todo en una línea o línea por línea.
> open(path_al_articulo, modo) → abre archivo. close → cierro el archivo
	> Tiene que ser un STR con la dirección a mi archivo
	> modo → la forma en que quiero ejecutarlo 
		> <r> → de lectura
		> <w> → escritura. Si el archivo no existe crea uno, si es que si, sobreescribe sobre eso borrando lo anterior.
		> <r+> → lectura y escritura
		> <a> → agrega al final del archivo
		> STR “ “
		> .readlines() → lee línea a línea Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.
		> .read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.
		> .readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.


> Otra forma para abrir archivo de forma segura:
	> with open(path_al_archivo, modo) as miarch:
    	# Aquí van las líneas de procesamiento del archivo

> RUTA ABSOLUTO: home/usuario/doc/Mi_nombre.txt → esto lo hago si el archivo que llama está en otro directorio.
	> Asumo un usuario, cuando lo prueba otro rompe.

> RUTA RELATIVA: “donde estoy parada”./doc/Mi_nombre.txt
	> No asume un usuario → mejor para los parciales.

