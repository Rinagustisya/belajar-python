row, col = 5, 5
for i in range (col*2):
    val = 1
    prev_val = 0 
    for j in range(col-row):
        print(' ', end='')
    for j in range (row*2):
        if(j < row):
            print(val, end ='')
            temp = val
            val = val + prev_val
            prev_val = temp
        else :
            print(prev_val, end='')
            temp = prev_val
            prev_val= val- prev_val
            val = temp
    
    temp= row
    row = row - 1
    if (i > (col -2)):
        row = i -(col -2)
    print()