# Juego pygame the_quest

pendientes:
   Surface entrada nombre se sobrescribe y se ve borroso.
   Hace falta doble espacio al entrar nombre para continuar.
   Ajustar velocidad meteoritos con diccionario. Separar velocidad a propiedad.
   Animación aterrizaje.
   Ajustar base de datos, id auto va subiendo y no se restablece al eliminar.
   Ordenar el código:
     ¿Hacer clase sql con sus funciones?
     Ordenar main.py y hacer archivo con funciones.

## Instalación 
1. Ejecutar
```
pip install -r requirements.txt
```

2. Crear _config.py

Renombrar `_config_template.py` a `_config.py` e informar correctamente ruta base de datos.

3. Crear BD

Ejecutar `migrations.sql` con `sqlite3` en el fichero elegido como base de datos
