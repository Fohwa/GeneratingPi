import random

times = int(input("Number of points: "))

incircle = 0
insquare = 0

while times >= 0:
    
    ran1 = random.uniform(0, 1)
    ran2 = random.uniform(0, 1)

    if ran1**2 + ran2**2 <= 1: #in circle
        incircle += 1
        insquare += 1
    elif ran1**2 + ran2**2 > 1: #not in circle
        insquare += 1
    else:
        print("Error: Point not in circle and not outside")
    
    
    times = times - 1

pi = 4 * incircle/insquare # Ration of points times four is indeed pi

#just for some additional information
print("In: " + str(incircle))
print("Outside: " + str(insquare - incircle))

#The result is printed to console
print("Pi: " + str(pi))
