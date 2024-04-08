import serial
from time import sleep
import pickle

DEVICE = '/dev/ttyUSB0'
MON = 1 #If MON is set to User then use 1-4 otherwise use 0
# MON = 0

TTY = serial.Serial(DEVICE, 9600)
TTY.setRTS(False)

def pickle_save(data, file):
    with open(file, 'wb') as f:  # open a text file
        pickle.dump(data, f)  # serialize the list
        f.close()

# This code works but not gonna use it. readline() works better.
# AB or User1-4 with MONITOR will open squelch, which collects a bunch of garbage data.
def read_serial():
    data = b''
    while TTY.inWaiting() == 0:
        sleep(.5) # This is required to allow time for buffer to collect data.
        pass
    while TTY.inWaiting() > 0:
        data += TTY.read(1)
    print(data)
    return data


if __name__ == "__main__":
    mic_data = {}
    print('Press the buttons as they appear to record serial data')
    print('Make sure VFO is enabled, and you are on empty frequencies on both VFO-A and VFO-B')
    print('Unplug the Mic, but NOT the radio. Hit Enter to start')
    print('')

    print('Plug in Mic')
    mic_data['Plug'] = TTY.readline()
    read_sleep() # Grab the returned data
    sleep(1)

    for i in range(0, 10):
        print(f'Button {str(i)}> ')
        mic_data[str(i)] = TTY.readline()
        sleep(1)

    print('Button *> ')
    mic_data['Star'] = TTY.readline()
    sleep(1)
    print('Button #> ')
    mic_data['Pound'] = TTY.readline()
    sleep(1)
    print('Button AB> ')
    mic_data['AB'] = TTY.readline()
    read_serial() # Grab the returned data
    sleep(1)

    for i in range(1, 5):
        print(f'User{i}> ')
        mic_data[f'User{i}'] = TTY.readline()
        if i == MON:
            read_serial() # Grab the returned data
        sleep(1)
# TODO Figure out what the data is that is being sent, and where it is coming from, the radio or the mic.
#    print('TX(Hold Down)> ')
#    mic_data['TXdown'] = read_serial()
#    sleep(1)
#    print('TX(Release)> ')
#    mic_data['TXup'] = read_serial()
#    sleep(1)

    pickle_save(mic_data, "mic.dat")
    print('Mic recording complete.')
    print(mic_data)
    TTY.close()
