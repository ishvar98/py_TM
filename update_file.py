import sys

def update_f():
            my_file = open("demofile2.txt")
            string_list = my_file.readlines()
            my_file.close()

                       
            print("Choose which line to be updated")
            with open('demofile2.txt') as fp:
                for i, line in enumerate(fp):
                    sys.stdout.write('%01d %s'%(i, line)) 
            
            with open("demofile2.txt", 'r') as fp:
                for count, line in enumerate(fp):
                    pass
            print('Please Choose from 0 to', count)
            
            
            #input list number  int()
            userInput = 0
            while True: 
                try:
                    answer = int(input("Enter Number:"))
                except ValueError:
                 print("Not an integer!")
                 continue  
                else:
                    print("Yes an integer!")
                    break 
            
            if type(answer) == int:
                print("Is a number")
                if answer <= count: 
                    nvalue=input("""Enter a new value:""")
                    string_list[answer] = nvalue+'\n'
                else: 
                    print("Please enter a Position Number not more than:" + str(count)) 
                    input_a()
            else:
              print("Not a number") 




         
            
               
            
            
           #nvalue=input("""Enter a new value:""")
           #string_list[answer] = nvalue+'\n' 

            #write changes to data.txt
            my_file = open("data.txt", "w")                                 
            new_file_contents ='\n'.join(string_list)
            my_file.write(new_file_contents)
            my_file.close()

            with open("data.txt", 'r+') as fd:
                lines = fd.readlines()
                fd.seek(0)
                fd.writelines(line for line in lines if line.strip())
                fd.truncate()
                
            readable_file = open("data.txt")
            read_file = readable_file.read()
            print(read_file)  
            print("Update more in inputs?")
            answer = input("Enter yes or no (lower case): ")
            if answer == "yes": 
                update_f() 
            elif answer == "no": 
                readable_file.close() 
                exit()
            else: 
                print("Please enter yes or no(lower case): ") 
                input_a()



def input_a():
     readable_file = open("data.txt")
     read_file = readable_file.read()
     print("Continue to update exisiting lines?")
     answer = input("Enter yes or no (lower case): ")
     if answer == "yes": 
         update_f() 
     elif answer == "no": 
         readable_file.close()
         exit()
     else: 
        print("Please enter yes or no (lower case):") 
        input_a()
        
        



update_f() 