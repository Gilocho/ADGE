#-------------------------------------------------------------
#|ads1262 pin label| Pin Function         |Raspi Connection  |
#|-----------------|:--------------------:|-----------------:|
#| DRDY            | Data ready Output pin|  PIN29     BCM5  |
#| MISO            | Slave Out            |  PIN21     BCM9  |
#| MOSI            | Slave In             |  PIN19     BCM10 |
#| SCLK            | Serial Clock         |  PIN23     BCM11 |
#| CS              | Chip Select          |  PIN24     BCM8  |
#| START           | Start Conversion     |  PIN31     BCM6  |
#| PWDN            | Power Down/Reset     |  PIN33     BCM13 |
#| DVDD            | Digital VDD          |  PIN2            |
#| DGND            | Digital Gnd          |  PIN6            |
#-------------------------------------------------------------


#/////////////////////////Librerias///////////////////////
import time
import spidev
import RPi.GPIO as GPIO
import csv
import struct

#//////////////////Asignacion de pines//////////////
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
CS_PIN = 8
DRDY_PIN = 5
START_PIN = 6
PWDN_PIN = 13
GPIO.setup(DRDY_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(START_PIN, GPIO.OUT)
GPIO.setup(PWDN_PIN, GPIO.OUT)
GPIO.setup(CS_PIN, GPIO.OUT)

#////////////////Comandosde Registros de Lectura////////
RREG  =0x20
WREG  =0x40
START =0x08
STOP  =0x0A
RDATAC=0x10
SDATAC=0x11
RDATA =0x12

#/////////////////////Direccion de Registros////////////
POWER    = 0x01
INTERFACE= 0x02
MODE0    = 0x03
MODE1    = 0x04
MODE2    = 0x05
INPMUX   = 0x06
OFCAL0   = 0x07
OFCAL1   = 0x08
OFCAL2   = 0x09
FSCAL0   = 0x0A
FSCAL1   = 0x0B
FSCAL2   = 0x0C
IDACMUX  = 0x0D
IDACMAG  = 0x0E
REFMUX   = 0x0F
TDACP    = 0x10
TDACN    = 0x11
GPIOCON  = 0x12
GPIODIR  = 0x13
GPIODAT  = 0x14
ADC2CFG  = 0x15
ADC2MUX  = 0x16
ADC2OFC0 = 0x17
ADC2OFC1 = 0x18
ADC2FSC0 = 0x19
ADC2FSC1 = 0x1A

#///////////////////////////////Variables//////////////
No_op=[0x00,0x00,0x00,0x00,0x00,0x00]
No_opF=[0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
#No_op=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
CH0 = 0x09
CH1 = 0x19
CH2 = 0x29
CH3 = 0x39
CH4 = 0x49
CH5 = 0x59
CH6 = 0x69
CH7 = 0x79
t = 0
resolucion=2.5/(2**31)

#/////////////////////Funciones///////////////////

def Reset():
    GPIO.output(PWDN_PIN,1)
    time.sleep(0.001)
    GPIO.output(PWDN_PIN,0)
    time.sleep(0.001)
    GPIO.output(PWDN_PIN,1)
    time.sleep(0.001)
    return

def Hard_Stop():
    GPIO.output(START_PIN,0)
    time.sleep(0.02)
    return

def Enable_Start():
    GPIO.output(START_PIN,1)
    time.sleep(0.02)
    return

def Leer_Dato():
    i = 0
    while GPIO.input(DRDY_PIN) == GPIO.HIGH:
        i=i+1
    time.sleep(0.1)
    Buff=spi.xfer(No_opF)
    return Buff

def Escribir_Reg(DIRECCION,DATO):
    DataToSend = DIRECCION|WREG
    PAQUETE = [DataToSend,0x00,DATO]
    spi.xfer(PAQUETE)
    return

def Inicializacion():
    Reset()
    time.sleep(0.1)
    Hard_Stop()
    time.sleep(0.1)

    Escribir_Reg(POWER,0x11)
    time.sleep(0.01)
    Escribir_Reg(INTERFACE,0x05)
    time.sleep(0.01)
    Escribir_Reg(MODE0,0x00)
    time.sleep(0.01)
    Escribir_Reg(MODE1,0x80)
    time.sleep(0.01)
    Escribir_Reg(MODE2,0x04)
    time.sleep(0.01)
    Escribir_Reg(INPMUX,CH0)
    time.sleep(0.01)
    Escribir_Reg(OFCAL0,0x00)
    time.sleep(0.01)
    Escribir_Reg(OFCAL1,0x00)
    time.sleep(0.01)
    Escribir_Reg(OFCAL2,0x00)
    time.sleep(0.01)
    Escribir_Reg(FSCAL0,0x00)
    time.sleep(0.01)
    Escribir_Reg(FSCAL1,0x00)
    time.sleep(0.01)
    Escribir_Reg(FSCAL2,0x40)
    time.sleep(0.01)
    Escribir_Reg(IDACMUX,0xBB)
    time.sleep(0.01)
    Escribir_Reg(IDACMAG,0x00)
    time.sleep(0.01)
    Escribir_Reg(REFMUX,0x00)
    time.sleep(0.01)
    Escribir_Reg(TDACP,0x00)
    time.sleep(0.01)
    Escribir_Reg(TDACN,0x00)
    time.sleep(0.01)
    Escribir_Reg(GPIOCON,0x00)
    time.sleep(0.01)
    Escribir_Reg(GPIODIR,0x00)
    time.sleep(0.01)
    Escribir_Reg(GPIODAT,0x00)
    time.sleep(0.01)
    Escribir_Reg(ADC2CFG,0x00)
    time.sleep(0.01)
    Escribir_Reg(ADC2MUX,0x01)
    time.sleep(0.01)
    Escribir_Reg(ADC2OFC0,0x00)
    time.sleep(0.01)
    Escribir_Reg(ADC2OFC1,0x00)
    time.sleep(0.01)
    Escribir_Reg(ADC2FSC0,0x00)
    time.sleep(0.01)
    Escribir_Reg(ADC2FSC1,0x40)
    time.sleep(0.01)
    Enable_Start()
    return

#/////////////////////Configuracion SPI//////////////
bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 1000000
spi.mode = 1

#//////////////////////Configuracion CSV/////////////////
salidaCSV = open('/home/pi/tesis/datos_new.csv', 'a')
salida = csv.writer(salidaCSV, delimiter=',')

Inicializacion()

while True:
    tic=time.time()
    Day_frame=time.strftime("%x %X")
    Escribir_Reg(INPMUX,CH0)
    Buff_ADS0 = Leer_Dato()
    ADS_DATO0=Buff_ADS0[1]<<24|Buff_ADS0[2]<<16|Buff_ADS0[3]<<8|Buff_ADS0[4]
    #Voltaje0=resolucion*ADS_DATO0
    Reset()

    Escribir_Reg(INPMUX,CH1)
    Buff_ADS1 = Leer_Dato()
    ADS_DATO1=Buff_ADS1[1]<<24|Buff_ADS1[2]<<16|Buff_ADS1[3]<<8|Buff_ADS1[4]
    #Voltaje1=resolucion*ADS_DATO1
    Reset()

    Escribir_Reg(INPMUX,CH2)
    Buff_ADS2 = Leer_Dato()
    ADS_DATO2=Buff_ADS2[1]<<24|Buff_ADS2[2]<<16|Buff_ADS2[3]<<8|Buff_ADS2[4]
    #Voltaje2=resolucion*ADS_DATO2
    Reset()

    """Escribir_Reg(INPMUX,CH3)
    Buff_ADS3 = Leer_Dato()
    ADS_DATO3=Buff_ADS3[1]<<24|Buff_ADS3[2]<<16|Buff_ADS3[3]<<8|Buff_ADS3[4]
    #Voltaje3=resolucion*ADS_DATO3
    Reset()

    Escribir_Reg(INPMUX,CH4)
 	Buff_ADS4 = Leer_Dato()
    ADS_DATO4=Buff_ADS4[1]<<24|Buff_ADS4[2]<<16|Buff_ADS4[3]<<8|Buff_ADS4[4]
    #Voltaje4=resolucion*ADS_DATO4
    Reset()

    Escribir_Reg(INPMUX,CH5)
    Buff_ADS5 = Leer_Dato()
    ADS_DATO5=Buff_ADS5[1]<<24|Buff_ADS5[2]<<16|Buff_ADS5[3]<<8|Buff_ADS5[4]
    #Voltaje5=resolucion*ADS_DATO5
    Reset()

    Escribir_Reg(INPMUX,CH6)
    Buff_ADS6 = Leer_Dato()
    ADS_DATO6=Buff_ADS6[1]<<24|Buff_ADS6[2]<<16|Buff_ADS6[3]<<8|Buff_ADS6[4]
    #Voltaje6=resolucion*ADS_DATO6
    Reset()

    Escribir_Reg(INPMUX,CH7)
    Buff_ADS7 = Leer_Dato()
    ADS_DATO7=Buff_ADS7[1]<<24|Buff_ADS7[2]<<16|Buff_ADS7[3]<<8|Buff_ADS7[4]
    #Voltaje7=resolucion*ADS_DATO7
    Reset()"""

#    print(Day_frame)
 #   print(ADS_DATO0)
 #   print(ADS_DATO1)
 #   print(ADS_DATO2)
    """pr int(ADS_DATO3)
    print(ADS_DATO4)
    print(ADS_DATO5)
    print(ADS_DATO6)
    print(ADS_DATO7)"""
    salida.writerow([ADS_DATO0,ADS_DATO1,ADS_DATO2,Day_frame])
    toc=time.time()
    times=1-(toc-tic)
    if times<0:
       times=(times)*(-1)	
    time.sleep(times)
    #print(1-(toc-tic))
   # t=t+1








