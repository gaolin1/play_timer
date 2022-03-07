from datetime import datetime
from logging import shutdown
from random import randint
from dateutil.relativedelta import relativedelta
from tkinter import messagebox
import tkinter as tk
import os

def main():
    root = tk.Tk()
    root.withdraw()
    num_q = max_num()
    shut_down, alert = get_time(num_q)
    alert_time(shut_down, alert)
    shut_down_time(shut_down, num_q)

def max_num():
    operation = def_operation()
    num_q = 0
    outcome = "correct"
    while num_q < 6 and "correct" in outcome:
        operation = def_operation()
        num_q, outcome = math(operation, num_q)
        min = 15 + num_q * 5
        print("Current total playing time: " + str(min) + " minutes.\n")
    return num_q

def shut_down_time(shut_down, num_q):
    now = datetime.now()
    while now <= shut_down:
        if now == shut_down:
            msg = "computer will shut down now."
            show_shut_down(msg)
            with open('log.txt', 'a') as file:
                shut_down_time = "system shut down time: " + str(shut_down) + "\n"
                number_of_correct = "number of correctly answered question: " + str(num_q) + "\n"
                string = shut_down_time + number_of_correct
                file.write(string)
            os.system('shutdown -s')
        else:
            now = datetime.now()
        now = datetime.now()

def alert_time(shut_down, alert):
    now = datetime.now()
    while now < shut_down:
        while now <= alert:
            if now == alert:
                msg = "5 minutes before shutdown, click Ok to confirm."
                show_time(msg)
                return
            else:
                now = datetime.now()
        else:
            now = datetime.now()
    print("it's time")

def show_shut_down(msg):
    messagebox.showwarning("Turn off warning", msg)
    return

def show_time(msg):
    messagebox.showwarning("5 minutes warning!", msg)
    return

def def_operation():
    num = randint(0,3)
    if num == 1:
        num = " + "
    elif num == 2:
        num = " - "
    elif num == 3:
        num = " x "
    else:
        num = " / "
    return num

def math(operation, num_q):
    num_three = randint(100,999)
    num_two = randint(10,99)
    question, answer = question_answer(num_three, num_two, operation)
    ben_answer = input(question)
    while ben_answer == "" or ben_answer.isalpha() == True:
        ben_answer = input("did not receive a valid number, try entering again: ")
    ben_answer = float(ben_answer)
    attempt = 1
    while attempt < 3:
        if ben_answer != answer:
            attempt += 1
            ben_answer = float(input("Sorry BenBen, try again (attempt #" + str(attempt) + "): "))
        else:
            print("Good Job BenBen :P (5 mins added)")
            attempt = 3
            num_q += 1
            outcome = "correct"
            return num_q, outcome
    print("you have exceeded the maximum number of attempts")
    num_q = num_q
    outcome = "wrong"
    return num_q, outcome

def question_answer(num_three, num_two, operation):
    question = str(num_three) + operation + str(num_two)
    question = "Question: " + question + "\n Answer: "
    if operation == " + ":
        answer = num_three + num_two
    elif operation == " - ":
        answer = num_three - num_two
    elif operation == " x ":
        answer = num_three*num_two
    else:
        answer = num_three/num_two
        answer= round(answer, 1)
    return question, answer


def get_time(min):
    now = datetime.now()
    min = min*5+15
    new = now + relativedelta(minutes=min)
    alert = new - relativedelta(minutes=5)
    return new, alert

if __name__ == '__main__':
    main()