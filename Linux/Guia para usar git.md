# Guía para usar GIT

## Instalación
> sudo apt-get install git

## Clonar repositorio

1. Crear carpeta deonde se guardará el repositorio
> sudo mkdir git  
> cd git

2. Descargar el repositorio desde GitHub
> sudo git clone http://github.com/usuario/repositorio.git

## Verificar estado
> git status

## Comprobar actualizaciónes en el repositorio remoto
> git fetch

## Agregar modificaciones al índice
> git add -A

## Guardar cambios al repositorio local
> git commit -m _mensaje de lo actualizado_

## Subir cambios del repositorio local al remoto (GitHub)
> git push 
Ingresar usuario y contraseña

## Descargar cambios del repositorio remoto (GitHub) al local
> git pull 
Es lo mismo que `git fetch` seguido de `git merge FETCH_HEAD`

## Ayuda sobre los comandos
> git _comando_ --help