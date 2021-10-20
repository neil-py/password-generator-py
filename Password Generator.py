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
        purpose = input("What's the password for?: ").upper()
        password_final = ""
        for i in range(0, password_len):
            rand_char = random.choice(char)
            password_final += rand_char
        print("Here's your password: " + password_final + "\n")
        if save_conf == "y":
            password_storage.write("//NEW PASSWORD//\nPurpose: {}\nPassword: {}".format(purpose, password_final))
            password_storage.write("\n\n")
            return

password_gen()
