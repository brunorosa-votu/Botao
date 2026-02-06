from machine import Pin
import time

led1 = Pin (2, Pin.OUT)
led2 = Pin (4, Pin.OUT)
led3 = Pin (5, Pin.OUT)

botao = Pin (35, Pin.IN, Pin.PULL_UP)

tempo = 0
contador = 0
pausa = 1
led1.off()
led2.off()
led3.off()
i = 0

while True:
    tempo = 0
    inicio = time.time()

    if botao.value() == 1 and i == 0:
        i = 1
        while tempo < 2:
            fim = time.time()
            tempo = fim - inicio

            if botao.value() == 1 and pausa == 1:
                contador += 1
                pausa = 0

            if botao.value() == 0:
                pausa = 1

            time.sleep(0.1)
    i = 0


    if contador == 1:
        led1.on()
        led2.off()
        led3.off()

    if contador == 2:
        led2.on()
        led1.off()
        led3.off()

    if contador == 3:
        led3.on()
        led2.off()
        led1.off()

    contador = 0