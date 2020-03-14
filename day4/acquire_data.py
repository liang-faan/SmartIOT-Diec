#
# Acquires data from micro:bit using serial IO
# Author: Lisa Ong, NUS/ISS
#

# import helper classes for acquiring data from the Micro:bit
import serialio

# comport = 'COM3' # Example Windows port
comport = '/dev/tty.usbmodem14102' # Example MacOS port
# /dev/tty.usbmodem14102

baudrate = 115200
output_file = 'data1.csv'

def SerialIoToFile_Factory():
    return serialio.SerialIoToFile(output_file)

serialio.run_loop_forever(comport, baudrate, SerialIoToFile_Factory)
