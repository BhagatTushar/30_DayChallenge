array1 = input("Enter array : ")
if len(array1)%2==1:
    if len(array1) == 1:
        print("Only 1 letter : ",array1)
    else:
        x = int((len(array1)-1) / 2)
        answer = array1[x]
        print(answer)

else:
    print("can't find middle value string is even ")