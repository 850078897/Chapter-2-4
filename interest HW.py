p = 10000
n = 12
r = 0.08
t = int(input("the number of years: "))
final_amount = p * ((1 + r / n ) ** (n * t))
print (final_amount)

day = 24
h = int(input("type number of hours to wait: "))
now = int(input("type number of now: "))
b = now + (h % day)
print ("alarm:" +str(b))
