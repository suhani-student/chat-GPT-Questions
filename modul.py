import random
random.choice()  # Tab use hoga jab list me se ek num chahiye

fruit = ["Mango","Banana","Apple","Papaya"]
secret = random.choice(fruit)
print(fruit )
guess = input("guess fruit :")
if guess == secret :
   print("Correct !")
else:
   print(f"wrong number was {secret}")

random.randint()  # Tab use hoga jab random integer chahiye jaise 1 se 10 ke bich (1,10)
import random
num = int(input ("Chose Number Between [1 to 10]"))
numC = random.randint(1,10)  
if num == numC:
   print("you Both Are Right")
else:
   print("You both Are Different")


random.shuffle()   #Tab Jab list ko Mix karn
random()            # Tab use hoga jab 0 se 1 ke bich Decimal Number nikalna ho Probability
a = 2
b = 4
random.uniform(a,b)  #jab decimal number range me chose karna ho
n = ["snjj","ashh","pilm","jwhuw"]
random.sample(list,n)    #Multyple Unique items
      