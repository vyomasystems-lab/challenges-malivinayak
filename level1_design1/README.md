# Level-1 Design-1

**Note - For Better Experience click on image**

## Bugs

### 1. Select Case ```5'b01100``` is misssing
Case ```5'b01100``` is not present due to which outpin for case ```5'b01100``` takes ```default value```.

| | |
| :--: | :--: |
| Python Test and Terminal | Bug in verilog |
| <p align="left"> <img src="https://user-images.githubusercontent.com/66154908/180635808-bcd67bbc-8ca0-4b33-a601-3cb169258879.png" alt="Bug Screenshot with Python test" /> | <img src="https://user-images.githubusercontent.com/66154908/180635840-a2cfc6d3-3609-4391-9f65-1d04f046bce0.png"/> | 
 
### 2. Select Case ```5'b01101``` is Unreachable
Case ```5'b01101``` is appeared twice for ```inp12``` and ```inp13```, due to this ```inp13``` is unreachable. Beacuse the ```first case``` which match with ```5'b01101``` is assigned for output i.e. ```inp12```
| | |
| :--: | :--: |
| Python Test and Terminal | Bug in verilog |
| <p align="left"> <img src="https://user-images.githubusercontent.com/66154908/180636516-2f2b55a3-2cb3-4d4b-8e99-053e982a79c3.png" alt="Bug Screenshot with Python test" /> | <img src="https://user-images.githubusercontent.com/66154908/180636340-05ca9fe0-1ef2-4be4-b507-f16ce625f253.png"/> | 

### 3. Select Case ```5'b01110``` is misssing
Case ```5'b01110``` is not present due to which outpin for case ```5'b01110``` takes ```default value```.

| | |
| :--: | :--: |
| Python Test and Terminal | Bug in verilog |
| <p align="left"> <img src="https://user-images.githubusercontent.com/66154908/180636645-9940f05e-f1a5-4ed6-9f32-1afa88a70321.png" alt="Bug Screenshot with Python test" /> | <img src="https://user-images.githubusercontent.com/66154908/180636655-6cc3134f-2bd0-4082-a8f7-a38520a225c9.png"/> | 
 
