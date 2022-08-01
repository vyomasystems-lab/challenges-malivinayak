# i_bit - Input bit
# c_state - current state

def detect_sequence(i_bit, c_state):
    if(c_state == 0):
        if(i_bit == '0'):
            return 0
        else:
            return 1
    elif(c_state == 1):
        if(i_bit == '0'):
            return 2
        else:
            return 1
    elif(c_state == 2):
        if(i_bit == '0'):
            return 0
        else:
            return 3
    elif(c_state == 3):
        if(i_bit == '0'):
            return 2
        else:
            return 4
    elif(c_state == 4):
        if(i_bit == '0'):
            return 2
        else:
            return 1
