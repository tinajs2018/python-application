# #itelate through a given function
# fruits=('Banana','lemon','apple')
# newit=iter(fruits)
# print(next(newit))
# print(next(newit))
# print(next(newit))

# #Bulding a itelator that return the numbers
# class Counting:
#     def __iter__(self):
#         self.a=1
#         return self 
#     def __next__(self):
#         x= self.a
#         self.a +=1
#         return x
# newobj=Counting()
# newit=iter(newobj)
# print(next(newit))
# print(next(newit))
# print(next(newit))
# # Question 1: print the python vesrion of your console.
# import sys 
# print(sys.version.split()[0])
# print('I will master python')
# x='python'
# y='3.8'
# print(x+ y)

# price=199.99
# print('This costs',price)
# price=69.99
# print(f'The cost of price {price}')

# prd_price='$34.99'
# prd_weight ='20lbs'

# print(f'The price of the product is {prd_price} and the weiht of the product is {prd_weight}')
# print('-' *20)
# print('VERSION: 1.0.1')
# print('-'*20)

# print('=' *40)
# print('author: johnsmith@sample.com')
# print('date: 01-01-2021')
# print('=' *40)

# print('summer' ,'time','holiday',sep ='#')
# # Write a program that calculates the area of a circle with a radius = 5. Use an approximate value of pi
# pi=3.14
# radius=5
# area=pi*5**2
# print(f'the areas of circle is{area}')
# princple=1000
# rate =1.03
# time =5
# interest=princple* (1+rate)*time
# Amount=interest+ princple
# print(f'The future value of the investment {Amount}')

# pv = 1000
# r = 0.03
# n = 5
# fv = pv * (1 + r) ** n
# print(f'The future value of the investment: {fv:.2f} USD')

# for i in range(10):
#     an= 10+4*i
#     x=sum(an)
#     print(x)

   
"""Program to word  pig latin"""
import sys
Vowel='aeoiu'
while True:
    word= input('Enter any word and get latin pig')
    if word[0] in Vowel:
        pig_latin = word + 'way'
    else:
        pig_latin =word[1:] + word[0] + 'ay'
    print()
    print('{}'.format(pig_latin),file=sys.stderr)
    try_again=input('Press enter n to stop')
    if try_again.lower()=='n':
        sys.exit() 














 