stud_data = open('studentdata.txt', 'r')
stud = stud_data.readline()
for stud in stud_data:
    stud = stud.split()
    num_stud = [int(num) for num in stud[1:]]
    #for num in num_stud:
        #print(type(num))
        #num_stud += int(num)
    print(num_stud)
    x = min(num_stud)
    y = max(num_stud)
    print(stud[0], x, y)
