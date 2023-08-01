import math
val = 0
print("\n")
print('\033[1m' +"HI, WELCOME TO SCIENTIFIC CALCULATOR")
print ('\033[0m')
def calculator():
        global val
        print("","1.Addition","\n","2.Substraction","\n","3.Multiplication","\n","4.Division","\n","5.Log","\n","6.Root",'\n',"7.Area of square","\n","8.Area of triangle","\n","9.Area of rectangle","\n","10.Area of circle","\n","11.Exit","\n")
        try:
            val = int(input("Choose the operation you want to perform: "))
            print("\n")
            if val == 1:
                a,b=  [float(z) for z in input("enter two numbers you want to add: ").split()]
                print("sum =",a+b)
                print("______________________________________________________________________________________________________________________")
            elif val == 2:
                a,b=  [float(z) for z in input("enter two numbers you want to substract: ").split()]
                print("difference =",a-b)
                print("______________________________________________________________________________________________________________________")
            elif val == 3:
                a,b=  [float(z) for z in input("enter two numbers you want to multiply: ").split()]
                print("product =",a*b)
                print("______________________________________________________________________________________________________________________")
            elif val == 4:
                a,b=  [float(z) for z in input("enter two numbers you want to divide: ").split()]
                print("quotient =",a/b)
                print("______________________________________________________________________________________________________________________")
            elif val == 5:
                a=float(input("enter the number: "))
                print("log",+a,"=",math.log(a))
                print("______________________________________________________________________________________________________________________")
            elif val == 6:
                a=float(input("enter the number: "))
                print("root of",+a,"=",math.sqrt(a))
                print("______________________________________________________________________________________________________________________")
            elif val == 7:
                a= float(input("enter the side: "))
                print(" Area of square =", a*a)
                print("______________________________________________________________________________________________________________________")
            elif val == 8:
                a,b=[float(z) for z in input("enter the base and height: ").split()]
                print(" Area of triangle =", 0.5*a*b)
                print("______________________________________________________________________________________________________________________")
            elif val == 9:
                a,b=[float(z) for z in input("enter the length and breadth: ").split()]
                print(" Area of rectangle =", a*b)
                print("______________________________________________________________________________________________________________________")
            elif val == 10:
                a= float(input("enter the radius: "))
                print(" Area of circle =", 3.14*a*a )
                print("______________________________________________________________________________________________________________________")
                   
            elif val ==11:
                def exit():
                    ans= str(input("Are you sure you want to exit?. Type yes or no:: "))
                    if ans == "yes":
                        print('\033[1m' +"THANK YOU FOR USING MY CALCULATOR.","\n","HAVE A NICE DAY")
                        print ('\033[0m')
                    elif ans=="no":
                        print("_____________________________________________________________________________________________________")
                        calculator()
                    else:
                        print("enter a valid answer")
                        exit()
                exit()
            else:      
                print("enter a valid number")
                print("______________________________________________________________________________________________________________________")
        except ValueError:
            print("please enter only valid entries")
            print("____________________________________________________________________________________________________________________")
while(val >=0 and val!=11):    
    calculator()