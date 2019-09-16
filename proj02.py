# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:30:25 2019

@author: Dante
"""

BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
print(BANNER)
PROMPT = '''\nWould you like to continue (Y/N)? '''
PROMPT = '''\nWould you like to continue (Y/N)? '''
cont=input('''\nWould you like to continue (Y/N)? ''')
while(cont=="Y"):
    code=input("\nCustomer code (BDW): ")
   #judge letter input
    if (code=="B"or code=="D" or code=="W"):
         
        days=int(input("\nNumber of days: "))
        startRead=int(input("Odometer reading at the start: "))
        endRead=int(input("Odometer reading at the end:   "))
        #distance calculation
        if endRead>=startRead:
            miles=(endRead-startRead)/10
        else:
            miles=(1000000-startRead)/10+endRead/10
        ####################
        totalSum=0
        
        #Do calculate here
        if code=="B":
            baseC=40*days
            mileC=miles*0.25
            totalSum=baseC+mileC
        elif code=="D":
            baseC=60*days
            avM=miles/days
            if(avM>100):
                mileC=(miles-days*100)*0.25
            else:
                mileC=0
            totalSum=baseC+mileC
        elif code=="W":
            #weekNum calculation
            if(days%7==0):
                weekNum=days/7
            elif(days%7!=0):
                weekNum=int(days/7)+1
            #WeekNum calculation End    
            baseC=weekNum*190
            avM=miles/weekNum
            if(avM<=900):
                mileC=0
            elif 900<avM<=1500:
                mileC=weekNum*100
            else:
                mileC=(weekNum*200)+(miles-weekNum*1500)*0.25
            totalSum=baseC+mileC    
         #Calculation Done       
            
            
            
        print("\nCustomer summary:")
        print("\tclassification code:",code)
        print("\trental period (days):",days)
        print("\todometer reading at start:",startRead)
        print("\todometer reading at end:  ",endRead)
        print("\tnumber of miles driven: ",miles)
        print("\tamount due: $",float(round(totalSum,2)))
       
        cont=input('''\nWould you like to continue (Y/N)? ''')
    else:
        print("\n\t*** Invalid customer code. Try again. ***")
        continue
else:
    print("Thank you for your loyalty.")    
    
    
    
    
"\nCustomer code (BDW): "
"\nNumber of days: "
"Odometer reading at the start: "
"Odometer reading at the end:   "
"\n\t*** Invalid customer code. Try again. ***"
"\nCustomer summary:"
"\tclassification code:"
"\trental period (days):"
"\todometer reading at start:"
"\todometer reading at end:  "
"\tnumber of miles driven: "
"\tamount due: $"
"Thank you for your loyalty."