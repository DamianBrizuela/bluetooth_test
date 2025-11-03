from bluetooth import DeviceDiscoverer, discover_devices, BluetoothError
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def init_devices():

    try:
        logger.info("Buscando dispositivos...")
        founded_devices = discover_devices(lookup_names=True)
        if founded_devices:
            for addr, name in founded_devices:
                logger.info(f"Dispositivo encontrado: {name} - {addr}")
    except BluetoothError as bt_err:
        logger.error(f"Error Bluetooth al buscar dispositivos: {bt_err}")
    except Exception as e:
        logger.error(f"Error al buscar dispositivos: {e}")