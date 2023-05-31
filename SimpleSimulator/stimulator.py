
import sys
from parameters2 import opcode2,registers2

# def binary_actual_op(b):  # binary to actual opcode
#     for x,y in opcode2.items():
#         if x==b:
#             return y

def get_registers_A(inst):
    return registers2[inst[7:10]],registers2[inst[10:13]],registers2[inst[13:16]]

def get_registers_B(inst):
    return registers2[inst[6:9]],inst[9:16].zfill(16)

def get_registers_D(inst):
    return registers2[inst[6:9]],binary_decimal(inst[9:16])

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
    destination,source_1,source_2=get_registers_A(inst)
    d_source_1=binary_decimal(r_values[source_1])
    d_source_2=binary_decimal(r_values[source_2])
    final=d_source_1+d_source_2
    if not (final >= 0 and final<=((2**16)-1)):
        final=0
        r_values["FLAGS"]=flag_overflow
    r_values[destination]=decimal_binary(final)
    out=count
    for y in r_values.values():
        out+=" "
        out+=y  
    return out

def sub_op(inst,pc):
    out=""
    count=decimal_binary_pc(pc)
    destination,source_1,source_2=get_registers_A(inst)
    d_source_1=binary_decimal(r_values[source_1])
    d_source_2=binary_decimal(r_values[source_2])
    final=d_source_1-d_source_2
    if not (final >= 0 and final<=((2**16)-1)):
        final=0
        r_values["FLAGS"]=flag_overflow
    r_values[destination]=decimal_binary(final)
    out=count
    for y in r_values.values():
        out+=" "
        out+=y  
    return out

def mul_op(inst,pc):
    out=""
    count=decimal_binary_pc(pc)
    destination,source_1,source_2=get_registers_A(inst)
    d_source_1=binary_decimal(r_values[source_1])
    d_source_2=binary_decimal(r_values[source_2])
    final=d_source_1*d_source_2
    if not (final >= 0 and final<=((2**16)-1)):
        final=0
        r_values["FLAGS"]=flag_overflow
    r_values[destination]=decimal_binary(final)
    out=count
    for y in r_values.values():
        out+=" "
        out+=y  
    return out

def xor_op(inst,pc):
    out=""
    count=decimal_binary_pc(pc)
    destination,source_1,source_2=get_registers_A(inst)
    d_source_1=r_values[source_1]
    d_source_2=r_values[source_2]
    final=d_source_1^d_source_2
    r_values[destination]=final
    out=count
    for y in r_values.values():
        out+=" "
        out+=y  
    return out

def or_op(inst,pc):
    out=""
    count=decimal_binary_pc(pc)
    destination,source_1,source_2=get_registers_A(inst)
    d_source_1=r_values[source_1]
    d_source_2=r_values[source_2]
    final=d_source_1|d_source_2
    r_values[destination]=final
    out=count
    for y in r_values.values():
        out+=" "
        out+=y  
    return out

def and_op(inst,pc):
    out=""
    count=decimal_binary_pc(pc)
    destination,source_1,source_2=get_registers_A(inst)
    d_source_1=inst[10:13].zfill(16)
    d_source_2=inst[13:16].zfill(16)
    r_values[source_1]=d_source_1
    r_values[source_2]=d_source_2
    final=d_source_1&d_source_2
    r_values[destination]=final
    out=count
    for y in r_values.values():
        out+=" "
        out+=y  
    return out

# Type B instructions

def mov_imm_op(inst, pc):
    out = ""
    count = decimal_binary_pc(pc)
    destination,immediate_value=get_registers_B(inst)
    r_values[destination] = immediate_value
    out = count
    for y in r_values.values():
        out += " "
        out += y
    return out

# Type C instruction

def mov_reg_op(inst, pc):
    out = ""
    count = decimal_binary_pc(pc)
    destination = binary_actual_r(inst[7:10])
    source = binary_actual_r(inst[10:13])
    r_values[destination] = r_values[source]
    out = count
    for y in r_values.values():
        out += " "
        out += y
    return out


# Type D instruction

def ld_op(inst, pc):
    out = ""
    count = decimal_binary_pc(pc)
    # destination = binary_actual_r(inst[7:10])
    # memory_address = binary_actual_r(inst[10:13])
    destination,memory_address=get_registers_D(inst)
    r_values[destination] = memory[memory_address]
    out = count
    for y in r_values.values():
        out += " "
        out += y
    return out

def st_op(inst, pc):
    out = ""
    count = decimal_binary_pc(pc)
    # source = binary_actual_r(inst[7:10])
    # memory_address = binary_actual_r(inst[10:13])
    source,memory_address=get_registers_D(inst)
    memory[memory_address] = r_values[source]
    out = count
    for y in r_values.values():
        out += " "
        out += y
    return out

# Main function

#input for testing
 
f=open("stdin.txt","r")

# lines = []

# actual input

# while True:
#     line = sys.stdin.readline().strip()
#     if not line:
#         break
#     lines.append(line)

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

k=0
file_instructions={}
memory=["0"*16]*128
pointers=[]
for i in f:
    pointer=bin(k)[2:].zfill(7)
    pointers.append(pointer)
    file_instructions[pointer]=i.rstrip("\n")
    memory[k]=file_instructions[pointer]
    k+=1

pc=0
halted=False

#Flag initialisation
flag_overflow="0"*12+"1000"
flag_less_than="0"*12+"0100"
flag_greater_than="0"*12+"0010"
flag_equal="0"*12+"0001"

i=0
inst=file_instructions[pointers[i]]
while not halted:
    op_code=inst[0:5]
    if op_code=="0"*5:
        final_result=add_op(inst,pc)
        print(final_result)
    elif op_code=="00001":
        final_result=sub_op(inst,pc)
        print(final_result)
    elif op_code=="00110":
        final_result=mul_op(inst,pc)
        print(final_result)
    elif op_code=="01010":
        final_result=xor_op(inst,pc)
        print(final_result)
    elif op_code=="01011":
        final_result=or_op(inst,pc)
        print(final_result)
    elif op_code=="01100":
        final_result=and_op(inst,pc)
        print(final_result)
    elif op_code=="00010":
        final_result=mov_imm_op(inst,pc)
        print(final_result)
    elif op_code=="00100":
        final_result=ld_op(inst,pc)
        print(final_result)
    elif op_code=="00101":
        final_result=st_op(inst,pc)
        print(final_result)
    elif op_code=="11010":
        halted=True
        break
    if op_code not in ["11100","11101","01111","11111"]:
        i+=1
        inst=file_instructions[pointers[i]]
    pc+=1
for i in memory:
    print(i)  
f.close()