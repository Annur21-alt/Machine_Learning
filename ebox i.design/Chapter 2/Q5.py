hurl_factor, spin_factor, speed_factor=map(int,input().split())
if hurl_factor > 50 and spin_factor > 60 and speed_factor>100:
    print(10)
elif hurl_factor>50 and spin_factor>60:
    print(9)
elif spin_factor>60 and speed_factor>100:
    print(8)
elif hurl_factor > 50 and speed_factor>100:
    print(7)
elif hurl_factor > 50 or spin_factor > 60 or speed_factor>100:
    print(6)
else :
    print(5)
    