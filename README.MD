## Test de bluetooth 
Pequeño código para probar comunicación con bluetooth
# Crear entorno e instalar librerias
    1. Crear entorno de ejecución

`python -m venv .venv`

    2. Activar el entorno

`source .venv/bin/activate`

    3. Desactivar el entorno

`deactivate`

    4. Instalar dependencias

`pip install -r requeriments.txt`

## Comandos utiles para verificar estado de bluetooth
## Verificar bloqueos:

`rfkill list bluetooth`

## Eliminar bloqueos:

`sudo rfkill unblock bluetooth`

## Reiniciar servicio de bluetooth:

`sudo systemctl restart bluetooth`

## Listar dispositivos de bluetooth

`bluetoothctl list`