#Import random module
#Thank you for checking out my code
import random

#change "generated password.txt" to your own choosing or use the provided txt file
password_storage = open("generated password.txt", "a")

#password characters
char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

def password_gen():
    while True:
        password_len = int(input("How many characters do you want?: "))
        save_conf = input("Do you want to save the file. y/n: ")
        password_final = ""
        for i in range(0, password_len):
            rand_char = random.choice(char)
            password_final += rand_char

        #if the user input = "y" then the program will ask the user for the purpose and save the details
        #if the user input ="n" then it will print out the password immediately
        if save_conf == "y":
            purpose = input("What's the password for?: ").upper()
            password_storage.write("//NEW PASSWORD//\nPurpose: {}\nPassword: {}".format(purpose, password_final))
            password_storage.write("\n\n")

        print("Here's your password: " + password_final + "\n")

        return

password_gen()
