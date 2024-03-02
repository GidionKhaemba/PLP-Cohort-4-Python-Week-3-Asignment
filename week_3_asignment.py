'''price=int(input("What is the price in Ksh: "))
discount_percent=int(input("What is the discount in %:  "))'''

#Question1
'''Create a function named calculate_discount(price, discount_percent)
 that calculates the final price after applying a discount. The function
   should take the original price (price)
 and the discount percentage (discount_percent) as parameters.
   If the discount is 20% or higher, apply the discount; otherwise, 
   return the original price.
'''
 
def calculate_discount(price, discount_percent):
   if discount_percent > 20:
        print("The price is: Ksh.", price*((100-discount_percent)/100))
   else:
        print("The price is: Ksh.", price)
calculate_discount(500, 20)
    
'''Using the calculate_discount function, 
prompt the user to enter the original price of an item and 
the discount percentage. Print the final price after applying the discount,
 or if no discount was applied, print the original price.'''

price=int(input("What is the price in Ksh: "))
discount_percent=int(input("What is the discount in %:  "))
if discount_percent > 20:
        print("The price is: Ksh.", price*((100-discount_percent)/100))
else:
        print("The price is: Ksh.", price)