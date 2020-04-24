import SI1145.SI1145 as SI1145 # https://github.com/THP-JOE/Python_SI1145.git
from datetime import datetime
sensor = SI1145.SI1145()

vis = str(sensor.readVisible())
ir = str(sensor.readIR())
uv = str(sensor.readUV())

try:
    f = open("/home/pi/home-automation/si1145.txt", "x")
    f.write("date" + "\t" + "time" + "\t" + "vis" + "\t" + "ir" + "\t" + "uv" + "\n")
    f.close()
except:
    pass

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

f = open("/home/pi/home-automation/si1145.txt", "a+")
f.write(date + "\t" + time + "\t" + vis + "\t" + ir + "\t" + uv + "\n")
f.close()
