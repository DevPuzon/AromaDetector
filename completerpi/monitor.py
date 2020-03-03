
import serial
serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate) 
ser = serial.Serial(serial_port, baud_rate)

while True:
    arduinodata = ser.readline();
    arduinodata = arduinodata.decode("utf-8")
    print("----------")
    print(arduinodata)