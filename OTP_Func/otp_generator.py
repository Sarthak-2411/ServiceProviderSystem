
import random
import math

data = '0123456789'
leng = len(data)

def generate_otp():
    global otp
    i=4
    otp=""
    while(i>0):
        otp += data[math.floor(random.random()*leng)]
        i-=1
    return otp