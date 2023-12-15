import statistics

admins ={'python':'Pass0123','user1':'pass2'}

def main():
    print("""
    Welcome to grade Central
    
    [1]-Enter Grades
    [2]-Remove Student
    [3]-Student Average Grades
    [4]-Exit
    """)
    
    action=input('What would you like to today?(Enter a number)')
    
    if action == '1':
        print('1')
    elif action == '2':
        print('2')
    elif action =='3':
        print('3')
    else:
        print('No valid choice was given,try again')
        
login =input('Username:')
passw =input('Password:')

if login in admins:
    if admins[login] == passw:
        print('Welcome',login) 
        while True:
            main()
    else:
        print('Invalid password,will detonate in 5 secods!')
else:
    print('Invalid username,calling the FBI to report this')
    