print("String Manipulation")
'''
    Data types:
        Int, Float, Strings, List, Booleans
        Primitive: Int, Booleans, Float, Character
        Non-Primitive: Strings, List

'''

#name = input("Enter Your Name!  ")
#age = input("How old are you? ")
#print("Hello " + name + ", you are " + age + " years old!")

#petName=input("What is your pets name? ")
#petAge=input("How old is your pet? ")
#petSize=input("How big is your pet? ")
#petSmell=input("How does your pet smell? ")

#print("Your pet, "+petName+", sounds like a cool pet. I can't believe they are "+petAge+" and "+petSize+".")
#print("I like "+petSmell+ " smelling pets.")


#output = (f'''
#Your pet, {petName}, sounds like a cool pet. I can't believe 
#they are {petAge} and {petSize}.
#'')

#print(output)

#name=input("what is your name?")
#print 
#print(bin(6))
#print(bin(-6))
#print(bin(ord("d")))
#print(bin(ord("o")))
#rint(bin(ord("g")))

cost=input("How much does gas cost? ")
numberOfGallons=input("How many gallons did you buy? ")
total=float(cost)*int(numberOfGallons)
print(total)

first=input("what is your first name? ").title()
last=input("What is your last name? ").title()
prefix=input("What is your title? (Mr, Mrs. Dr... ").title()
print(f"Hello, {prefix}. {first} {last}")