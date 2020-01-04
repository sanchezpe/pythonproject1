# ask the customer for their name using an input statement
nameCustomer = input ("Enter customer name: ")


# ask the user for their bill subtotal (before gratuity) using an input statement
# remember to “eval” the variable in order to perform arithmetic operations later
subtotal = eval(input("Enter subtotal: "))


# ask the user for the gratuity percent, e.g., 15 (they will not enter the % sign)
# use an input statement
# again, remember to “eval” the variable
gratuityPercent = eval(input("Enter gratuity: "))


# compute the gratuity charge, which is bill subtotal * (gratuity percent/100)
gratuityCharge = (subtotal * (gratuityPercent / 100))


# compute the final bill, which is subtotal + gratuity charge
total = (subtotal + gratuityCharge)


# print all input and computed values
print ("Customer:    " , nameCustomer)
print ("Subtotal:    " , subtotal)
print ("Gratuity:    " , gratuityCharge)
print ("Final Bill:  " , total)