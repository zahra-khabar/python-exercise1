import string

# ---------------Password Strength Checker Program-----------------
username = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()
birthday = input("Enter your birthday year:").strip()

score = 7
failed_check =[]

#Check if inputs are empty or not
if not username:
    score -= 1
    failed_check.append("Username not be empty.")
if not password:
    score -= 1
    failed_check.append("Password not be empty.")
if not birthday:
    score -= 1
    failed_check.append("Birthday not be empty.")


#Rule 1 ---> Password Length
if len(password) <8:
    score -= 1
    failed_check.append("Password must be longer than 8 characters.")

#Rule 2 ---> Special Char and at least English Alphabet
special_char = {"!", "@", "$"}

has_special = False
has_letter = False

for char in password:
    if char in special_char:
        has_special = True

    if char in string.ascii_letters:
        has_letter = True

if not has_special or not has_letter:
    score -= 1

    if not has_special:
        failed_check.append("Password must contain at least one special character (!,@,$).")

    if not has_letter:
        failed_check.append("Password must contain at least one English letter.")

# Rule 3 -----> password != username
if password == username:
    score -= 1
    failed_check.append("Password cannot be the same as username.")


# Rule 4 -----> Lower & Upper ----> یکی از شروط باید درست باشه
if password.islower():
    score -= 1
    failed_check.append("Password cannot be all lowercase.")

elif password.isupper():
    score -= 1
    failed_check.append("Password cannot be all uppercase.")

# Rule 5 -----> SwapCase
if password == username.swapcase():
    score -= 1
    failed_check.append("Password is swapcase version of Your username.")

# Rule 6
char_replacement = {
    "a": "@",
    "i": "!",
    "s": "$",
    "o": "0"
}
new_username = ""
for char in username.lower():
    if char in char_replacement:
        new_username += char_replacement[char]
    else:
        new_username += char
if new_username == username.lower():
    score -=1
    failed_check.append("Password contains symbol replacements like @  ! $ 0")

# Rule 7 ----> common password
common_password = [
    "12345",
    "123456",
    "12345678",
    "123456789",
    "111111",
    "qwerty",
    "asdfgh",
    "zxcvbnm",
    "password",
    "admin",
    "p@s$w0rd"
]
if password.lower() in common_password:
    score -= 1
    failed_check.append("Password is too common or similar to 'password'.")

# Rule 8 ----> check birthday year is in password
if birthday in password:
    score -= 1
    failed_check.append("Password contains your birth year.")

# Password level
level = ""
if score >= 6:
    level ="Very Strong"
elif score >= 5:
    level ="Strong"
elif score >= 3:
    level ="Medium"
else:
    level = "Weak"

#---------------------------------------------
# خروجی
print("\n Password Strength:"f"{score}/7")
print(f" Level: {level} ")

if failed_check:
    print("\n Failed Checks:")
    for i in failed_check:
        print("-",i)
else:
    print("\n Your Password is Passed All Checks:")
