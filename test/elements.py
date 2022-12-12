# # def even_odd(a):
# #     next_even,next_odd=0,len(a)-1
# #     while next_even < next_odd:
# #         if a[next_even]%2==0:
# #             next_even+=1
# #         else:
# #             a[next_even,a[next_odd]]=a[next_odd],a[next_even]
# #             next_odd-=1
# # even_odd(7)
# # i =1
# # while i< 7:
# #     i+=1
# #     if i ==4:
# #         continue
# #     print(i)

# # import sys
# # print(sys.version.split()[0])
# # numbers = [1, 2, 3, 4, 2, 5]

# # # check if numbers is instance of list
# # result = isinstance(numbers, list)
# # print(result)
# # def is_all_eaqual(iterator):
# #     return len(set(iterator))<=1
# # is_all_eaqual({1.0, (1, 2, 3), 'Hello'})

# # def swap_elements(new_list):
# #     (new_list[0],new_list[-1])=(new_list[-1],new_list[0])
# #     return new_list
# # swap_elements([3,5,6,7,8])

# # def reversed_word(x):
# #     return x.rever
# import sys,random
# print('Welocme to the syche game of wining the best name')
# firt=('megga','wex','tina','max')
# last=('landmere','kuria','landia','rabbitman')
# while True:
#     firstname=random.choice(firt)
#     lastname =random.choice(last)
#     print('\n\n')
#     print('{}{}'.format(firstname,lastname),file=sys.stderr)
#     print('\n\n')
#     try_again=input('\n\n Try again?(Press Enter else n to quit)\n')
#     if try_again.lower() =='n':
#         break
#     input('\n Press Enter to exit')
# import math
# def circ(r):
#     '''Return the cirmfrence of the circle with the radius 
#     r = radius
#     c=Cirmfrence of the circle
#     '''
#     c=2*r*math.pi
#     return c
# circ(7)

# """Program to word  pig latin"""
# import sys
# Vowel='aeoiu'
# while True:
#     word= input('Enter any word and get latin pig')
#     if word[0] in Vowel:
#         pig_latin = word + 'way'
#     else:
#         pig_latin =word[1:] + word[0] + 'ay'
#     print()
#     print('{}'.format(pig_latin),file=sys.stderr)
#     try_again=input('Press enter n to stop')
#     if try_again.lower()=='n':
#         sys.exit()

# """Load a text file  a list 
# Arguments:
# ­text file name (and directory path, if needed)
# Exceptions:
# ­IOError if filename not found.
# Returns:
# ­A list of all words in a text file in lower case.
# Requires­import sys


# """
# import sys
# def  load(file):
#     '''open a text file and return a list of lowercase'''
#     try:
#         with open(file) as in_file:
#             loaded_txt=in_file.read().strip().split('\n')
#             loaded_txt =[x.lower() for x in loaded_txt]
#             return loaded_txt
#     except IOError as e:
#         print('{}\nerroer opening{}Terming the program'.format(e,file))
#         sys.exit(1)

# """Testing something palinderone strategy """
# word='Nurses'
# print(word[:])
# print(word[::-1])
"""Finding the palindromes in a list of words"""
word_list=('Jane','kelly','enaJ','Nurses','sesruN')
pali_list=[]
for word in word_list:
     if len(word)> 1 and word ==word[::-1]:
        pali_list.append(word)
print('The number of words are {}'.format(len(pali_list)))
print(pali_list,sep='\n')