# See LICENSE.vyoma for details
# SPDX-License-Identifier: CC0-1.0

from os import system, name
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)
    
    print(dut.light_LS.value)
    print(dut.light_RB.value)
    print(dut.light_LR.value)
    print(dut.light_BR.value)
    print()

    for i in range(6):
        print(dut.ps.value) 
        await FallingEdge(dut.clk)
        assert dut.ps.value == 0, "\nBug Detected\nSignal State must be S0"
        assert dut.light_LS.value == 1, "light_LS state must be 001"
        
    for i in range(3):
        print(dut.ps.value) 
        await FallingEdge(dut.clk)
        assert dut.ps.value == 1, "\nBug Detected\nSignal State must be S0"
        
    for i in range(5):
        print(dut.ps.value) 
        await FallingEdge(dut.clk)
        assert dut.ps.value == 2, "\nBug Detected\nSignal State must be S0"

    print(dut.ps.value)