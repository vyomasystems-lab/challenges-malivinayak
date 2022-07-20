#!/bin/bash

export PS1='\[\033[01;32m\]vyoma\[\033[00m\] \[\033[01;34m\]\w\[\033[00m\] (uptickpro) $ '
brew install icarus-verilog
PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.8.10
pyenv global 3.8.10
pip install --upgrade pip
pip install cocotb
clear
echo "****** UpTickPro (Evaluation Version) 1.0.0 *******"
echo "Copyright (c) 2022, Vyoma Systems Private Limited"
echo "All Rights Reserved."
