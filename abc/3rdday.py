#l = [1,3,9]
#l1 = []
#for i in l: 
 #    l1.append(i**2)
#print(l1)
#l2 = [2,8,6,7,9,5]
#l3=[]
#l3 = [i for i in l2 if i%2==0]
#print(l3)
#l4 = ["sudha","ria","aditi"]
#l5 =[i.upper() for i in l4]
#print(l5)
#d1 = {"aditi":4,"chhavi":6,"tanu":9}
#d2 = {k:v**2 for k, v in d1.items()}
#print(d2)
#d3 = {"key1":1, "key2":5,"key3":8}
#d4 = {k:v for k,v in d3.items() if v>1}
#print(d4)  
def test():
    pass
def test1():
    print("this is my first function")
test1()
def test2():
    return"this is my first function "
print(test2() + "sudh")
def test3():
    return("sudh", 34, 67.87,[7,9,3])
print(test3())
#a,b,c,d = test3()
#print(a,b,c,d)
def test4():
    a = 5+5
    return a
print(test4())
def test5(a,b,c):
    d = a+b/c
    return d
print(test5(4,5,6))
def test6(f,g):
    h = f+g
    return h
print(test6("ello","world"))
#def test7(*args):
 #   return args
#print(test7())
def test8(**kwargs):
    return kwargs
print(test8())
print(type(test8()))
def test8(f = [5,6,9],l = "aditi", y = 89):
    return {"f":f,"l":l,"y":y}
print(test8())
def test7(*kwargs):
    return kwargs+(5,6)
print(test7())
#def test10(c,d,a = 8,b = 6):
 #   return test10()
#print(test10())
def test11(k, j, g = 7685):
    return k,j,g
print(test11(9,0))
#def add(p,o):
#    return p+o
#def calc(a,b,separator):
    #if(separator=="+"):
    #    print(a+b)
    #elif(separator=="-"):
    #    print(a-b)
   # elif(separator=="*"):
  #      print(a*b)
 #   else:
#        print("unavailable")
#a = int(input("enter number:"))
#b = int(input("enter number:"))
#separator = input("enter operator:")
#calc(a,b,separator)
# atm machine program-
pin_num = int(input("enter your pin number: "))
amount = int(input("enter your amount :  "))

withdrawl_amount = int(input("enter your withdrawl amount:"))
add_amount = int(input("enter  new amount:"))

dict = {   '1':"checking pin num",
           '2':"checking total amount",
           '3': "for left amount",
           '4': "add new amount",
           '5': "pin num is invalid"
        }
print(dict)
choose_num = int(input("choose 1 to 5"))

if choose_num==1 :
    print("pin number is correct")
    if (withdrawl_amount< amount):
        print("your withdrawl amount is",withdrawl_amount)
    else:
        print("insufficient amount")
elif choose_num==2:
    print("your total ammaount is :  ",amount)
elif choose_num==3:
    print("your total ammount after withdraw:" ,amount-withdrawl_amount)
elif choose_num==4:
    print("New total ammount is :",amount+add_amount)
elif choose_num==5:
     print("pin number is invalid")             
