secret_number = 9
guess_count = 0
while guess_count < 3:
       guess = int(input("Guess: "))
       guess_count = guess_count+1
       if guess == secret_number:
           print("congo!! you won!")
           break
else:
           print("wrong attempted!")
