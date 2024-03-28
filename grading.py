# a program to utilise the if statement

'''
scores and grade
    A = 100 - 75
    B = 74 - 65
    C = 64 - 50
    D = 49 - 45
    F = 44 - 0
'''

retry = True

# name of the student
while retry == True :

    input('name of student :')
    grade = float(input ('score of student :'))

# the conditional statement 

    if grade >=75 :
        print(f"Your score is {grade} grade is A")
    elif 74>=grade>=65 :
        print(f"Your score is {grade} grade is B")
    elif 64>=grade>=50 :
        print(f"your score is {grade} grade is C")
    elif 49>=grade>=45 :
        print(f"your score is {grade} grade is D")
    else:
        44>=grade>=0
        print(f"Your score is {grade} grade is F")
    
    yes = input('do you want to try AGAIN : ')
    
    if yes == 'yes' :
        retry == True
    else:
        retry = False   
    
     

