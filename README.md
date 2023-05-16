# Assembler
The [Simple-Assembler](https://en.wikipedia.org/wiki/Assembly_language) is the first part of the project assigned under the Computer Organisation (CSE112) course. It consists of 2 files:

## parameters.py 
The file consists of all the parameters being used. It consists of 3 dictionaries:

- registers: which consists of registers (which are not case-sensitive) names and their addresses.

- opcode: which consists of instructions and their opcodes.

- type: which includes instructions and their type.

## assembler.py
The file contains the main code which includes:

- Functions for the binary encoding of the types A to F.

- Functions for checking the errors which consists of any kind of syntax errors and all the error handling cases mentioned in the comments of the file.

- Finally the code in the `main` section which reads the input from `stdin` into machine code according to types, opcodes and instructions in `parameters.py` file and displays it in `stdout`.

### Running the file
To run the file, clone the repository in the device and navigate to the automatedTesting folder after making all run files executable.

To run the Assembler, run the following command on Linux:
```
./run --no-sim
```