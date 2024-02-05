import sys

def start() -> int:
    user = input("Press 'enter' to 'begin' or type anything to 'exit'.")
    if user != "":
        print("Goodbye...")
        sys.exit()
    return 0


def password_inpout() -> str:
    pw = input("Type the password for testing: ")
    return pw


def password_check(pw: str) -> tuple:
    length = False
    number = False
    upper_ch = False
    lower_ch = False
    special_ch = False
    count = 0

    if len(pw) >= 12:
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


def evaluation(checked_pw: tuple) -> int:
    length, number, upper_ch, lower_ch, special_ch, count = checked_pw

    if count == 5:
        print("Your password is strong!")
    elif count == 4 and length:
        print("Your password is good!\nHere is an improvement you should make.")
    elif count == 4 and not length:
        print("Your password would be strong, if you ...")
    elif count == 3 and length:
        print("Your password is okay. Here are some improvements you should make.")
    elif count == 3 and not length:
        print("Your password would be strong, if you ...")
    elif count <= 2:
        print("\nYour password is very weak! You should make the following improvements!")

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


def main() -> int:
    print("Welcome! Here you can test the strength of your password.\n")
    start()
    pw = password_inpout()
    checked_pw = password_check(pw)
    eval = evaluation(checked_pw)


if __name__ == "__main__":
    main()