# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    print('\nExecution of Python Verification')
    # Initialize signal
    sel = dut.sel
    sel.value = 3
    for i in range(31):
        # print("dut.inp%d.value = %d" % (i,i))
        exec("dut.inp%d.value = %d" % (i,i))
    await Timer(1, "ns")
    print(sel.value)
    await Timer(1, "ns")
    print(dut.inp4)
    print('\nCompletion of Python Verification\n')
    cocotb.log.info('##### CTB: Develop your test here ########')
