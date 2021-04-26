import random
word_list = ["arward","baboon","camel"]
chosen_word = random.choice(word_list)

guess = input(" Guess a word : ").lower()

display =[]
# for letter in chosen_word:             #  the same output
for _ in range (len(chosen_word)) :      # the same output
       display +="-"                     #  add dash _ into display
print(display)       


# print(f"Pssst, the solution is {chosen_word")
# for letter in chosen_word:
#     if letter == guess :
#         print(" Right ! ")
#     else :
#         print("wrong !")    
    
