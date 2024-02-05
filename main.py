import sys

def start():
    user = input("Press 'enter' to 'begin' or type anything to 'exit'.")
    if user != "":
        print("Goodbye...")
        sys.exit()
    return 0


def password_inpout():
    pw = input("Type the password for testing: ")
    return pw


def password_check(pw):
    length = False
    number = False
    upper_ch = False
    lower_ch = False
    special_ch = False
    count = 0

    if len(pw) > 12:
        length = True
    
    for i in pw:
        if i.isnumeric():
            number = True
        if i.isupper():
            upper_ch = True
        if i.islower():
            lower_ch = True
        if not i.isnumeric() and not i.isalpha():
            special_ch = True

    if length:
        count += 1
    if number:
        count += 1
    if upper_ch:
        count += 1
    if lower_ch:
        count += 1
    if special_ch:
        count += 1
        
    return (length, number, upper_ch, lower_ch, special_ch, count)


def evaluation(checked_pw):
    length, number, upper_ch, lower_ch, special_ch, count = checked_pw

    if count == 5:
        print("Your password is strong!\n")
    elif count == 4:
        print("Your password is good!\nHere are some improvements you could make.\n")
    elif count == 3:
        print("Your password is okay!\nHere are some improvements you could make.\n")
    elif count == 2:
        print("Your password is weak!\nHere are some improvements you should make.\n")
    elif count == 1:
        print("Your password is very weak!\nHere are some improvements you should make.\n")
    elif count == 0:
        print("Your password is extremely weak!\nHere are some improvements you should make.\n")

    if not length:
        print("- Increase the length of your password to atleast 12 characters.")
    if not number:
        print("- Include atleast one number character like '1, 2, 3 ...'")
    if not upper_ch:
        print("- Include atleast one uppercase character like 'A, B, C ...'")
    if not lower_ch:
        print("- Include atleast one lowercase character like 'a, b, c ...'")
    if not special_ch:
        print("- Include atleast one special character like '@, $, % ...'")


def main():
    print("Welcome! Here you can test the strength of your password.\n")
    start()
    pw = password_inpout()
    checked_pw = password_check(pw)
    eval = evaluation(checked_pw)


if __name__ == "__main__":
    main()