import random
import operator
import csv
from random import randint

def randomCalc():
#This is a dictionary where the key is a string and the operator value is the functioning symbol
    symbols={"*":operator.mul,
            "+":operator.add,
            "/":operator.truediv,
            "-":operator.sub}

    while True:
        random_a = randint(0,9)
        random_b = randint(0,9)

        random_c = random.choice(list(symbols.keys()))
        if not (random_c =="/" and random_b ==0):
#get Answer by accessing dictionary value using "symbols[key]"and applying it between random_a and random_b
            Answer = symbols[random_c](random_a,random_b)
            print("what is {} {} {} ?\n".format(random_a, random_c, random_b))
            return Answer

def AskQuestion():
    Answer=randomCalc()
    Guess=float(input())
    return Guess ==Answer

def Quiz(Name):
    print('Welcome' + Name + 'This is a ten question quiz\n')
    score = 0
    for i in range(10):
        correct = AskQuestion()
        if correct:
            score+=1
            print ("Correct!\n")
        else:
            print("Incorrect.\n")
    print ('Your score was {}/10'.format(score))
    return score
name = input("Please enter your name: ")
class_number = input("Please enter class number: ")

score = Quiz(name)

#Userscore = (name, '', str(score), '')

if (int(class_number)==1):
    with open ('class1.csv', 'a') as myFile:
        writer =csv.writer(myFile, delimiter=' ')
        writer.writerow((name, score))
        #myFile.writelines(Userscore)
        #myFile.close()
elif (int(class_number)==2):
    with open ('class2.csv', 'a') as myFile:
        writer =csv.writer(myFile, delimiter=' ')
        writer.writerow((name, score))
        #myFile.writelines(Userscore)
        #myFile.close()
elif (int(class_number)==3):
    with open ('class3.csv', 'a') as myFile:
        writer =csv.writer(myFile, delimiter=' ')
        writer.writerow((name, score))
        #myFile.writelines(Userscore)
        #myFile.close()

with open('class1.csv', 'r') as f:
    #lines = f.read().splitlines()
    list_of_results=[]
    reader = csv.reader(f, delimiter=' ')
    for l in reader:
        list_of_results.append([l[0],int(l[1])])
#This is a dictionary where keys are names of users and values are lists of results for user
    dict_of_results={}
    for l in list_of_results:
#If key(name of user) doesn't already exist, create a new list to append results to,
#else append results to current list
        if not l[0] in dict_of_results:
            dict_of_results[l[0]]=[]
        dict_of_results[l[0]].append(l[1])
#Creates list using dictionary keys
list_of_keys=list(dict_of_results.keys())
#Sorts list of names into alphabetical order
list_of_keys.sort()
for x in list_of_keys:
    users_results=dict_of_results[x]
    high_score = max(users_results[-3:])
    print("%s %r Highest score: %d" % (x, users_results[-3:], high_score))
