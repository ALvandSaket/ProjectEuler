
def check_if_right(x):
    factors = []
    for i in range (1,int(x**(0.5))+1):
        if x % i == 0 :
            factors.append(i)
    # print (len(factors))
    if len(factors) == 500 :
        print("this is the right one")
        return False
    else:
        # print("not this one")
        return True

number = 1 
u = 2
while True :
    number = number + u
    u += 1
    # print(u)
    print (number)
    # list.append(new)
    if not check_if_right(number):
        break

