
print("calculate your BMI")
print("written by Franklin Araque")
print("")


#user input
Heightfeet = int(input("enter your height(in feet): "))
Heightinches = int(input("enter your height(in inches): "))
weight = int(input("enter your weight (in lbs): "))


#unit conversions for BMI calculation
FeetToinches= (Heightfeet)*12               #converting feet to inches 
 
FeetandInches = FeetToinches + Heightfeet   #adding the converted feet to inches and the inches from the user input together, total weight



#calculate BMI
calcBMI = (weight / (FeetandInches**2)) * 703    #in python "**" means the "^" for raised powers, eg "2^3" = "2**3"
calcBMI = round(calcBMI, 2)                      #rounding to the second decimal point

#display
print("for height " +str(Heightfeet)+"\""+str(Heightinches) +" and "+str(weight)+ " your BMI is: "+str(calcBMI))  #the "\"" is telling it to print the " inside the two other "", it skips the \
