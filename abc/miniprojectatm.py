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
