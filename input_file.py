#Input_file (Python)
#f.write("Now the file has more content!\n")



def write_f():
    val = input("Enter your value: ")
    f.write(val)
    f.write('\n')
    print("Insert more in inputs?")
    answer = input("Enter yes or no (lower case): ")
    if answer == "yes": 
         write_f() 
    elif answer == "no": 
         f.close() 
    else: 
        print("Please enter yes or no(lower case): ") 
        input_a()

   

def input_a():
     answer = input("Enter yes or no (lower case): ")
     if answer == "yes": 
         write_f() 
     elif answer == "no": 
         f.close() 
     else: 
        print("Please enter yes or no (lower case):") 
        input_a()
        

        




f = open("demofile2.txt", "a")
write_f()                             
f.close()