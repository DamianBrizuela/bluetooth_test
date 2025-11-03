from bluetooth import DeviceDiscoverer, discover_devices, BluetoothError, BluetoothSocket, RFCOMM, lookup_name, find_service
import bleak
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


def conection(addr: str):
    port = 1  # generalmente RFCOMM usa el canal 1, pero depende del dispositivo
    sock = None
    try:
        sock = BluetoothSocket(RFCOMM)
        sock.connect((addr, port))
        sock.send("Hola desde Python!\n")

        data = sock.recv(1024)
        logger.info("Recibido:", data.decode())

    except Exception as e:
        logger.error(f"Error de conexion: {e}")

    finally:
        if sock:
            sock.close()
        logger.info("Conexion cerrada.")

def find_services(addr: str) :
    """ de acuerdo a un MAC address busca los servicios visibles """
    try:
        services = find_service(address=addr)
        if services:
            for svc in services:
                logger.info(f"Servicio: {svc['name']} | Canal: {svc['port']} | Tipo: {svc['protocol']}")
        else:
            logger.info("No se encontraron servicios visibles.")
    except BluetoothError as e:
        logger.error(f"No se pudo buscar servicios: {e}")

MAC =  init_devices()
if MAC:
    find_services(MAC)
    