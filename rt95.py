import asyncio
import serial
from time import sleep
import struct

KEYS = {'RESET': b'AL~KR\r\n', 
       '0': b'AL~K0\r\n', 
       '1': b'AL~K1\r\n', 
       '2': b'AL~K2\r\n', 
       '3': b'AL~K3\r\n', 
       '4': b'AL~K4\r\n', 
       '5': b'AL~K5\r\n', 
       '6': b'AL~K6\r\n', 
       '7': b'AL~K7\r\n', 
       '8': b'AL~K8\r\n', 
       '9': b'AL~K9\r\n', 
       '*': b'AL~K*\r\n', 
       '#': b'AL~K#\r\n', 
       'AB': b'AL~K/\r\n', 
       'User1': b'AL~KA\r\n', 
       'User2': b'AL~KB\r\n', 
       'User3': b'AL~KC\r\n', 
       'User4': b'AL~KD\r\n'}

KEY_LIST = []
for k in KEYS:
       KEY_LIST.append(KEYS[k])

def to_struct(bytestring):
    return struct.unpack(bytestring)

def parse_data(bytestring):
    pass


class RT95:
    DEVICE = "/dev/ttyUSB0"
    TTY: serial.Serial

    RX_A = False
    RX_B = False
    TX_A = False
    TX_B = False
    VFO = 'A'

    tx_buffer = []
       
    def __init__(self, device="/dev/ttyUSB0", baud=9600):
        self.DEVICE = device
        self.TTY = serial.Serial(self.DEVICE, baud)

    def send_single(self, char):
        self.tx_buffer.append(KEYS[char])

    def send_multiple(self, presses):
        for char in presses:
            self.tx_buffer.append(KEYS[char])
            sleep(.1)

    async def main_loop(self):
        data = b''
        while self.TTY.inWaiting() == 0:
               while len(self.tx_buffer) > 0:
                      self.TTY.write(self.tx_buffer[0])
                      self.tx_buffer.pop(0)
                      self.TTY.flush()
              await asyncio.sleep(.5)
        while self.TTY.inWaiting() > 0:
            data += self.TTY.read(1)
            if data in KEY_LIST:
                   data = b''
    
    def setRTS(self, enable=True):
        self.TTY.setRTS(enable)
    
    def setPTT(self, enable=True):
        self.setRTS(enable)


if __name__ == "__main__":
    radio = rt95()
    while True:
        radio.setRTS(True)
        sleep(1)
        radio.setRTS(False)
        sleep(1)
