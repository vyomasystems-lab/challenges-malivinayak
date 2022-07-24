# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from random import randrange

@cocotb.test()
async def test_mux(dut):
    dict = {}                                                   # Creating dict dictonary for accesing all inp
    for i in range(31):
        dict[i] = "dut.inp"+ str(i) + ".value"
    
    for i in range(31):                                 
        exec("dut.inp%d.value = %d" % (i,randrange(4)))        #  Assigning inp0 to inp30
        dut.sel.value = i                                      # Assigning out
        await Timer(1, "ns")
        if(dut.out.value != eval(dict[i])):
            print("\nSelect Value - %d" % dut.sel.value)       # Checking select pin value
            print("Out Value - %d" % dut.out.value)            # Checking out pin value
            print("Respective inp pin value in binary : " + dict[i]+"\n")
            raise TestFailure("Failure!")
    print('\nCompletion of Python Basic Testcase Verification\n')
