def start() -> int:
    # Asks the user to start or exit the program.
    user = input("Press 'enter' to 'begin' or type anything to 'exit'.")
    if user:
        print("Goodbye...")
        return 1
    return 0

def password_input() -> str:
    # Prompts the user to input a password.
    while True:
        try:
            pw = input("Type the password for testing: ")
            return pw
        except (KeyboardInterrupt, EOFError):
            print("\nPlease enter a valid password.")

def password_check(pw: str) -> tuple:
    # Logic to check the password strength. Returns a tuple with Boolean values for the evaluation.
    length = len(pw) >= 12
    number = any(char.isnumeric() for char in pw)
    upper_ch = any(char.isupper() for char in pw)
    lower_ch = any(char.islower() for char in pw)
    special_ch = any(not char.isalnum() for char in pw)

    count = sum([length, number, upper_ch, lower_ch, special_ch])
    return length, number, upper_ch, lower_ch, special_ch, count


def evaluation(checked_pw: tuple) -> None:
    #  Prints password strength evaluation.
    length, number, upper_ch, lower_ch, special_ch, count = checked_pw

    print("Password Strength Evaluation:")
    if count == 5:
        print("Your password is strong!")
    elif count == 4 and length:
        print("Your password is good! Here is an improvement you should make.")
    elif count == 4 and not length:
        print("Your password would be strong if you increase its length.")
    elif count == 3 and length:
        print("Your password is okay. Here are some improvements you should make.")
    elif count == 3 and not length:
        print("Your password would be strong if you increase its length.")
    elif count <= 2:
        print("\nYour password is very weak! You should make the following improvements!")

    if not length and count <= 2:
        print("- Increase the length of your password to at least 12 characters.")
    if not number:
        print("- Include at least one number character like '1, 2, 3 ...'")
    if not upper_ch:
        print("- Include at least one uppercase character like 'A, B, C ...'")
    if not lower_ch:
        print("- Include at least one lowercase character like 'a, b, c ...'")
    if not special_ch:
        print("- Include at least one special character like '@, !, $ ...'")

def main() -> int:
    print("Welcome! Here you can test the strength of your password.\n")
    if start():
        return 0
    
    pw = password_input()
    checked_pw = password_check(pw)
    evaluation(checked_pw)

if __name__ == "__main__":
    main()