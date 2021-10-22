#variables
Shirtprice = float(9.99)
HST = float(1.13)
Pantp = 14.99
start = input("Hello, welcome to Abby's Merchandizing!\nReady to order? (Yes/No): ")

if start.lower() == "yes":

    print("Let's start with choosing your first item!")
    
    first_item = input("Please make a selection:\nJeans: $14.99 \nShirt(Polo/T-Shirt) $9.99\n")

    if first_item.lower() == "jeans":

        print("Jeans sounds great!")

        pantq = input("How many Jeans would you like: ")

        pantsc = input("Sounds great! What colour of Jeans would you like? ")

        print("you have selected", pantq, pantsc,"Jeans!")

        check1 = str(input("ready to checkout? 'YES/NO': "))

        shirtsmaybe = input("Perfect! Great Choices! which shirts would you like?: (Polo, T-Shirt, None")
 





        total1 = (Pantp * float(pantq) * HST)

        tax = (float(pantq) * Pantp * 0.13)

        if check1.upper() == "YES":

   #IF another item == yes, else checkout
            print("your order:\n", pantq, pantsc, "Jeans    ", (Pantp* float(pantq)))

            discount = input("Are you a considered a senior citizen or a student?")

            if discount.lower() == "yes":

                disctotal = ((total1 / 100)*90)
                print( "Subtotal               " + float(pantq)*Pantp)
                print("HST:                       %.2f "  % float(tax))
                print("Senior/Student Discount     -10%   ")
                print("Total =================== %.2f" % disctotal)
                print("Thank you for shopping!")
        else:
            print("please come back soon!")

            
                         
          
          
          
          
            print("tax:                       %.2f "  % float(tax))
            print("Total ===================  %.2f" % total1)
            print("Thank you for shopping!")
           
#Check here for senior citizen/ student
# set quantity if statement, If quantity of one specific item is 3 or more, Apply a 15% dis
check = str(input("ready to checkout? 'YES/NO': "))

if check == (str("YES")):
    print("your order:")
    print(str(quant) + " " + colourChoose + " " + shirtstyle + "           " + "    %.2f " % float(str((float(Shirtprice * quant)))))
    
    
    #Variables
    quantfin = Shirtprice * quant
    total = (float(atax) + quantfin)
    #Command
    print("tax:                       %.2f "  % float(atax))
    print("Total ===================  %.2f" % total)
    print("Thank you for shopping!")
else:
    print("please come back soon!")
  