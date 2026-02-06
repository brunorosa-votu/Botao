from machine import Pin
import time

led1 = Pin (2, Pin.OUT)
led2 = Pin (4, Pin.OUT)
led3 = Pin (5, Pin.OUT)

botao = Pin (35, Pin.IN, Pin.PULL_UP)

tempo = 0
contador = 0
pausa = False

def apagar():
    led1.off()
    led2.off()
    led3.off()
apagar()
i = True

def espera():
    time.sleep(0.1)

while True:
    tempo = 0
    inicio = time.time()

    if botao.value() == 1 and i == True:
        i = False
        while tempo < 2:
            fim = time.time()
            tempo = fim - inicio

            if botao.value() == 1 and pausa == False:
                contador += 1
                pausa = True

            if botao.value() == 0:
                pausa = False

            espera()
    i = True


    if contador == 1:
        apagar()
        led1.on()

    if contador == 2:
        apagar()
        led2.on()

    if contador == 3:
        apagar()
        led3.on()

    elif contador > 3:
        s = True
        while s == True:
            apagar()
            led3.on()
            espera()
            apagar()
            espera()
            led2.on()
            espera()
            apagar()
            espera()
            led1.on()
            espera()
            if botao.value() == 1:
                s = False


    contador = 0