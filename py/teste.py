# Teste simples para acender e apagar um led 

import serial
import time

arduino = serial.Serial(port='COM9', baudrate=9600, timeout=1)
time.sleep(2)

def enviar_comando(comando):
    arduino.write(f"{comando}\n".encode())
    print(f"Comando enviado: {comando}")

while True:
    cmd = input("Digite LED_ON, LED_OFF ou SAIR: ").strip()
    if cmd == "SAIR":
        break
    enviar_comando(cmd)