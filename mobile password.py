a=1
while a<=5 :
   b = int(input("Enter a Password: "))
   if b == 123:
      print(b,"password is correct")
      break
   elif a>=5:
      print("you tryed 5 times above ... so please wait 30 secs" )  
   else:
      print(b,"password is incorrect..... retry again")
   a=a+1

   
