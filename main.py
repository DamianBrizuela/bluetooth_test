from bluetooth import DeviceDiscoverer, discover_devices, BluetoothError, BluetoothSocket, RFCOMM
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def init_devices() -> str:

    try:
        logger.info("Buscando dispositivos...")
        founded_devices = discover_devices(lookup_names=True)
        if founded_devices:
            for addr, name in founded_devices:
                logger.info(f"Dispositivo encontrado: {name} - {addr}")

        return founded_devices[0][0] if founded_devices else None
    except BluetoothError as bt_err:
        logger.error(f"Error Bluetooth al buscar dispositivos: {bt_err}")
    except Exception as e:
        logger.error(f"Error al buscar dispositivos: {e}")


def conection(bd_addr: str):
    port = 1  # generalmente RFCOMM usa el canal 1, pero depende del dispositivo
    sock = None
    try:
        sock = BluetoothSocket(RFCOMM)
        sock.connect((bd_addr, port))
        sock.send("Hola desde Python!\n")

        data = sock.recv(1024)
        logger.info("Recibido:", data.decode())

    except Exception as e:
        logger.error(f"Error de conexion: {e}")

    finally:
        if sock:
            sock.close()
        logger.info("Conexion cerrada.")


MAC =  init_devices()
if MAC:
    conection(MAC)