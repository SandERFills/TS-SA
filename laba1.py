matrix=[[20,25,15],[25,24,10],[15,28,12],[9,30,20]] #work matrix
array_buff,array_y,risc=[],[],[]
i=0                                                 #cycle iterator
for x in range(len(matrix[i])):                     #in lenght of line in array

    for y in range(len(matrix)):                    #in matrix lenght
        # array_buff=matrix[x]
        # if x>y:
        #     continue
        array_y.append(matrix[y][i])                #add in buffer first elemnts 
    risc.append(array_y[:])                         #copies in risc array
    array_y.clear()
    i=+1
