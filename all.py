
import sys


def input_a():
        answer = int(input("Enter Number:"))
        if answer == 1: 
                 import input_file 
                 
        elif answer == 2: 
                 import update_file 
        else: 
                print("Please enter yes or no (lower case):") 
                input_a() 
                #n


print("Content(s) in file:")
with open('demofile2.txt') as fp:
    for i, line in enumerate(fp):
        sys.stdout.write('%01d %s'%(i , line))
print("\n")        
print("Choose which action to do:")
print("1.Input new data/value:")
print("2.Update existing data/value:")  

answer = int(input("Enter Number:"))
if answer == 1: 
         import input_file 
         
elif answer == 2: 
         import update_file 
else: 
        print("Please enter yes or no (lower case):") 
        input_a()      
#write_f()                             

                
                         
