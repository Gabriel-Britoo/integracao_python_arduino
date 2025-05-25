# Controle de leds no Arduino UNO usando o joystick esquerdo de um controle de videogame 
# via bibliotecas em Python (serial e pygame).

import serial
import pygame
import time

# Substitua "COM9" pela porta em que seu Arduino está conectado
arduino = serial.Serial(port='COM9', baudrate=9600, timeout=1)
time.sleep(2)

arduino.write(b'START\n')

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

limiar = 0.6
ultimo_comando = ""

def enviar_sinal(direcao):
    global ultimo_comando
    if direcao != ultimo_comando:
        arduino.write(f"{direcao}\n".encode())
        print(f"Sinal enviado: {direcao}")
        ultimo_comando = direcao

try:
    while True:
        pygame.event.pump()
        eixo_x = joystick.get_axis(0)
        eixo_y = joystick.get_axis(1)

        if eixo_y < -limiar:
            enviar_sinal("CIMA")
        elif eixo_y > limiar:
            enviar_sinal("BAIXO")
        elif eixo_x < -limiar:
            enviar_sinal("ESQUERDA")
        elif eixo_x > limiar:
            enviar_sinal("DIREITA")
        else:
            enviar_sinal("ZERO")

        time.sleep(0.05)

except KeyboardInterrupt:
    arduino.write(b'END\n')
    print("\nSaindo...")