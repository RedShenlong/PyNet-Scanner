# ==========================================
# BANNER
# ==========================================
print("""
************************************************************************************************
*  ######  ####### ######      #####  #     # ####### #     # #       ####### #     #  #####   *
*  #     # #       #     #    #     # #     # #       ##    # #       #     # ##    # #     #  *
*  #     # #       #     #    #       #     # #       # #   # #       #     # # #   # #        *
*  ######  #####   #     #     #####  ####### #####   #  #  # #       #     # #  #  # #  ####  *
*  #   #   #       #     #          # #     # #       #   # # #       #     # #   # # #     #  *
*  #    #  #       #     #    #     # #     # #       #    ## #       #     # #    ## #     #  *
*  #     # ####### ######      #####  #     # ####### #     # ####### ####### #     #  #####   *                                                                                            
************************************************************************************************
""")

# ==========================================
# LIBRERIAS
# ==========================================
import socket
from concurrent.futures import ThreadPoolExecutor
import os

# ==========================================
# FUNCIONES
# ==========================================
def Verificar_puerto(ip, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, puerto))
        if result == 0:
            print(f" [+] Puerto {puerto:5} está ABIERTO")
            puertos_abiertos.append(puerto)
        sock.close()
    except:
        pass

def escaneo_de_puertos(ip):
    try:
        ip = socket.gethostbyname(ip)
        with ThreadPoolExecutor(max_workers=500) as executor:
            for puerto in range(1, 65536):
                executor.submit(Verificar_puerto, ip, puerto)
    except socket.gaierror:
        print("\n [!] No se pudo resolver la dirección IP.")
    except socket.error:
        print("\n [!] No se pudo conectar al servidor.")
        
# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    try:
        target = input("➤  Ingresa la IP a escanear: ").strip()
        global puertos_abiertos 
        puertos_abiertos = []
        if target:
            escaneo_de_puertos(target)
            print(f" »»» Puertos_abiertos: {puertos_abiertos}")
        else:
            print(" [!] Debes ingresar una IP válida.")
    except KeyboardInterrupt:
        print(f" »»» Puertos_abiertos: {puertos_abiertos}")
        print("\n\n [!] Programa cerrado.")
        os._exit(0)