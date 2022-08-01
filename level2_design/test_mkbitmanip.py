# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *
from os import system, name

def clear():
   # for windows
   if name == 'nt':
    _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    instr = {}
    instr[0] = 0b01100000000000000101000000110011
    instr[1] = 0b01000000000000000111000000110011
    instr[2] = 0b01000000000000000110000000110011
    instr[3] = 0b01000000000000000100000000110011
    instr[4] = 0b00100000000000000001000000110011
    instr[5] = 0b00100000000000000101000000110011
    instr[6] = 0b01100000000000000001000000110011
    instr[7] = 0b00100000000000000010000000110011
    instr[8] = 0b00100000000000000100000000110011
    instr[9] = 0b00100000000000000110000000110011
    instr[10] = 0b01001000000000000001000000110011
    instr[11] = 0b00101000000000000001000000110011
    instr[12] = 0b01101000000000000001000000110011
    instr[13] = 0b01001000000000000101000000110011
    instr[14] = 0b00101000000000000101000000110011
    instr[15] = 0b01101000000000000101000000110011
    instr[16] = 0b01100000000000000001000000010011
    instr[17] = 0b01100000000100000001000000010011
    instr[18] = 0b01100000001000000001000000010011
    instr[19] = 0b01100000010000000001000000010011
    instr[20] = 0b01100000010111111001111110010011
    instr[21] = 0b01100001000000000001000000010011
    instr[22] = 0b01100001000100000001000000010011
    instr[23] = 0b01100001001000000001000000010011
    instr[24] = 0b01100001100000000001000000010011
    instr[25] = 0b01100001100100000001000000010011
    instr[26] = 0b01100001101000000001000000010011
    instr[27] = 0b00001010000000000001000000110011
    instr[28] = 0b00001010000000000011000000110011
    instr[29] = 0b00001010000000000010000000110011
    instr[30] = 0b00001010000000000100000000110011
    instr[31] = 0b00001010000000000101000000110011
    instr[32] = 0b00001010000000000110000000110011
    instr[33] = 0b00001010000000000111000000110011
    instr[34] = 0b01001000000000000110000000110011
    instr[35] = 0b00001000000000000110000000110011
    instr[36] = 0b00001000000000000100000000110011
    instr[37] = 0b01001000000000000100000000110011
    instr[38] = 0b00001000000000000111000000110011
    instr[39] = 0b00100000000100000101000000010011
    instr[40] = 0b01100000000100000101000000010011
    instr[41] = 0b001000000000000001000000010011
    instr[42] = 0b010010000000000001000000010011
    instr[43] = 0b001010000000000001000000010011
    instr[44] = 0b011010000000000001000000010011
    instr[45] = 0b010010000000000101000000010011
    instr[46] = 0b0000100000000000001000000010011
    instr[47] = 0b0000100000000000101000000010011
    instr[48] = 0b00001000000000000001000000110011
    instr[49] = 0b00001000000000000101000000110011
    instr[50] = 0b00101000000100000101000000010011
    instr[51] = 0b01101000000100000101000000010011
    instr[52] = 0b00000100000000000101000000010011 
    instr[53] = 0b01001000000000000111000000110011 
    instr[54] = 0b00000110000000000001000000110011
    instr[55] = 0b00000110000000000101000000110011
    instr[56] = 0b00000100000000000001000000110011
    instr[57] = 0b00000100000000000101000000110011
    instr[58] = 0b11000000000000000001000000110011
    instr[59] = 0b11000000000000000101000000110011
    instr[60] = 0b10000000000000000001000000110011
    instr[61] = 0b10000000000000000101000000110011
    instr[62] = 0b00000000000000000110000000110011
    instr[63] = 0b00000000000000000111000000110011
    
    for no in range(len(instr)):
        # clock
        cocotb.fork(clock_gen(dut.CLK))

        # reset
        dut.RST_N.value <= 0
        yield Timer(10) 
        dut.RST_N.value <= 1

        ######### CTB : Modify the test to expose the bug #############
        # input transaction
        mav_putvalue_src1 = 0x5
        mav_putvalue_src2 = 0x0
        mav_putvalue_src3 = 0x0
        mav_putvalue_instr = instr[no]

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
    
        yield Timer(1) 
        print("src_1 - " + str(dut.mav_putvalue_src1.value))
        print("src_2 - " + str(dut.mav_putvalue_src2.value))
        print("src_3 - " + str(dut.mav_putvalue_src3.value))
        print("Instruction - " + str(dut.mav_putvalue_instr.value)+ "\nInstruction Number - "+str(no))

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message + "\nBug Detected for Instruction : " + str(dut.mav_putvalue_instr.value)
