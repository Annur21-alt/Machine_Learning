age = 38
if (age >= 11):
    print ("You are eligible to see the Football match.",end=" ")
    if (age <= 20 or age >= 60):
        print("Ticket price is $12",end=" ")
    else:
        print("Tic kit price is $20",end=" ")
else:
    print ("You're not eligible to buy a ticket.")