from machine import pin 

led1 = LED(32, Pin.OUT)
led2 = LED(33, Pin.OUT)
led3 = LED(25, Pin.OUT)

def connect_to(ssid : str, passwd : str) -> None:
    """Conecta el microcontrolador a la red indicada.

    Parameters
    ----------
    ssid : str
        Nombre de la red a conectarse
    passwd : str
        Contraseña de la red
    """
    
    import network
    from time import sleep
    

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            print(".",end="")
            sleep(.05)
    
    print()
    print("Network config:", sta_if.ifconfig())
    
connect_to("Cooperadora Alumnos", "")