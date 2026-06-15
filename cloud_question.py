# [1.] 
# print("[] this is a list symbol")
# a = [1 , 2 , 3 , 4 , 5]
# print(len(a))                  # len()   matlab length
# print(a.index(3))            # index()  bata raha hai ki 3 kis index pe hai
# print(type(a))

# print(range(4))             # samaj me nhi aya



# [2.]  
# def prayer(name,Class):
#     print(f"Wellcom To {name} in class {Class} Campaus.")
#     print(f" i pledge to never missbehavin with our class {Class} students. ")
#     print(f"I oath that i am {name} not a Hindu not a Muslim not a sikh not a cristian \n i am only the student of class {Class}.")
    
# prayer("sahil",12)
# prayer("sameer",5)



# student = ["jiya","riya","siya","siya"]
# student.append("priya")
# print(student)
# print(student.count("siya"))


# Student = [1, 8 , 3, 0]
# Student.sort()               # sort()  orignal list ko change kar raha hai
# print(Student)

# print(sorted(Student))       # ek new list return karega

# Student.sort(reverse=True)   # ye list ko ulta kar ke print kar raha desending order me
# print(Student)


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
# plt.show()

