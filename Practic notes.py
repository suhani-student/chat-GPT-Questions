# python me module kya hota hai ek example do jisme math module use ho
a = 8
print()




# string slicing kya hai "python string ka use kar ke "tho" output nikalo
a2 = "python"






# if else or elif example ke sath samjhao 
x = "seema"
if x == "seema" :      # if statment kah rahi hai ki x me seema vallue hai 
    print("you log in")   # to tum login ho
else:                   # else ka kahna hai ki if agar nhi sahi hua to 
   print("incorrect name")  # name incorrect hai esa print kara do 
         # mainly ye tab use hota hai jab sirf ek statment tru or false hone par answer dependent ho 


xx = "neema"

if xx == "neema":                #   if kah raha ki xx me agar neema hai to
    print("you log in ")         #   print kara do tum log in ho 
elif xx == "suhani":             #   elif ne ek ke alawa dusri bhi statment li
    print('yes you are close')   #   or dusri statment ke liye alag chij print karai
else:                            #   else last me use hua jab sari statments galat ho to last me 
    print("wrong name")          #   ye print kara do









# for loop or while loop with example







# dictonery kya hoti hai ek student ki distonery banao jisme name ,age , marks ho 
student = {
    "name": "suhani",
    "age" : 20,
  "marks" : 61,
}







# Operators kitne type ke hote hai python me Arthmatic or comparisition ka example
operator = ["Arthmatic","logical","Assignment","Comparision"]
print(operator)

#Arthmatic operator 
a2 = 22
b2 = 9

c2 = a2*b2
d2 = a2+b2
e2 = a2-b2
print(c2,b2,e2)

#Comparisition operator 
name2 = "hema"
if name2 == "hema":     # is line me jo == hai wo compare kar raha name ki value hema se
    print("hello dear")
else:
    print("get lost frome the here")





# function jo do num ka sum return kare 
no1 = int(input("first num:"))
no2 = int(input ("second num:"))
def sum(x,y):
    print("no1+no2 :",no1+no2)

sum(2,3)
    




# ek program banao jisme user se no lo agar no positive ho to print karao positve or agar no negative ho to print karao negtiv 
U_Num = int(input("enter any num:"))
if U_Num % 2 == 0 :
    print("number is positive")
else:
    print("number is negetive")




            #[14 may 2026]


a = [ "apple","banana","papaya",]
a.append("Mango")                          # list me ek fruit or add karo
print(a)


a2 = [2,3,4,]
print(a2[-1])                # list me last element print karo


a3 = [10,20,30,40]
a3[2] = 25                      # list me second element ko change karo
print(a3)


a4 = [1,2,3,4,5]
print(len(a4))                   # list ki len print karo (jab len print hoti hai to index nhi list ke eliment ke hisab se len batata hai)

  
name = input("your name:")
print(name.upper())              # user se name lo aur usko upper case me print karo


character = ["python programing"]
print(len(character))                  # python programing me kitne character hai


s = "hello"
print(s[0])                   # string ke last or starting ke character print karao 
print(s[-1])


az = "adani ambani tata "
print(az.split())              # string ko list banakar print karo

idcard ={                      # ek distonery banao
    "name":"ayush",                             
    "age":34,
    "city": "delhi",
}
print(idcard["age"])                           # sirf age ki value print karao
print(idcard.keys())                                  # dictonery ki sabhi keys print karo
idcard.update({"mobile":"samsung"})             # ek set banao jisme ek value add karo 
print(idcard)
 

sets = {1,2,3,4}
sets.add(5)                             #ek set banao jisme ek value add karo 
print(sets)       
 


check ={2,4,6,8,10,2,6,6, 4}                # duplicate value lekar print karao or output dekho
print(check)  

 
Set1 = {10,20,30}
Set2 = {40,50,60}
print(Set1.union(Set2))               # Do sets ka union print karao


number = {5,6,8,9,2,3,5,3}           # kisi set me koi no dhundhna ho jaise 9 is set me dhundho
print(9 in number)

x = int(input("num:"))
y = int(input("num:"))
sum = x+y                                 # 2 input lo or unks - + * print karao
sub = x-y
mul = x*y
print("sum of x y :",sum ,"sub of x y :",sub ,"multiply of x y",mul)


#            [Total 20 Questions me se 12 Correct but 8 Questions  Wrong ]





                                 #[15] May 2026



  # Ans [1]       interpreter bolte hai
# Ans [3]       built in module ka ek exemle 



# Ans [4]       External module ka matlab kisi or ka likha code ya kisi or ka koi project jo mai apne code me use kar luu pip ki help se  
# Ans [5]       

# Ans [6]       single line comment 
# Ans [7]       multi line comment '''  ''' lagakar likha jata hai example
'''hi suhani 
        how are you'''
# Ans [8]       
a = "suhani"   #isme a variable hai kyuki suhani value a me store h 

# Ans [9]      
a = 23         # 23 ek num h yani ek int value hai

# Ans [10]     
a = "suhani"      # string data type

# Ans [11]
A = 45
B = 45
c = A + A         # + operater ka use do variables ya value ko jodna hai


# Ans [12]   
a = 34      # Asignment operator
A = 33 == 33   # comparison poerator

# Ans [13]  nhi pythone case senstive language nhi hai
# Ans [14]  input function user se input leta hai
a = input()
 
# Ans [15]  print () print karane ka kaam karta hai example 
print( " aspsafnvj")

# Ans [16]   
x = 10
y = 5
print (x+y)      # Output  15

# Ans [17]
print(10 // 3)    # Output  3.33

# Ans [18]
print(2**3)       # Output 2*2*2 = 8

# Ans [19]  AND Operator , OR Operator , NOT Operator
# Ans [20]  comparison operator  ( == , >= , <= , !=)
# ANs [21]   function wo hai jisse hum koi logical code likhkar  apna kaam asan kar sakte hai taki  baar bar usi function ko cal karne par kisi bhi value ke liye same kaam repeat ho sake 
def  sum(x,y):
   return x+y

# Ans [22]
a = "Radhikafashioncollab"
print(len(a))
print(a.index("f"))
print(a.count("a"))
print(a.upper())
print(a.lower())


# Ans [23]


                             # [16]  May 2026



#[37] Output batao
num = [1,2,3]
print(num[2])            # output 2


# [38] list me value add karne ke liye kon sa mathod use hota hai 
num = [1,2,3,4,]
num.append(5)


                              # [17] May 2026

# write a programe to creat a dictonary of hindi word with values as their english translation provid user with an option to look it up
meaning ={
     "Acha": "Good",
     "namashkar":"Hello",
     "bhagwaan":"Good",
     "khush":"happy",
}
print("Mean of that words:",meaning.keys())
print(meaning["khush"])





                              # [18]  May 2026
#  For loop se table            
num = int(input("enter num:"))
for i in range(1,11):
    print(f"{num} X {i} =",num * i)


table = int(input("enter num:"))



                        # [18] june 2026
                    
# [1.]  When we talk about function. Function in python has 2 types first Built in function and external function that is use for the work and code made short and repetable 




# [2.]   We use function in python for reapiting a work whenever we want and this way a function help us to don't write so much code excapet of this we cal function and complet the same work again whenever we want 

def sum(a,b):
   print (f"a+b = {a+b}")

sum(2,9)



# [3.]
def functionname (parameater):
        # the work we want to do 
 functionname()


# [4.] A function defination is says that a function is a code that help us to make shorter our program and make a key like line called function calling .lets example that  we right a code for a 2 num sub traction that we want show on screen thats way we write tha subtraction code  but after some work we wnt to same code again but when we write the same code again its to large thats wy we call the function and solve the problem. and we use function for diffrent type of works.....


# [5.]  a parameater given by the programer and the bases of parameater we give arguments in function calling 
def functioname( Parameater):
       return
functioname("Aurgumeant")


# [6.] exatly the word argument i cote in my 5th answer and the argument is given by the user at the time of function calling 


# [10.]  the diffrence bitween print and return is a print function whenever you want it give the value of the function but the return only one time return the value after complet the function


# [11.]   Explane the upper()
a = "suhaniDubey"
print(a.upper())



# [12.]   Explane the lower()
b = 'shunaniDUBEY'
print(b.lower())



# [13.]   Explane the title()
c = "hy i am shuanhi from india UP kanpur nagar"
print(c.title())



# [14.]   Explane the capitalize()
d = "hyy is this a indian food ?"
print(d.capitalize())

# [15.]  Explane the strip ()
e = "yes i realise here is somthing somthing missing"
print(e.strip("somthing missing"))                                  # i dont understand this


# [16.]  Explane the replace 
name = "sunita , sangita , babita , namita , venita"
print(name.replace("babita", "gita "))


# [17.]  explane the find
script = "Twinkle Twinkle little star mera gana super star gana mera gate jao dahi jamake khilate jao"
print(script.find("dahi".lower()))

# [18.]  Explane the count 
world = " sara jaman sara jaman ab mai kya batau hume ata nhi gana"
print(world.count("jaman".lower()))

# [19.]  Explane the split
student = " Jitendr Prsad Bajpai"
print(student.split("Bajpai"))

# [20.]  Explane the join
capitals = "delhi , kolkata , lucknow , patna , mumbai , maduray "           # i dont understand this also
print(capitals.join( "Ahamd"))


# [21.]  Explane the startswith 
student = "HarshitYadav"
print(student.startswith("shit"))
print(student.startswith("Har"))                                   # somthing somthing Dout
print(student.startswith("Yadav"))


# [22.]  Explane the endswith 
student2 = "swetaThakre"
print(student2.endswith("e"))
print(student2.endswith("swe"))


# [23.]  Explane the isalpha()
char = "wjdnmsnds"
print(char.isalpha())


# [24.]  Explane the isalnum() /  isdigit
print(student.isalnum())
print(student.isdigit())

# [25.] Write a programe to count vowels in a string 
a = "i am a student of Sowftware engeniaring and cybersecurity "
print(a)
print(a.count("a".lower() or "i".lower() or "e".lower() or 'o'.lower() or "u".lower()),"vowels in the line")

# [26.]  Write a program to reverse a string 
student = "Cybersecurity"
                                                                  # i forget this 

# [27.]  Write a program to check wether a string is a palindrome
                                                                    # i think i don't understand this question

# [28.] a list contains multiple values is calld list [] this symbol use for list
a = [ 1,2,3,4,5]



 
 


                          # [13] june 2026

   # [1.] 
print("[] this is a list symbol")
a = [1 , 2 , 3 , 4 , 5]
print(len(a))                  # len()   matlab length
print(a.index(3))            # index()  bata raha hai ki 3 kis index pe hai
print(type(a))

print(range(4))             # samaj me nhi aya



# [2.]  
def prayer(name,Class):
    print(f"Wellcom To {name} in class {Class} Campaus.")
    print(f" i pledge to never missbehavin with our class {Class} students. ")
    print(f"I oath that i am {name} not a Hindu not a Muslim not a sikh not a cristian \n i am only the student of class {Class}.")
    
prayer("sahil",12)
prayer("sameer",5)



student = ["jiya","riya","siya","siya"]
student.append("priya")
print(student)
print(student.count("siya"))


Student = [1, 8 , 3, 0]
Student.sort()               # sort()  orignal list ko change kar raha hai
print(Student)

print(sorted(Student))       # ek new list return karega

Student.sort(reverse =True)   # ye list ko ulta kar ke print kar raha desending order me
print(Student)




                       
 
                         # [14] june 2026

                      
 
ques = input("enter the name of lord ram's wife...")
if ques == "sita":
    print("yes your Answer is Right. ")
else :
    print("No you are wrong sita is the name of Lord Ram's wife.")


class12th = {
    "student":23,
    "subject":6,
    "ClassTeacher":"Saurabh sir",
    "Boys Moniter":"Nitin",
    "Girls Moniter":"kirti"
}
print(class12th.keys())
print(class12th.items())
print(class12th.values())
# class12th.update(["site":"science"])           i don't understand update()
print(class12th.clear())
# print(class12th.pop())                   i don't understand pop ()


# strig slicing
string = "kanpurMemorialinstute"
print(string.index[4:6])                          # i don't understand string slicing
 


 # use while loop
i = 1 
while i < 11:
    print(f"5 X {i} = {i*5}")
    i += 1




import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.title("My First Graph")
plt.show()

import matplotlib.pyplot as plt
sub = ["Python", "Math","Science"]
marke = [90,85,95]

plt.bar(sub,marke)
plt.show()

                     