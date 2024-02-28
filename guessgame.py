from random import *
win = False
start_num = 1
end_num = 99
attempt = 0

def board():    
    print("  ---------------")
    print(start_num, "      ?      ", end_num)
    print("  ---------------")
# Print the game board
'''
def error_check(answer):
    
    if answer < start_num or answer > end_num:
        print("Error")
        answer = int(input("Try again!!  "))
        
'''
# function to check number is out of range

def answer_checker(answer):

    global start_num
    global end_num
    global win
    global attempt

    if answer < x_number:
        start_num = answer
    elif answer > x_number:
        end_num = answer

    if answer == x_number:
        win = True
        print("Congratuation!! the answer is ", x_number)
        print("You have tried", attempt, "times!!")
        exit()

board()
# Check the answer


x_number = randint(1, 100)
answer = int(input("Guess the answer!  "))
while win != True:
    answer_checker(answer)
    attempt += 1
    board()
    answer = int(input("The number is between " + str(start_num) + " and " + str(end_num) + " :  "))
#    error_check(answer)