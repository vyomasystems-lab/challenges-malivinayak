# Level-1 Design-1

## Bugs

### 1. Case 5'b01100 is misssing

| | |
| :--: | :--: |
| `Python Test and Terminal` | `Bug in verilog ` |
| <p align="left"> <img src="https://user-images.githubusercontent.com/66154908/180635808-bcd67bbc-8ca0-4b33-a601-3cb169258879.png" alt="Bug Screenshot with Python test" /> | <img src="https://user-images.githubusercontent.com/66154908/180635840-a2cfc6d3-3609-4391-9f65-1d04f046bce0.png"/> | 
 
### 1. Case 5'b01101 is Unreachable
Case ```5'b01101``` is appear twice for ```inp12``` and ```inp13```, due to this ```inp13``` is unreachable when ```inp12 = 0```. Beacuse the ```first case which match with 5'b01101 is assigned for output i.e. inp12```
| | |
| :--: | :--: |
| `Python Test and Terminal` | `Bug in verilog ` |
| <p align="left"> <img src="" alt="Bug Screenshot with Python test" /> | <img src=""/> | 
 