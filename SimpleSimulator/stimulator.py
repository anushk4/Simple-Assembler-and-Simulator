
import sys
from parameters2 import opcode2,registers2

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
        
def binary_actual_r(a):   # binary to actual register
    for x,y in registers2.items():
        if x==a:
            return y
      
def decimal_binary(n):  
    x=bin(n).replace("0b","")
    return x.zfill(16)

def binary_decimal(n):    
    x=int(n,2)
    return x

def decimal_binary_pc(k):
    y=bin(k).replace("0b","")  
    return y.zfill(7)

#Type A instructions
def add_op(inst,pc):
    out=""
    count=decimal_binary_pc(pc)
    destination=binary_actual_r(inst[7:10])
    print(destination)
    source_1=binary_actual_r(inst[10:13])
    print(source_1)
    source_2=binary_actual_r(inst[13:16])
    print(source_2)
    d_source_1=binary_decimal(inst[10:13])
    d_source_2=binary_decimal(inst[13:16])
    r_values[source_1]=decimal_binary(d_source_1)
    r_values[source_2]=decimal_binary(d_source_2)
    sum=d_source_1+d_source_2
    if sum>((2**16)-1):
        print("Overflow")
        #overflow condition
    else:
        r_values[destination]=decimal_binary(sum)
        out=count
        for y in r_values.values():
            out+=" "
            out+=y  
        return out


# def sub_op():

# def mul_op():

# def xor_op():

# def or_op():

# def and_op():



# Main function
for line in f:
    inst=line.rstrip("\n")
    result=binary_actual_op(inst[0:5])
    if result=="add":
        final_result=add_op(inst,pc)
        pc+=1
        print(final_result)

    










f.close()





