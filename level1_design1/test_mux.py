# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
from random import randrange

# Base Test Case
@cocotb.test()
async def test_mux(dut):
    print('\nExecution of Python Verification')
    
    dict = {}                                           # Creating dict dictonary for accesing all inp
    for i in range(31):
        dict[i] = "dut.inp"+ str(i) + ".value"
    test = randrange(31)                                # Taking Random select pin
    dut.sel.value = test                                # Assigning out
    await Timer(1, "ns")
    for i in range(31):                                 #  Assigning inp0 to inp30
        exec("dut.inp%d.value = %d" % (i,i%4))
    await Timer(2, "ns")
    print("Select Value - %d" % dut.sel.value)          # Checking select pin value
    print("Out Value - %d" % dut.out.value)             # Checking out pin value
    print("Respective inp pin value in binary : ")
    print(eval(dict[test]))
    assert dut.out.value == eval(dict[test]), 'MUX is not working'      # Base test case

    print('\nCompletion of Python Verification\n')
    cocotb.log.info('##### CTB: Develop your test here ########')
