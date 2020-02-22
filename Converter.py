a = int(input('Enter the integer:'))
print('Binary output:')
bin_list = []
if a < 2:
    print(a)
else:
    while(a != 0):
        if  a%2 == 0:
            print("\t",0)
            bin_list.append(0)
        else:
            print("\t",1)
            bin_list.append(1) 
        a = a//2

bin_list.reverse()
print("Binary list:",bin_list)