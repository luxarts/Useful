#Agregar entrada al menu de GNOME 

1. Crear archivo .desktop en

`/usr/share/applications/` si para todos los usuarios
`/home/<usuario>/.local/share/applications/` si es para un usuario

>sudo nano <ruta>/.<nombre-de-la-app>.desktop

2. Editar el archivo con la siguiente información

```
[Desktop Entry]
Type=
Encoding=
Name=
Comment=
Icon=
Terminal=
Categories=
Exec=

```

**Explicación**
* `Type` tipo de entrada (`Application`, `Link` o `Directory`).
* `Encoding` codificación de caracteres (por lo general, UTF-8).
* `Name` nombre de la entrada.
* `Comment` descripción.
* `Icon` ruta absoluta del ícono.
* `Terminal` si debe ejecutarse en una terminal (`true` o `false`).
* `Categories` categorias donde estará la entrada separadas por punto y coma (`;`).
* `Exec` ruta absoluta del ejecutable.

Los argumentos para `Exec` se pueden obtener con las siguientes variables
* `%f` el nombre de un archivo.
* `%F` el nombre de varios archivos.
* `%u` una URL.
* `%U` varias URLs.
* `%d` un directorio. Usado en conjunto con `%f` para obtener un archivo.
* `%D` varios directorios. Usado en conjunto con `%F` para obtener varios archivos.
* `%n` el nombre de un archivo sin la ruta
* `%N` el nombre de varios archivos sin sus rutas

3. Guardar el archivo

>Ctrl+X -> S -> Enter