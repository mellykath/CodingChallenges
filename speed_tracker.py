import re
import csv
start_time = 0
end_time = 0.008
distance_between_cameras =1

def speed_of_car(distance_between_cameras,end_time):
    speed = distance_between_cameras/end_time
    return speed

#variable speed called within the function
speed= speed_of_car(distance_between_cameras,end_time)
print(speed)

#regular expression
#^means starting letter/number, []means letters in between, + means 1 or more letters and $ means ending letter
print (re.match('^[A-z]{2}[0-9]{3}[A-z]{2}$', 'XX123XX')!=None)

string = ("XX1X3XX")
is_alphabetical=True
#boolean cannot be combined with string etc
for a in string[0:2]:
#a.isaplha() is a function calling a boolean value based on whether a is alphabetical or not
    is_alphabetical = is_alphabetical and a.isalpha()
for b in string[2:5]:
#b.isdigit() is a function calling a boolean value based on whether b is digital or not
    is_alphabetical = is_alphabetical and b.isdigit()
for c in string[5:7]:
    is_alphabetical = is_alphabetical and c.isalpha()

print (is_alphabetical)


l=[]

with open('carreg.csv') as f:
    l = list(filter(None, csv.reader(f)))
l.pop(0)
print (l)
for item in l:
    print(float(item[1]))
    speed=speed_of_car(distance_between_cameras,float(item[1]))
    if speed>70:
        print(str(speed) +'Exceeded speed limit')
    else:
        print(str(speed) + 'Within speed limit')
    print(item[0])
    string = item[0]
    is_alphabetical=True
#boolean cannot be combined with string etc
    for a in string[0:2]:
#a.isaplha() is a function calling a boolean value based on whether a is alphabetical or not
        is_alphabetical = is_alphabetical and a.isalpha()
    for b in string[2:5]:
#b.isdigit() is a function calling a boolean value based on whether b is digital or not
        is_alphabetical = is_alphabetical and b.isdigit()
    for c in string[5:7]:
        is_alphabetical = is_alphabetical and c.isalpha()

    print (is_alphabetical)
