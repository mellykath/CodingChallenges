import random

Credit = 100

Roll = ""

while Credit>20 and Roll =="":


    Objects = ("Cherry", "Bell", "Lemon", "Orange", "Star", "Skull")
    Credit -= 20
    print ("This turn has cost 20p Your balance is now"+ str(Credit))
    Chosen_objects = random.choice(Objects) + random.choice(Objects) + random.choice(Objects)
    if Chosen_objects.count("Skull")==2:
        Credit-=100
    elif Chosen_objects.count("Skull")==3:
        Credit = 0
    elif Chosen_objects.count("Bell")==3:
        Credit+=500
    else:
        for Object in Objects:
            if Chosen_objects.count(Object)==2:
                Credit+=50
            elif Chosen_objects.count(Object)==3:
                Credit+=100

    print (Chosen_objects)
    print (Credit)
    if Credit>20:
        print ("Press Enter to roll again; Enter any symbol to stop. Your balance is " + str(Credit)+"p")
        Roll=input()
