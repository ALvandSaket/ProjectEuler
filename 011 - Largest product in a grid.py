one = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08'
two = '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00'
three = '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65'
four = '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91'
five = '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80'
six = '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50'
seven = '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70'
eight = '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21'
nine = '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72'
ten = '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95'
eleven = '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92'
twelve = '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57'
thirteen = '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58'
fourteen = '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40'
fifteen = '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66'
sixteen = '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69'
seventeen = '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36'
eighteen = '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16'
nineteen = '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54'
twenty = '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

le_list = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty]

les_lists = []
for i in le_list :
    new = i.split(' ')
    new_int = []
    for x in new :
        new_int.append(int(x))
    les_lists.append(new_int)

# Horiz
biggest_horiz = 0
for x in range (0,20):
    for y in range (0,17):
        z1 = les_lists[x][y]
        z2 = les_lists[x][y+1]
        z3 = les_lists[x][y+2]
        z4 = les_lists[x][y+3]
        mul = z1 * z2 * z3 * z4
        if  mul > biggest_horiz :
            biggest_horiz = mul
# print (biggest_horiz)

# Vertic
biggest_ver = 0
for x in range (0,17):
    for y in range (0,20):
        z1 = les_lists[x][y]
        z2 = les_lists[x+1][y]
        z3 = les_lists[x+2][y]
        z4 = les_lists[x+3][y]
        mul = z1 * z2 * z3 * z4
        if  mul > biggest_ver :
            biggest_ver = mul
# print (biggest_ver)

# Oblique

biggest_obl_one = 0
for x in range (0,17):
    for y in range (0,17):
        z1 = les_lists[x][y]
        z2 = les_lists[x+1][y+1]
        z3 = les_lists[x+2][y+2]
        z4 = les_lists[x+3][y+3]
        mul = z1 * z2 * z3 * z4
        if  mul > biggest_obl_one :
            biggest_obl_one = mul
# print (biggest_obl_one)



biggest_obl_two = 0
for x in range (0,17):
    for y in range (0,17):
        z1 = les_lists[x][y+3]
        z2 = les_lists[x+1][y+2]
        z3 = les_lists[x+2][y+1]
        z4 = les_lists[x+3][y]
        mul = z1 * z2 * z3 * z4
        # print(f"{x}-{y+3} , {x+1}-{y+2} , {x+2}-{y+1} , {x+3}-{y} = {mul}")
        if  mul > biggest_obl_two :
            biggest_obl_two = mul
# print (biggest_obl_two)


# print (biggest_horiz)
# print (biggest_ver)
# print (biggest_obl_one)
# print (biggest_obl_two)

gratest_list = [biggest_horiz, biggest_ver,biggest_obl_one,biggest_obl_two]
print(max(gratest_list))