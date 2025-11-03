import bluetooth

print("Buscando dispositivos...")
devices = bluetooth.discover_devices(lookup_names=True)

print("Dispositivos encontrados:")
for addr, name in devices:
    print(f"{name} - {addr}")
