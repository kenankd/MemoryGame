from ili934xnew import ILI9341, color565
from machine import Pin, SPI
from micropython import const
import os
import glcdfont
import tt14
import tt24
import tt32
import time
from utime import sleep
import random
from machine import ADC
import utime
import sys
 
 
#Definisanje matricne tastature
R1 = Pin(21, Pin.OUT)
R2 = Pin(22, Pin.OUT)
R3 = Pin(26, Pin.OUT)
R4 = Pin(27, Pin.OUT)
C1 = Pin(0, Pin.IN, Pin.PULL_DOWN)
C2 = Pin(1, Pin.IN, Pin.PULL_DOWN)
C3 = Pin(2, Pin.IN, Pin.PULL_DOWN)
C4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
adc = ADC(Pin(28))
 
#Definisanje display-a
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(2)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)
TFT_CLK_PIN = const(18)
TFT_MOSI_PIN = const(19)
TFT_MISO_PIN = const(16)
TFT_CS_PIN = const(17)
TFT_RST_PIN = const(20)
TFT_DC_PIN = const(15)
spi = SPI(
    0,
    baudrate=62500000,
    miso=Pin(TFT_MISO_PIN),
    mosi=Pin(TFT_MOSI_PIN),
    sck=Pin(TFT_CLK_PIN))
display = ILI9341(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=2)
display.set_font(tt24)
display.erase()
display.rotation=1
 
#Kreiranje prazne sekvence int-ova
sekvenca2=[1]
sekvenca2.pop()
 
# Funkcija za generisanje sekvence za mod1
def generisi_sekvencu(nivo):
    return [random.randint(1, 9) for _ in range(nivo)]
 
# Funkcija za generisanje sekvence za mod2
def generisi_sekvencu2():
    sekvenca2.append(random.randint(1,9))
 
# Funkcija za prikazivanje sekvence
def prikazi_sekvencu(mod,sekvenca,nivo,boja):
#Definisanje vremena i velicine trajanja krugova
    vrijeme=0.5
    velicina=15
    if boja==0:
        boja2=color565(255, 0, 0)
    elif boja==1:
        boja2=color565(0,255,0)
    elif boja==2:
        boja2=color565(0,0,255)
    if mod==2:
        if(nivo<6):
            vrijeme=vrijeme-(nivo*0.1)
        else:
            vrijeme=0
            if(nivo<11):
                velicina=velicina-nivo+5
            else:
                velicina=10
    for broj in sekvenca:
        if(broj == 1):
            for c in range(velicina):
                draw_circle(53, 106, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(53, 106, c, color565(0, 0, 0))
        if(broj == 2):
            for c in range(velicina):
                draw_circle(119, 106, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(119, 106, c, color565(0, 0, 0))
        if(broj == 3):
            for c in range(velicina):
                draw_circle(185, 106, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(185, 106, c, color565(0, 0, 0))
        if(broj == 4):
            for c in range(velicina):
                draw_circle(53, 179, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(53, 179, c, color565(0, 0, 0))
        if(broj == 5):
            for c in range(velicina):
                draw_circle(119, 179, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(119, 179, c, color565(0, 0, 0))
        if(broj == 6):
            for c in range(velicina):
                draw_circle(185, 179, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(185, 179, c, color565(0, 0, 0))
        if(broj == 7):
            for c in range(velicina):
                draw_circle(53, 252, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(53, 252, c, color565(0, 0, 0))
        if(broj == 8):
            for c in range(velicina):
                draw_circle(119, 252, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(119, 252, c, color565(0, 0, 0))
        if(broj == 9):
            for c in range(velicina):
                draw_circle(185, 252, c, boja2)
            time.sleep(vrijeme)
            for c in range(velicina):
                draw_circle(185, 252, c, color565(0, 0, 0))
 
 #Funkcija za iscrtavanje pojedinačnog kruga
def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        # Prikaz pojedinačnih piksela
        display.pixel(xpos0 + x, ypos0 + y, col)
        display.pixel(xpos0 + y, ypos0 + x, col)
        display.pixel(xpos0 - y, ypos0 + x, col)
        display.pixel(xpos0 - x, ypos0 + y, col)
        display.pixel(xpos0 - x, ypos0 - y, col)
        display.pixel(xpos0 - y, ypos0 - x, col)
        display.pixel(xpos0 + y, ypos0 - x, col)
        display.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)
 
 
#Funkcija za unos i provjeru unosa sekvence
def provjeri_unos(mod, nivo, sekvenca):
    unos = []
#Dva različita mod-a
    if(nivo>4 and mod==1):
        vrijeme = utime.ticks_ms()
        while(utime.ticks_diff(utime.ticks_ms(), vrijeme) < 15000):
            display.set_pos(140,10)
            display.print("Time: " + str(15-int(utime.ticks_diff(utime.ticks_ms(), vrijeme)/1000)))
            R1.value(1)
            if C1.value() == 1:
                unos.append(1)
                print(1)
                while(C1.value()==1):
                    pass
            elif C2.value() == 1:
                unos.append(2)
                print(2)
                while(C2.value()==1):
                    pass
            elif C3.value() == 1:
                unos.append(3)
                print(3)
                while(C3.value()==1):
                    pass
            R1.value(0)
            R2.value(1)
            if C1.value() == 1:
                unos.append(4)
                print(4)
                while(C1.value()==1):
                    pass
            elif C2.value() == 1:
                unos.append(5)
                print(5)
                while(C2.value()==1):
                    pass
            elif C3.value() == 1:
                unos.append(6)
                print(6)
                while(C3.value()==1):
                    pass
            R2.value(0)
            R3.value(1)
            if C1.value() == 1:
                unos.append(7)
                print(7)
                while(C1.value()==1):
                    pass
            elif C2.value() == 1:
                unos.append(8)
                print(8)
                while(C2.value()==1):
                    pass
            elif C3.value() == 1:
                unos.append(9)
                print(9)
                while(C3.value()==1):
                    pass
            R3.value(0)
            R4.value(1)
            if(C1.value()==1):
                if(len(unos)>0):
                    vrijednost=[]
                    vrijednost.append(unos.pop())
                    print(140)
                    while(C1.value()==1):
                        pass
            elif(C3.value()==1):
                print(0)
                break
            elif(C4.value()==1):
                return 2
            R4.value(0)
            time.sleep(0.1)
    else:
        while(1):
            R1.value(1)
            if C1.value() == 1:
                unos.append(1)
                prikazi_sekvencu(2, [1], 10,1)
                print(1)
                while(C1.value()==1):
                    pass
            elif C2.value() == 1:
                unos.append(2)
                prikazi_sekvencu(2, [2], 10,1)
                print(2)
                while(C2.value()==1):
                    pass
            elif C3.value() == 1:
                unos.append(3)
                prikazi_sekvencu(2, [3], 10,1)
                print(3)
                while(C3.value()==1):
                    pass
            R1.value(0)
            R2.value(1)
            if C1.value() == 1:
                unos.append(4)
                prikazi_sekvencu(2, [4], 10,1)
                print(4)
                while(C1.value()==1):
                    pass
            elif C2.value() == 1:
                unos.append(5)
                prikazi_sekvencu(2, [5], 10,1)
                print(5)
                while(C2.value()==1):
                    pass
            elif C3.value() == 1:
                unos.append(6)
                prikazi_sekvencu(2, [6], 10,1)
                print(6)
                while(C3.value()==1):
                    pass
            R2.value(0)
            R3.value(1)
            if C1.value() == 1:
                unos.append(7)
                prikazi_sekvencu(2, [7], 10,1)
                print(7)
                while(C1.value()==1):
                    pass
            elif C2.value() == 1:
                unos.append(8)
                prikazi_sekvencu(2, [8], 10,1)
                print(8)
                while(C2.value()==1):
                    pass
            elif C3.value() == 1:
                unos.append(9)
                prikazi_sekvencu(2, [9], 10,1)
                print(9)
                while(C3.value()==1):
                    pass
            R3.value(0)
            R4.value(1)
            if(C1.value()==1):
                if(len(unos)>0):
                    vrijednost=[]
                    vrijednost.append(unos.pop())
                    prikazi_sekvencu(2, vrijednost, 10,0)
                    print(140)
                    while(C1.value()==1):
                        pass
            elif(C3.value()==1):
                print(0)
                break
            elif(C4.value()==1):
                return 2
            R4.value(0)
            time.sleep(0.1)
    return (sekvenca==unos)
 
 
#Funkcija za iscrtavanje polja i poziv ostalih funkcija potrebnih za igru
def zapocni_igru(mod,nivo):
    while(1):
        if(nivo==1):
            sekvenca2.clear()
        if mod==1:
            sekvenca = generisi_sekvencu(nivo)
        elif mod==2:
            generisi_sekvencu2()
            sekvenca = sekvenca2
        col=color565(255, 255, 255)
        x=10
        y=200
        display.erase()
        display.set_color(color565(255, 255, 255), color565(0, 0, 0))
        display.set_font(tt24)
        display.set_pos(10,10)
        display.print("Lvl " + str(nivo))
        display.set_pos(120,10)
 
        #gornja granica
        x=220
        y=70
        while x>20:
            display.pixel(int(x),int(y),col)
            x=x-1
 
        #donja granica
        x=220
        y=290
        while x>20:
            display.pixel(int(x),int(y),col)
            x=x-1
 
        #desna granica
        x=220
        y=290
        while y>70:
            display.pixel(int(x),int(y),col)
            y=y-1
 
        #lijeva granica
        x=20
        y=290
        while y>70:
            display.pixel(int(x),int(y),col)
            y=y-1
 
        #unutrašnja lijeva 
        x=86
        y=290
        while y>70:
            display.pixel(int(x),int(y),col)
            y=y-1
 
        #unutrašnja desna
        x=153
        y=290
        while y>70:
            display.pixel(int(x),int(y),col)
            y=y-1
 
        #unutrašnja gornja
        x=220
        y=143
        while x>20:
            display.pixel(int(x),int(y),col)
            x=x-1
 
        #unutrašnja donja
        x=220
        y=216
        while x>20:
            display.pixel(int(x),int(y),col)
            x=x-1
        prikazi_sekvencu(mod,sekvenca,nivo,2)
        unos=provjeri_unos(mod,nivo,sekvenca)
        if(unos):
            if(unos==2):
                break
            nivo+=1
            display.erase()
            display.set_font(tt32)
            display.set_pos(45,CENTER_Y-20)
            display.set_color(color565(0, 150, 0), color565(0, 0, 0))
            display.print("LEVEL "+str(nivo-1))
            display.print("COMPLETED")
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.set_font(tt24)
            time.sleep(1)
            display.erase()
 
        else:
            display.erase()
            display.set_font(tt32)
            display.set_pos(45,CENTER_Y-40)
            display.set_color(color565(255, 0, 0), color565(0, 0, 0))
            display.print("LEVEL "+str(nivo))
            display.print("FAILED")
            display.print("BACK TO START")
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.set_font(tt24)
            nivo=1
            time.sleep(3)
            display.erase()
 
 
#Funkcija za prikaz početnog ekrana
def welcome_screen(prvi_put, nivo):
    while(1):
        display.erase()
        display.set_font(tt32)
        if(prvi_put):
            prvi_put=0
            display.set_pos(50,CENTER_Y-10)
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.print("WELCOME")
            time.sleep(0.5)
            display.set_pos(50,CENTER_Y-10)
            display.set_color(color565(0, 0, 0), color565(0, 0, 0))
            display.print("WELCOME")
            display.set_pos(50,CENTER_Y-10)
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.print("WELCOME")
            time.sleep(0.5)
            display.set_pos(50,CENTER_Y-10)
            display.set_color(color565(0, 0, 0), color565(0, 0, 0))
            display.print("WELCOME")
        display.set_pos(10,20)
        display.set_color(color565(255, 255, 255), color565(0, 0, 0))
        display.set_font(tt24)
        display.print("SELECT MODE")
        display.print("CLICK A OR B:")
        display.print("")
        display.print("CLICK C")
        display.print("FOR MORE INFORMATION:")
        display.print("")
        display.print("CLICK D")
        display.print("TO GO TO MENU:")
        display.print("")
        display.print("CLICK #")
        display.print("TO TURN OFF:")
        select_mode(nivo)
 
 
 
#Funkcija za prikaz dodatnih informacija
def dodatne_informacije():
    display.erase()
    display.set_font(tt24)
    display.set_pos(10,10)
    display.set_color(color565(255, 255, 255), color565(0, 0, 0))
    display.print("Explanation")
    display.set_font(tt14)
    display.print("Wait for the sequence to show up on the screen and repeat it on the keyboard, pressing the numbers in the order show on screen. After that press # to confirm input. Use * to erase the last input.")
    display.print("")
    display.print("MODE A")
    display.print("Mode A increases the sequence every level starting from 1.")
    display.print("")
    display.print("MODE B")
    display.print("Mode B increases the size of the sequence every level and randomizes it, but also decreases the time the circle is shown on screen. After level 5 to level 10 the circles get smaller and the time it is shown on screen is less.")
    while(1):
        R1.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
            break
        R1.value(0)
        R2.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
            break
        R2.value(0)
        R3.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1 ):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
            break
        R3.value(0)
        R4.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
            break
        R4.value(0)
 
 
#Funkcija za odabir mod-a
def select_mode(nivo):
    while(1):
        sekvenca2.clear()
        R1.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
        elif (C4.value()==1):
            while(C4.value()==1):
                pass
            display.set_pos(10,20)
            display.set_color(color565(0, 0, 0), color565(0, 0, 0))
            display.print("SELECT MODE")
            display.print("CLICK A OR B:")
            display.print("")
            display.print("CLICK C")
            display.print("FOR MORE INFORMATION:")
            display.print("")
            display.print("CLICK D")
            display.print("TO GO TO MENU:")
            display.print("")
            display.print("CLICK #")
            display.print("TO TURN OFF:")
            display.set_pos(10,60)
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.print("AFTER YOU TYPE THE SEQUENCE PRESS # TO CONFRIM OR PRESS * TO ERASE THE LAST ENTRY")
            display.print("")
            display.print("PRESS # IF YOU UNDERSTAND")
            R4.value(1)
            while(C3.value()==0):
                pass
            R4.value(0)
            zapocni_igru(1,nivo)
            break
        R1.value(0)
        R2.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
        elif (C4.value()==1):
            while(C4.value()==1):
                pass
            display.set_pos(10,20)
            display.set_color(color565(0, 0, 0), color565(0, 0, 0))
            display.print("SELECT MODE")
            display.print("CLICK A OR B:")
            display.print("")
            display.print("CLICK C")
            display.print("FOR MORE INFORMATION:")
            display.print("")
            display.print("CLICK D")
            display.print("TO GO TO MENU:")
            display.print("")
            display.print("CLICK #")
            display.print("TO TURN OFF:")
            display.set_pos(10,60)
            display.set_color(color565(255, 255, 255), color565(0, 0, 0))
            display.print("AFTER YOU TYPE THE SEQUENCE PRESS # TO CONFRIM OR PRESS * TO ERASE THE LAST ENTRY")
            display.print("")
            display.print("PRESS # IF YOU UNDERSTAND")
            R4.value(1)
            while(C3.value()==0):
                pass
            R4.value(0)
            zapocni_igru(2,nivo)
            break
        R2.value(0)
        R3.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C3.value() == 1):
            while(C1.value() == 1 or C2.value() == 1 or C3.value() == 1 or C4.value()==1):
                pass
        elif(C4.value() ==1):
            while(C4.value()==1):
                pass
            dodatne_informacije()
            break
        R3.value(0)
        R4.value(1)
        if (C1.value() == 1 or C2.value() == 1 or C4.value()==1):
            while(C1.value() == 1 or C2.value() == 1 or C4.value()==1):
                pass
        elif(C3.value()==1):
            while(C3.value()==1):
                pass
            display.erase()
            sys.exit()
        R4.value(0)
 
 
# Glavna petlja igre
while (1):
    nivo = 1
    sec=10
    welcome_screen(1,nivo)
 