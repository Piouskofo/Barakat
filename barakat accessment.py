num = 0

while(num<100):
    num+=1
    if(num%3==0 and num%5==0):
        print("fuzzBuzz")
    
    elif(num%3==0):
        print("fizz")
    elif(num%4==0):
        print("Tetra")
    else:
        print(num)
    
    
