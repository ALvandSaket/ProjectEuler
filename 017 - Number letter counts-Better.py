Ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
Tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
Ten_to_Twenty = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


list_of_numbers = []

for i in range(1000):
    Our_num = ''
    if i>2 and i%100 == 0 :
        Our_num = Our_num + Ones[i//100] + 'hundred'
    elif i//100>0 :
        Our_num = Our_num + Ones[i//100] + 'hundredand'

    if not 10<i%100<20:
        Our_num = Our_num + (Tens[(i%100)//10])
        
    if 0<i%100<11 or 20<i%100<100 :
        Our_num = Our_num +  (Ones[i%10])
    elif 10<i%100<20 :
        Our_num = Our_num + (Ten_to_Twenty[i%10 -1])
    
    

    list_of_numbers.append (Our_num)


list_of_numbers.append ('onethousand')

print (list_of_numbers)

count = 0
for i in list_of_numbers :
    for x in i :
        count += 1

print (count)

