#homework 2
# problem 1
"""Rewrite the code using a **while** loop to accomplish the same thing.

  Գրել նշված ծրագիրը **while** ցիկլով։

`for i in range(1, 51):`

           `print(i)`
"""
# i=1
# while 1<=i<=50:
#   print(i)
#   i+=1

# problem 2
"""
  Գրել ծրագիր while ցիկլով, որը կխաղա հետևյալ խաղը․ խաղացողը սկսում է $100$-ով և յուրաքանչյուր քայլում նետվում է
   մետաղադրամ, իսկ խաղացողը պետք է գուշակի արդյոք ղուշ է ստացվել, թե գիր։ Յուրաքանչյուր ճիշտ գուշակածի համար խաղացողը ստանում է 9$ և կորցնում է
   10$ յուրաքանչյուր սխալի դեպքում։ Խաղն ավարտվում է, եթե խաղացողը կորցնում է ամբողջ գումարը կամ հավաքում է 200$:"""


import random

user_money = 100

while user_money > 0 and user_money < 200:
    # Flip a coin (0 for heads, 1 for tails)
    coin_flip = random.randint(0,1)

    # Get the user's guess
    user_guess = input("Guess heads or tails: ").lower()

    if user_guess == "heads" and coin_flip == 0:
        user_money += 9
        print("Correct! You now have ${}".format(user_money))
    elif user_guess == "tails" and coin_flip == 1:
        user_money += 9
        print("Correct! You now have ${}".format(user_money))
    else:
        user_money -= 10
        print("Incorrect. You now have ${}".format(user_money))

if user_money == 0:
    print(" Game over!")
elif user_money == 200:
    print(" You've reached $200. You win!")

# problem 3
"""Գրել ծրագիր while ցիկլով, որը կտպի օգտատիրոջ կողմից տրված թվի բազմապատկման աղյուսակը 
(թիվը բազմապատկած 1-ից 10 ամբողջ թվերով)։ Օրինակ՝ 2 թվի համար կլինի"""

# num = int(input("enter number: "))
# i=1
# while i<11:
#     res = num*i
#     print(f"{num}*{i}=", res)
#     i+=1

# problem 4
"""Գրել ծրագիր, որը կվերցնի օգտատիրոջ անունը և մի թիվ, որը կներկայացնի թե քանի անգամ պետք 
է տպել այդ անունը։ Ծրագիրը պետք է տպի այդ անունը նշված քանակությամբ նույն տողում (բացատով առանձնացված)։"""

# user_name = input("What is your name?: ")
# quantity_survey = int(input("how many times should the name be repeated? "))
# for i in range(quantity_survey):
#     print(user_name, sep=" ", end=" ")

# problem 5
"""The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each number
 thereafter is the sum of the two preceding numbers. 
Write a program that asks the user how many Fibonacci numbers to print and then prints that many."""

# n = int(input("Enter the number of Fibonacci numbers to print: "))
#
# fibonacci_sequence = [1, 1]
#
# if n == 1:
#     print("Fibonacci sequence of length 1:", [1])
# elif n == 2:
#     print("Fibonacci sequence of length 2:", fibonacci_sequence)
# elif n > 2:
#     for i in range(2, n):
#         next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_fibonacci)
#
#     print("Fibonacci sequence of length", n, ":", fibonacci_sequence)
# else:
#     print("Please enter a positive integer greater than 0.")


# problem 6
"""Գրել ծրագիր, որը օգտատիրոջ կողմից մուտքագրված  n -ի համար կհաշվի հետևյալ արտահայտությունը  1+1/2+1/3+…+1/n  և կտպի ստացված արժեքը։"""
# n = int(input("Enter n: "))
# sum_result = 0
# for i in range(1, n + 1):
#     sum_result += 1 / i
# print("1 + 1/2 + 1/3 + ... + 1/n =", sum_result)


# Problem 7
""" Write a program to compute the
sum  1−2+3−4+…+1999−2000  using a for loop."""
# sum_res = 0
# for i in range(1, 2001):
#     if i % 2 == 0:
#         sum_res -= i
#     else:
#         sum_res += i
# print(sum_res)

