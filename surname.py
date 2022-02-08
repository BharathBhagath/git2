name_list=[]
i=0
while True:
    i+=1
    print('A-add\nE-exit')
    option=input('please choose your option :')
    if option == 'A':
        name=input('please enter student name :')
        split_name=name.split()
        name_list.append(split_name[-1])
    elif option == 'E':
        print('thanks you for visiting')
        break
    else:
        print('invalid option selected')
print('\n\n\n')
print('student list is :',name_list)
print('\n\n')
print('*'*100)
for i in (name_list):
    print(i) 
