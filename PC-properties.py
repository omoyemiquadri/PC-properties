# A python program to Find all your Laptop properties.
import os,platform
import time

print("This is your PC properties below: ")
print("")
print('Operating system name: ', os.name)
print('Platform name        : ',platform.system())
print('This Laptop Processor: ',platform.processor())
print('Laptop Machine type  : ',platform.machine())
print('This Laptop Version  : ',platform.version())
print('This Laptop Username : ',platform.node())
print('')
print('')
print('')
print('Compile by: Horla_Barnabas')

time.sleep(20)
