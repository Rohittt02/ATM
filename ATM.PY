print("Welcome to Bank Of India" )
print("Please Insert Your ATM card")
print("Please Enter your 4 Digit Pin")
amount = 20000
print("#My balance is",amount)
password= 1234
Pin=int(input("Enter Your Pin : "))
if Pin==password:
   print("Please Select Your Language")
   Language=int(input("Choose your language : \n 1. English\n 2. Hindi\n select any one:  "))
   if Language==1:
       print("thank you for choosing English language")
       print(" Dear Costumer What you want")
       print( " 1. Cash withdrawal\n 2. Cash deposit\n 3.Balance Enquiry ")
       cash=int(input("enter What you want : "))
       if cash==1:
           print("You choose cash withdrawal ")
           withdrawal=int(input("enter your withdrawal amount : "))
           if withdrawal<amount:
               print("Your Available amount is ", amount-withdrawal)
               print('thanks to visit ')
           else:
               print("You have no Enough Balance")
       elif cash==2:
           print("You choose cash deposit")
           deposit=int(input("enter your deposit amount : "))
           if deposit+amount:
               print("Your Total amount is " ,amount+deposit)
               print('thanks to visit ')
       elif cash==3:
           print("Your Total amount is", amount )
           print('thanks to visit ')
       else:
           print("Please select valid option ")
   elif Language==2:
       print("Hindi is not available\n continue in English ")
       Language=int(input("Choose English language : \n 1. English\n :  "))
       if Language==1:
           print(" Dear Costumer What you want")
           print( " 1. Cash withdrawal\n 2. Cash deposit\n 3. Balance Enquiry ")
           cash=int(input("enter What you want : "))
           if cash==1:
                   print("You choose cash withdrawal ")
                   withdrawal=int(input("enter your withdrawal amount : "))
                   if withdrawal<amount:
                       print("Your Available balance is " , amount-withdrawal )
                       print('thanks to visit ')
                   else:
                       print(withdrawal<amount,"You have no Enough Balance")
                       print('thanks to visit ')
           elif cash==2:
               print("You choose cash deposit")
               deposit=int(input("enter your deposit amount : "))
               if deposit+amount:
                   print("Your Total Amount is " ,amount+deposit)
                   print('thanks to visit ')
           elif cash==3:
               print("Your Total amount is", amount )
               print("thanks to visit")

           else:
               print("please select valid option")

       else:
           print("Please select valid language ")
   else:
       print("Please select valid language ")
else:
	print("Your pin is incorrect please try again ")






























    