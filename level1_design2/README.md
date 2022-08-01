# Level-1 Design-2

**Note - For Better Experience click on image**

## Bugs

### 0. Without Overlapping Basic Sequence ```1011```
The Verloig Code works well with without overlapping sequence. When overlapping sequence occur verilog code fail to detect the sequence in particular cases

<p align="center">
<img src="https://user-images.githubusercontent.com/66154908/182136103-f3f4e4ef-796d-4bc1-a733-22645d9c55fe.png"/>
</p>

### 1. State ```SEQ_1```
When bit 1 is arrived on SEQ_1 then State SEQ_1 is reseting the state, Due to which Overlapping sequence is not detected. <br>
```SEQ_1 -> 1 -> SEQ_1``` (Remain on current state only)

| | |
| :--: | :--: |
| Bug Detected | Bug Fixed |
| <p align="center"> <img src="https://user-images.githubusercontent.com/66154908/182137351-84f1f655-8535-4554-a88f-37ec04a2a267.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/66154908/182137633-08480f12-bcab-4c51-b35d-8c14ead998ba.png"/> | 
 
 ### 2. State ```SEQ_101```
When bit 0 is arrived on SEQ_101 then State SEQ_101 is reseting the state to IDLE state, Due to which Overlapping sequence is not detected. <br>
```SEQ_101 -> 0 -> SEQ_10```

| | |
| :--: | :--: |
| Bug Detected | Bug Fixed |
| <p align="center"> <img src="https://user-images.githubusercontent.com/66154908/182139492-8d2c21e3-b208-4537-b666-46b359964b79.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/66154908/182139974-fd3fc7dd-1268-4e55-9886-38cb89a2dde0.png"/> | 
 
 ### 3. State ```SEQ_1011```
When bit ```0 or 1``` is arrived on SEQ_1011 then State SEQ_1011 is reseting the state to IDLE state, Due to which Overlapping sequence is not detected. <br>
```SEQ_1011 -> 0 -> SEQ_10``` <br>
```SEQ_1011 -> 1 -> SEQ_1```

| | |
| :--: | :--: |
| Bug Detected | Bug Fixed |
| <p align="center"> <img src="https://user-images.githubusercontent.com/66154908/182141577-5fc73aa4-eaa9-40a8-933c-398d0027d01e.png" /> | <p align="center"> <img src="https://user-images.githubusercontent.com/66154908/182140878-17120344-1a32-4d3f-8760-783bb9be6e5c.png"/> | 
 
