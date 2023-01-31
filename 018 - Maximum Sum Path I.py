first = "75"
second = "95 64"
third = "17 47 82"
forth = "18 35 87 10"
fifth = "20 04 82 47 65"
sixth = "19 01 23 75 03 34"
seventh = "88 02 77 73 07 63 67"
eighth = "99 65 04 28 06 16 70 92"
nineth = "41 41 26 56 83 40 80 70 33"
tenth = "41 48 72 33 47 32 37 16 94 29"
eleventh = "53 71 44 65 25 43 91 52 97 51 14"
twelveth = "70 11 33 28 77 73 17 78 39 68 17 57"
thirteenth = "91 71 52 38 17 14 91 43 58 50 27 29 48"
forteenth = "63 66 04 68 89 53 67 30 73 16 69 87 40 31"
fifteenth = "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

list_of_assets = [first, second, third, forth, fifth, sixth, seventh, eighth,
                  nineth, tenth, eleventh, twelveth, thirteenth, forteenth, fifteenth]
for i in list_of_assets :
    i = i.split(' ')
    for x in i :
        x = int(x)

for i in reversed(list_of_assets) :
     
