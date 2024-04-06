import serial
import pickle
from time import sleep


def pickle_load(file):
    try:
        with open(file, 'rb') as f:
            retval = pickle.load(f)  # deserialize using load()
            f.close()
        return retval
    except FileExistsError:
        print(f"ERROR - {file} not found! Run 'python3 mic_send.py' to create.")
        exit()


class rt95:
    DEVICE = "/dev/ttyUSB0"
    TTY: serial.Serial
    MIC_DATA = {}

    def __init__(self, device="/dev/ttyUSB0", baud=9600, dat_file="mic.dat"):
        self.DEVICE = device
        self.MIC_DATA = pickle_load(dat_file)
        self.TTY = serial.Serial(self.DEVICE, baud)

    def send_single(self, char):
        self.TTY.write(self.MIC_DATA[char])

    def send_multiple(self, presses):
        for char in presses:
            self.TTY.write(self.MIC_DATA[char])
            sleep(.1)

    def read_serial(self):
        data = b''
        while self.TTY.inWaiting() == 0:
            # sleep(.5)
            pass
        while self.TTY.inWaiting() > 0:
            data += self.TTY.read(1)
        print(data)
        return data
    
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
