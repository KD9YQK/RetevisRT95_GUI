import asyncio
import serial
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
    return struct.unpack('12b', bytestring)


class RT95:
    DEVICE = "/dev/ttyUSB0"
    TTY: serial.Serial

    RX_A = False
    RX_B = False
    TX_A = False
    TX_B = False
    VFO = 'A'

    tx_buffer = []
    isRTS = False

    def parse_data(self, data):
        d_spl = data.split(b'ST')
        d_spl.pop(0)
        for d in d_spl:
            d_st = to_struct(d)
            if d_st[6] == 0:
                self.VFO = 'A'
            else:
                self.VFO = 'B'
            if d_st[4] == 7:
                self.TX_A = True
            else:
                self.TX_A = False
            if d_st[5] == 7:
                self.TX_B = True
            else:
                self.TX_B = False
            if d_st[10] == 1 and d_st[2] == 1:
                self.RX_A = True
            elif d_st[10] == 1 and d_st[2] == 0:
                self.RX_B = True
            else:
                self.RX_A = False
                self.RX_B = False

    def __init__(self, device="/dev/ttyUSB0", baud=9600):
        self.DEVICE = device
        self.TTY = serial.Serial(self.DEVICE, baud)

    def send_single(self, char):
        self.tx_buffer.append(KEYS[char])

    def send_multiple(self, presses):
        for char in presses:
            self.tx_buffer.append(KEYS[char])

    async def main_loop(self):
        data = b''
        while self.TTY.inWaiting() == 0:
            data = b''
            while len(self.tx_buffer) > 0:
                self.TTY.write(self.tx_buffer[0])
                self.tx_buffer.pop(0)
                self.TTY.flush()
                await asyncio.sleep(.2)
            await asyncio.sleep(.2)
        while self.TTY.inWaiting() > 0:
            data += self.TTY.read(1)
            if data in KEY_LIST:
                print(f'ECHO - ', end='')
                print(data)
                data = b''
        if data != b'':
            self.parse_data(data)

    def setRTS(self, enable=True):
        self.isRTS = enable
        self.TTY.setRTS(enable)

    def setPTT(self, enable=True):
        self.setRTS(enable)


if __name__ == "__main__":
    import argparse
#    from time import sleep
    radio = RT95()
#    radio.setRTS(True)
#    sleep(1)
#    radio.setRTS(False)
#    sleep(1)

    # create a parser
    parser = argparse.ArgumentParser()
    # -----------Create Arguments -----------------------
    # Without a '-' it is a must-have
    parser.add_argument('keypresses', help='A string of keypresses', type=str)
    # With a '-' it is optional
    parser.add_argument('-d', '--device', help='Set the device. Default is "/"dev/ttyUSB0"',
                        type=str, default='/dev/ttyUSB0')
    # -------------- End Arguments -----------------------

    args = parser.parse_args()
    print(args.device)
    if args.keyresses in KEYS.keys():   
        radio.send_single(args.keypresses)
    else:
        for l in args.keypresses:
            if l in KEYS.keys():
                pass
            else:
                print(f"ERROR invalid key: {l}")
                exit()
        radio.send_multiple(args.keypresses)
