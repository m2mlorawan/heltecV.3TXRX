from sx1262 import SX1262
import time

import machine, ssd1306, time
from machine import Pin,SoftI2C
pin21 = machine.Pin(21, machine.Pin.OUT)
pin21.value(1) #heltec V3

# init ic2 object
i2c = machine.SoftI2C(scl=machine.Pin(18), sda=machine.Pin(17), freq=20000) #heltec V3
lcd=ssd1306.SSD1306_I2C(128,64,i2c,60)


#sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=3, irq=20, rst=15, gpio=2)
sx = SX1262(spi_bus=1, clk=9, mosi=10, miso=11, cs=8, irq=14, rst=12, gpio=13)
# LoRa
sx.begin(freq=923, bw=500.0, sf=12, cr=8, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

# FSK
##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
##            tcxoVoltage=1.6, useRegulatorLDO=False,
##            blocking=True)

while True:
    msg, err = sx.recv()
    if len(msg) > 0:
        error = SX1262.STATUS[err]
        print(msg)
        print(error)
        lcd.text(msg,0,0)
        lcd.show()         
