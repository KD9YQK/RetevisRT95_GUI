import serial
import serial.threaded

class SerialReader(serial.threaded.Protocol):
    def __init__(self):
        self.buffer = bytearray()

    def data_received(self, data):
       self.buffer.extend(data)
        if b'\n' in self.buffer:
            lines = self.buffer.split(b'\n')
            self.buffer = bytearray()
            for line in lines[:-1]:
                print(line.decode('ascii'))

ser = serial.Serial('/dev/ttyUSB0', 9600)
with serial.threaded.ReaderThread(ser, SerialReader) as protocol:
    ## The ReaderThread will automatically call the data_received method when data is received
    ## You can perform other tasks here while the ReaderThread handles incoming data
    time.sleep(10)  ## Example: wait for 10 seconds before exiting
