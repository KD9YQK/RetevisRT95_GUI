import serial
from time import sleep
import pickle

DEVICE = '/dev/ttyUSB0'

TTY = serial.Serial(DEVICE, 9600)


def pickle_save(data, file):
    with open(file, 'wb') as f:  # open a text file
        pickle.dump(data, f)  # serialize the list
        f.close()


def read_serial():
    data = b''
    while TTY.inWaiting() == 0:
        # sleep(.5)
        pass
    while TTY.inWaiting() > 0:
        data += TTY.read(1)
    print(data)
    return data


if __name__ == "__main__":
    mic_data = {}
    print('Press the buttons as they appear to record serial data')

    for i in range(0, 10):
        print(f'{str(i)}> ', end='')
        mic_data[str(i)] = read_serial()
        sleep(1)

    print('*> ', end='')
    mic_data['Star'] = read_serial()
    sleep(1)
    print('#> ', end='')
    mic_data['Pound'] = read_serial()
    sleep(1)
    print('AB> ', end='')
    mic_data['AB'] = read_serial()
    sleep(1)

    for i in range(1, 5):
        print(f'User{i}> ', end='')
        mic_data[f'User{i}'] = read_serial()
        sleep(1)

    print('TX(Hold Down)> ', end='')
    mic_data['TXdown'] = read_serial()
    sleep(1)
    print('TX(Release)> ', end='')
    mic_data['TXup'] = read_serial()
    sleep(1)

    pickle_save(mic_data, "mic.dat")
    print('Mic recording complete.')
    TTY.close()
