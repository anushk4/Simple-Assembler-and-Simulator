
import sys
from parameters2 import opcode2,registers2
# import os


# current_dir = os.getcwd()
# file_path = os.path.join(current_dir, 'stdin.txt')
# print(file_path)

f=open("stdin.txt","r")

r_values={
    "R0":"0"*16,
    "R1":"0"*16,
    "R2":"0"*16,
    "R3":"0"*16,
    "R4":"0"*16,
    "R5":"0"*16,
    "R6":"0"*16,
    "FLAGS":"0"*16
}
pc=0
halted=False

def binary_actual_op(b):  # binary to actual opcode
    for x,y in opcode2.items():
        if x==b:
            return y
        
def binary_actual_r(a):   #binary to actual register
    for x,y in registers2.items():
        if x==a:
            return y
      
def binary_decimal(n):    #binary to decimal
    return bin(n).replace("0b","")

def decimal_binary(n):    #decimal to binary
    x=int(n,2)
    return x.zfill(8)


#Type A instructions
# def add_inst():

# def sub_inst():

# def mul_inst():

# def xor_inst():

# def or_inst():

# def and_inst():
for line in f:
    inst=line
    print(inst)
    print("\n")

f.close()





