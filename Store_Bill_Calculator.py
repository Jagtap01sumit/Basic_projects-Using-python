
sum=0
while(True):
    
    user_Input=(input("Enter the value of item:\n"))
    if(user_Input != 'q'):
        sum=sum + int(user_Input)
        print(f"order Total so far : {sum}")
    else:
        print(f"Your Bill total is {sum} Thank You for shopping in our shop!!!")
        break