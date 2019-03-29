# Ejecutar comando al inicio de la sesión

1. Editar el archivo `~/.bashrc`
> sudo nano ~/.bashrc

2. Agregar al final del archivo el comando en una nueva linea
Ej:
```
sudo python3 script.py
```

3. Guardar y salir
> CTRL+X -> S -> Enter

---

# Ejecutar comando al inicio del sistema

1. Editar el archivo `/etc/rc.local`
> sudo nano /etc/rc.local

2. Agregar antes de la linea `exit 0` el comando en una nueva linea
Ej:
```
sudo python3 script.py
exit 0
```

3. Guardar y salir
> CTRL+X -> S -> Enter