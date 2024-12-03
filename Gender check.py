# a=input('Enter 1st Number:')
# b=input('Enter 2nd number:')
# c=int(a)
# d=int(b)
# e=c+d
# print(f'The sum of Two numbers is {e}')
def gender():
    user_input=input('Enter your Gender:').strip().lower()
    name=str(user_input)

    if name=='boy':
        print('You are physcially strong')
    elif name=='girl':
        print('you are mentally strong')
    else:
        print('Enter correctly')
        gender()


    
def recursive():
    while True:
        repeat=input('Do you want to repeat?(y/n)\n').strip().lower()
        if repeat=='y':
            gender()
        elif repeat=='n':
            print('thank you')
            break
        else:
            print('enter correctly')
            recursive()
    
gender()
recursive()