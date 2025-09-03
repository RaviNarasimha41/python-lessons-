#String Data types 

# literal Assignment 

first ="ravi"
last = "narasimha"
print(type(first))
print(type(first)==str)
print(isinstance(first,str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += " " +"hallo"
print(fullname)

# Multiple line 
multipleline=''''
hey i am Ravi Narasimha                                                                                       
                           how are you
                                          I am Fine 
'''
print(multipleline)
print(len(multipleline))
print(len(multipleline.strip()))
print(len(multipleline.lstrip()))
print(len(multipleline.rstrip()))




#escapng speacial characters

sentance='I/am back to home!\t hey \n hi '
print(sentance)

#string method

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multipleline.title())
print(multipleline.replace("fine","good"))
print(multipleline)

#build a menu 

title = "menu".upper()
print(title.center(20,"="))
print("cofee".ljust(16,":") + "$3".rjust(4))
print("drink".ljust(16,":") + "$4".rjust(4))
print("juice".ljust(16,":")+  "$8".rjust(4)) 

print("")