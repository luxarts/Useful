#Auto montar partición

1. Buscar la ruta de la partición

> sudo fdisk -l

2. Crear directorio donde se montará

> sudo mkdir /mnt/_nombre_

3. Montar la ruta en el directorio

> sudo mount -t auto -v RUTA /mnt/_nombre_

Para desmontar usar
> sudo umount /mnt/_nombre_

4. Abrir el archivo `fstab` con un editor

> sudo nano /etc/fstab

5. Agregar al final del archivo lo siguiente
```
# Nombre de la particion
UUID=uuid /mnt/nombre auto defaults 0 2
```

Para obtener el uuid usar `sudo blkid` y copiar el UUID de la particion deseada

Ejemplo:
```
# Datos
UUID=01234567ABCDEF /mnt/datos auto defaults 0 2
```

6. Guardar y salir

> CTRL+X -> S -> Enter

7. Agregar permisos a la carpeta
> sudo chmod -Rv 777 /mnt/_nombre_  
> sudo chown -R _usuario_ /mnt/_nombre_
