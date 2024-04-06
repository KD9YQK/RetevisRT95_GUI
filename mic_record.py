import serial
from time import sleep
import pickle

DEVICE = '/dev/ttyUSB0'


def pickle_save(data, file):
    with open(file, 'wb') as f:  # open a text file
        pickle.dump(data, f)  # serialize the list
        f.close()


def read_serial(tty: serial.Serial):
    while True:
        bytesToRead = tty.inWaiting()
        data = ser.read(bytesToRead)
        if data is not None:
            break
    print(data)
    return data


if __name__ == "__main__":
    mic_data = {}
    ser = serial.Serial(DEVICE, 9600)
    print('Press the buttons as they appear to record serial data')

    for i in range(0, 10):
        print(f'{str(i)}> ', end='')
        mic_data[str(i)] = read_serial(ser)
        sleep(1)

    print('*> ', end='')
    mic_data['Star'] = read_serial(ser)
    sleep(1)
    print('#> ', end='')
    mic_data['Pound'] = read_serial(ser)
    sleep(1)
    print('AB> ', end='')
    mic_data['AB'] = read_serial(ser)
    sleep(1)

    for i in range(1, 5):
        print(f'User{i}> ', end='')
        mic_data[f'User{i}'] = read_serial(ser)
        sleep(1)

    print('TX(Hold Down)> ', end='')
    mic_data['TXdown'] = read_serial(ser)
    sleep(1)
    print('TX(Release)> ', end='')
    mic_data['TXup'] = read_serial(ser)
    sleep(1)

    pickle_save(mic_data, "mic.dat")
    print('Mic recording complete.')
