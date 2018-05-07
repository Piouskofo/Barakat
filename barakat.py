
x = int(input("what is your grade"))
#check grade
#70-100=A
#69-60 =B
#59-50 =C
#49-40 =D
#39-30 =E
#29-20 =F

 #and or are used for comparism
if (x >=70 and x <= 100):
    print("you scored A")
elif(x<=69 and x>=60):
    print("you score B")
elif(x<=59 and x>50):
    print("you score C")
elif(x<=49 and x>=40):
    print("you score D")
elif(x<=39 and x>=30):
    print("you score E")
elif(x<=29 and x>=20):
     print("you score F")
else:
     print("pls go and read your score is below average")
