def my_function (num):
    order = 0
    while True: 
        if num == 1:
            # print(order)
            break
        elif num % 2 == 0 :
            order += 1
            num = num/2
            # print (num)
        else:
            order += 1
            num = 3*num + 1
            # print (num)
    return (order)


# my_function (125)

biggest = 0
for i in range(2,1000000):
    now_num = my_function(i)
    if now_num > biggest:
        biggest = now_num
        my_dic = {i : biggest}

print(my_dic)


