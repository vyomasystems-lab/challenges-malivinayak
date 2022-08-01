# See LICENSE.vyoma for details
# SPDX-License-Identifier: CC0-1.0

from os import system, name
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

import detect_seq

def clear():
   # for windows
   if name == 'nt':
    _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')


@cocotb.test()
async def test_seq_bug(dut):
    
    clear()

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    # Test Cases
    s1 = "1011"
    s2 = "11011"
    s3 = "1101011"
    s4 = "11010110110111011"

    # Assiging a testcase to find bug
    sequence = s4

    # Execution
    print("\n0. Sequence : " + sequence)
    print("1. Sequence bit\t\t\t", end = ' ')
    for i in range(0, len(sequence)):
        print( sequence[i] , end = ' ')
    print()  

    print("2. Expected Seq_detection\t", end = ' ')
    c_state = 0
    for i in range(0, len(sequence)):
        c_state = detect_seq.detect_sequence(sequence[i],c_state)
        print( "1" if c_state == 4 else "0" , end = ' ')    
    print()  
    
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    print("3. Output Seq_detection\t\t", end = ' ')
    for i in range(0, len(sequence)):
        c_state = detect_seq.detect_sequence(sequence[i],c_state)
        if(sequence[i] == '1'):
            dut.inp_bit.value = 1
        else:
            dut.inp_bit.value = 0
        await FallingEdge(dut.clk)
        from_verilog = dut.seq_seen.value
        print(str(from_verilog), end = ' ')
        check = '1' if c_state == 4 else '0'
        assert (str(from_verilog) == check) , '\nBug Detected:\n1. input \t\t\t: '+ sequence + "\n2. Current State\t\t: "+ str(c_state) + "\n3. Output from Verilog is \t: " + str(from_verilog) + "\n4. Expected Output  \t: " + "1" if c_state == 4 else "0" 
    print()
