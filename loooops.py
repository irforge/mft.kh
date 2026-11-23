digits = "0123456789"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = lower + upper
special = "!@#$%^&*()_+-=[]{};:'\",.<>/?\\|`~"

task = input("Task number (1-29): ")

# TASK 1
if task == "1":
    name = input("Name: ")
    if name == "":
        print("Error: name is empty")
    elif len(name) < 3:
        print("Error: name must have at least 3 characters")
    elif len(name) > 30:
        print("Error: name must have at most 30 characters")
    elif name.startswith(" "):
        print("Error: name cannot start with a space")
    elif name.endswith(" "):
        print("Error: name cannot end with a space")
    elif not set(name).isdisjoint(digits):
        print("Error: name cannot contain digits")
    elif not set(name).isdisjoint(special):
        print("Error: name cannot contain special characters")
    else:
        print("Valid name")

# TASK 2
elif task == "2":
    username = input("Username: ")
    if len(username) < 5:
        print("Error: username must have at least 5 characters")
    elif len(username) > 20:
        print("Error: username must have at most 20 characters")
    elif username[0] in digits:
        print("Error: username cannot start with a digit")
    elif " " in username:
        print("Error: username cannot contain spaces")
    elif not set(username).issubset(letters + digits + "_"):
        print("Error: only English letters, digits and _ are allowed")
    elif set(username).isdisjoint(letters):
        print("Error: username must have at least one letter")
    elif "admin" in username.lower():
        print('Error: username cannot contain "admin"')
    else:
        print("Valid username")

# TASK 3
elif task == "3":
    age = input("Age: ")
    if age == "":
        print("Error: age is empty")
    elif age.startswith("-"):
        print("Error: age cannot be negative")
    elif age.count(".") == 1 and age.replace(".", "").isdecimal():
        print("Error: age must be a whole number")
    elif not age.isdecimal():
        print("Error: age must contain only digits")
    elif int(age) < 13:
        print("Error: age cannot be less than 13")
    elif int(age) > 120:
        print("Error: age cannot be more than 120")
    else:
        print("Valid age:", int(age))

# TASK 4
elif task == "4":
    phone = input("Phone number: ")
    if phone == "":
        print("Error: phone number is empty")
    elif " " in phone:
        print("Error: phone number cannot contain spaces")
    elif "+" in phone:
        print("Error: phone number cannot contain +")
    elif "-" in phone:
        print("Error: phone number cannot contain -")
    elif len(phone) != 11:
        print("Error: phone number must have exactly 11 characters")
    elif not phone.isdigit():
        print("Error: phone number must contain only digits")
    elif not phone.startswith("09"):
        print("Error: phone number must start with 09")
    else:
        print("Valid phone number")

# TASK 5
elif task == "5":
    code = input("National code: ")
    if code == "":
        print("Error: national code is empty")
    elif " " in code:
        print("Error: national code cannot contain spaces")
    elif len(code) != 10:
        print("Error: national code must have exactly 10 digits")
    elif not code.isdigit():
        print("Error: national code must contain only digits")
    elif code == code[0] * 10:
        print("Error: digits cannot be identical")
    else:
        print("Valid national code")

# TASK 7
elif task == "7":
    phone1 = input("First phone number: ")
    phone2 = input("Second phone number: ")

    phone1_error = ""
    if phone1 == "":
        phone1_error = "first phone number is empty"
    elif " " in phone1:
        phone1_error = "first phone number cannot contain spaces"
    elif "+" in phone1:
        phone1_error = "first phone number cannot contain +"
    elif "-" in phone1:
        phone1_error = "first phone number cannot contain -"
    elif len(phone1) != 11:
        phone1_error = "first phone number must have 11 characters"
    elif not phone1.isdigit():
        phone1_error = "first phone number must contain only digits"
    elif not phone1.startswith("09"):
        phone1_error = "first phone number must start with 09"

    phone2_error = ""
    if phone2 == "":
        phone2_error = "second phone number is empty"
    elif " " in phone2:
        phone2_error = "second phone number cannot contain spaces"
    elif "+" in phone2:
        phone2_error = "second phone number cannot contain +"
    elif "-" in phone2:
        phone2_error = "second phone number cannot contain -"
    elif len(phone2) != 11:
        phone2_error = "second phone number must have 11 characters"
    elif not phone2.isdigit():
        phone2_error = "second phone number must contain only digits"
    elif not phone2.startswith("09"):
        phone2_error = "second phone number must start with 09"

    if phone1_error + phone2_error != "":
        if phone1_error != "":
            print("Error:", phone1_error)
        if phone2_error != "":
            print("Error:", phone2_error)
    elif phone1 == phone2:
        print("Error: the two phone numbers are the same")
    else:
        print("Both phone numbers are valid and different")

# TASK 8
elif task == "8":
    email = input("Email: ")
    after_at = email.split("@")[-1]
    if email == "":
        print("Error: email is empty")
    elif " " in email:
        print("Error: email cannot contain spaces")
    elif email.count("@") != 1:
        print("Error: email must have exactly one @")
    elif email.startswith("@"):
        print("Error: email cannot start with @ (nothing before @)")
    elif email.endswith("@"):
        print("Error: email cannot end with @ (nothing after @)")
    elif "." not in after_at:
        print("Error: there must be a . after @")
    elif email.startswith("."):
        print("Error: email cannot start with .")
    elif email.endswith("."):
        print("Error: email cannot end with .")
    else:
        print("Valid email")
        
# TASK 10
elif task == "10":
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    age = input("Age: ")
    city = input("City: ")

    missing = 0
    errors = 0
    after_at = email.split("@")[-1]

    if first_name == "":
        missing = missing + 1
        print("First name: missing")
    elif len(first_name) < 2:
        errors = errors + 1
        print("First name: at least 2 characters are required")
    elif not set(first_name).isdisjoint(digits):
        errors = errors + 1
        print("First name: digits are not allowed")
    elif not set(first_name).isdisjoint(special):
        errors = errors + 1
        print("First name: special characters are not allowed")

    if last_name == "":
        missing = missing + 1
        print("Last name: missing")
    elif len(last_name) < 2:
        errors = errors + 1
        print("Last name: at least 2 characters are required")
    elif not set(last_name).isdisjoint(digits):
        errors = errors + 1
        print("Last name: digits are not allowed")
    elif not set(last_name).isdisjoint(special):
        errors = errors + 1
        print("Last name: special characters are not allowed")

    if phone == "":
        missing = missing + 1
        print("Phone number: missing")
    elif not phone.isdigit():
        errors = errors + 1
        print("Phone number: only digits are allowed")
    elif len(phone) != 11:
        errors = errors + 1
        print("Phone number: exactly 11 digits are required")
    elif not phone.startswith("09"):
        errors = errors + 1
        print("Phone number: must start with 09")

    if email == "":
        missing = missing + 1
        print("Email: missing")
    elif " " in email:
        errors = errors + 1
        print("Email: spaces are not allowed")
    elif email.count("@") != 1:
        errors = errors + 1
        print("Email: exactly one @ is required")
    elif "." not in after_at:
        errors = errors + 1
        print("Email: a . is required after @")

    if age == "":
        missing = missing + 1
        print("Age: missing")
    elif not age.isdecimal():
        errors = errors + 1
        print("Age: only digits are allowed")
    elif int(age) < 13 or int(age) > 120:
        errors = errors + 1
        print("Age: must be between 13 and 120")

    if city == "":
        missing = missing + 1
        print("City: missing")
    elif len(city) < 2:
        errors = errors + 1
        print("City: at least 2 characters are required")
    elif not set(city).isdisjoint(digits):
        errors = errors + 1
        print("City: digits are not allowed")

    if errors > 0:
        print("Status: validation error")
    elif missing > 0:
        print("Status: incomplete")
    else:
        print("Status: valid")

# TASK 11
elif task == "11":
    username = input("Username: ")
    password = input("Password: ")

    username_error = ""
    if len(username) < 5:
        username_error = "username must have at least 5 characters"
    elif len(username) > 20:
        username_error = "username must have at most 20 characters"
    elif " " in username:
        username_error = "username cannot contain spaces"

    password_error = ""
    if len(password) < 8:
        password_error = "password must have at least 8 characters"
    elif set(password).isdisjoint(letters):
        password_error = "password must have at least one letter"
    elif set(password).isdisjoint(digits):
        password_error = "password must have at least one digit"
    elif " " in password:
        password_error = "password cannot contain spaces"

    if username_error + password_error == "":
        print("Registration successful")
    else:
        if username_error != "":
            print("Error:", username_error)
        if password_error != "":
            print("Error:", password_error)

# TASK 12
elif task == "12":
    password = input("Password: ")
    errors = 0
    if len(password) < 8:
        print("Error: at least 8 characters are required")
        errors = errors + 1
    if len(password) > 30:
        print("Error: at most 30 characters are allowed")
        errors = errors + 1
    if set(password).isdisjoint(letters):
        print("Error: at least one English letter is required")
        errors = errors + 1
    if set(password).isdisjoint(digits):
        print("Error: at least one digit is required")
        errors = errors + 1
    if set(password).isdisjoint(upper):
        print("Error: at least one uppercase letter is required")
        errors = errors + 1
    if set(password).isdisjoint(lower):
        print("Error: at least one lowercase letter is required")
        errors = errors + 1
    if set(password).isdisjoint(special):
        print("Error: at least one special character is required")
        errors = errors + 1
    if " " in password:
        print("Error: spaces are not allowed")
        errors = errors + 1
    if errors == 0:
        print("Strong password")

# TASK 13
elif task == "13":
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    errors = 0

    if len(password) < 8:
        print("Error: password must have at least 8 characters")
        errors = errors + 1
    if len(password) > 30:
        print("Error: password must have at most 30 characters")
        errors = errors + 1
    if set(password).isdisjoint(letters):
        print("Error: password must have an English letter")
        errors = errors + 1
    if set(password).isdisjoint(digits):
        print("Error: password must have a digit")
        errors = errors + 1
    if set(password).isdisjoint(upper):
        print("Error: password must have an uppercase letter")
        errors = errors + 1
    if set(password).isdisjoint(lower):
        print("Error: password must have a lowercase letter")
        errors = errors + 1
    if set(password).isdisjoint(special):
        print("Error: password must have a special character")
        errors = errors + 1
    if " " in password:
        print("Error: password cannot contain spaces")
        errors = errors + 1

    confirm_ok = (8 <= len(confirm_password) <= 30
                  and not set(confirm_password).isdisjoint(letters)
                  and not set(confirm_password).isdisjoint(digits)
                  and not set(confirm_password).isdisjoint(upper)
                  and not set(confirm_password).isdisjoint(lower)
                  and not set(confirm_password).isdisjoint(special)
                  and " " not in confirm_password)
    if not confirm_ok:
        print("Error: confirm password is not valid")
        errors = errors + 1

    if password != confirm_password:
        print("Error: password and confirm password do not match")
        errors = errors + 1
    if password == username:
        print("Error: password cannot be the same as username")
        errors = errors + 1

    if errors == 0:
        print("Password confirmed successfully")

# TASK 14
elif task == "14":
    username = input("Username: ")
    password = input("Password: ")
    common_passwords = ("12345678", "password", "123456789", "qwerty",
                        "abcdefgh")
    errors = 0

    if len(password) < 8:
        print("Reason: password has less than 8 characters")
        errors = errors + 1
    if password.isdigit():
        print("Reason: password contains only digits")
        errors = errors + 1
    if password.isalpha():
        print("Reason: password contains only letters")
        errors = errors + 1
    if " " in password:
        print("Reason: password contains a space")
        errors = errors + 1
    if password == username:
        print("Reason: password is the same as username")
        errors = errors + 1
    if password.lower() in common_passwords:
        print("Reason: password is too common")
        errors = errors + 1

    if errors == 0:
        print("Password is acceptable")
    else:
        print("Weak password")

# TASK 15
elif task == "15":
    correct_username = "ali_dev"
    correct_password = "Ali@1234"
    username = input("Username: ")
    password = input("Password: ")
    if username == "":
        print("Username not entered.")
    elif password == "":
        print("Password not entered.")
    elif username != correct_username:
        print("Wrong username.")
    elif password != correct_password:
        print("Wrong password.")
    else:
        print("Login successful.")

# TASK 16
elif task == "16":
    correct_otp = "583214"
    otp = input("OTP: ")
    if otp == "":
        print("Error: OTP is empty")
    elif len(otp) != 6:
        print("Error: OTP must have exactly 6 characters")
    elif not otp.isdigit():
        print("Error: OTP must contain only digits")
    elif otp != correct_otp:
        print("Error: OTP is incorrect")
    else:
        print("OTP is correct")

# TASK 17
elif task == "17":
    correct_otp = "583214"
    phone = input("Phone number: ")
    otp = input("OTP: ")

    phone_error = ""
    if phone == "":
        phone_error = "phone number is empty"
    elif len(phone) != 11:
        phone_error = "phone number must have exactly 11 digits"
    elif not phone.isdigit():
        phone_error = "phone number must contain only digits"
    elif not phone.startswith("09"):
        phone_error = "phone number must start with 09"

    otp_error = ""
    if otp == "":
        otp_error = "OTP is empty"
    elif len(otp) != 6:
        otp_error = "OTP must have exactly 6 characters"
    elif not otp.isdigit():
        otp_error = "OTP must contain only digits"
    elif otp != correct_otp:
        otp_error = "OTP is incorrect"

    if phone_error + otp_error == "":
        print("Authentication successful")
    else:
        if phone_error != "":
            print("Error:", phone_error)
        if otp_error != "":
            print("Error:", otp_error)

# TASK 18
elif task == "18":
    pin = input("PIN: ")
    if pin == "":
        print("Error: PIN is empty")
    elif len(pin) != 4:
        print("Error: PIN must have exactly 4 characters")
    elif not pin.isdigit():
        print("Error: PIN must contain only digits")
    elif pin == pin[0] * 4:
        print("Error: the four digits cannot be identical")
    elif pin in ("0000", "1111", "1234", "4321"):
        print("Error: this PIN is not allowed")
    else:
        print("Valid PIN")

# TASK 19
elif task == "19":
    saved_pin = "2580"
    current_pin = input("Current PIN: ")
    new_pin = input("New PIN: ")
    confirm_pin = input("Confirm new PIN: ")
    errors = 0

    if current_pin != saved_pin:
        print("Error: current PIN is incorrect")
        errors = errors + 1

    new_error = ""
    if new_pin == "":
        new_error = "new PIN is empty"
    elif len(new_pin) != 4:
        new_error = "new PIN must have exactly 4 characters"
    elif not new_pin.isdigit():
        new_error = "new PIN must contain only digits"
    elif new_pin == new_pin[0] * 4:
        new_error = "the four digits cannot be identical"
    elif new_pin in ("0000", "1111", "1234", "4321"):
        new_error = "this PIN is not allowed"

    if new_error != "":
        print("Error:", new_error)
        errors = errors + 1
    elif new_pin == current_pin:
        print("Error: new PIN cannot be the same as current PIN")
        errors = errors + 1

    if new_pin != confirm_pin:
        print("Error: new PIN and confirm PIN do not match")
        errors = errors + 1

    if errors == 0:
        saved_pin = new_pin
        print("PIN changed successfully")
        print("Saved PIN is now:", saved_pin)

# TASK 20
elif task == "20":
    correct_username = "ali_dev"
    correct_password = "Ali@1234"
    attempts = 0
    logged_in = False

    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password:
        logged_in = True
        print("Login successful")
    else:
        attempts = attempts + 1
        print("Wrong login. Attempts:", attempts, "of 3")

    if not logged_in:
        username = input("Username: ")
        password = input("Password: ")
        if username == correct_username and password == correct_password:
            logged_in = True
            print("Login successful")
        else:
            attempts = attempts + 1
            print("Wrong login. Attempts:", attempts, "of 3")

    if not logged_in:
        username = input("Username: ")
        password = input("Password: ")
        if username == correct_username and password == correct_password:
            logged_in = True
            print("Login successful")
        else:
            attempts = attempts + 1
            print("Wrong login. Attempts:", attempts, "of 3")

    if attempts == 3:
        print("Account status: LOCKED (3 failed attempts)")
    else:
        print("Account status: active")

# TASK 21
elif task == "21":
    print("*" * 20)
    print("        MENU")
    print("*" * 20)
    print("1. View balance")
    print("2. Buy charge")
    print("3. Transfer money")
    print("4. Pay bill")
    print("5. Exit")
    choice = input("Your choice: ")
    if choice == "":
        print("Error: input is empty")
    elif not choice.isdigit():
        print("Error: only numbers are allowed")
    elif choice not in ("1", "2", "3", "4", "5"):
        print("Error: choice must be between 1 and 5")
    elif choice == "1":
        print("You chose: View balance")
    elif choice == "2":
        print("You chose: Buy charge")
    elif choice == "3":
        print("You chose: Transfer money")
    elif choice == "4":
        print("You chose: Pay bill")
    else:
        print("You chose: Exit")

# TASK 22
elif task == "22":
    print("1. Hamrah Aval")
    print("2. Irancell")
    print("3. Rightel")
    operator = input("Operator: ")
    amount = input("Amount (Toman): ")

    operator_error = ""
    if operator not in ("1", "2", "3"):
        operator_error = "operator must be 1, 2 or 3"

    amount_error = ""
    if amount == "":
        amount_error = "amount is empty"
    elif not amount.isdecimal():
        amount_error = "amount must contain only digits"
    elif int(amount) <= 0:
        amount_error = "amount must be greater than zero"
    elif int(amount) < 1000:
        amount_error = "amount must be at least 1000 Toman"
    elif int(amount) > 100000:
        amount_error = "amount must be at most 100000 Toman"

    if operator_error + amount_error == "":
        if operator == "1":
            operator_name = "Hamrah Aval"
        elif operator == "2":
            operator_name = "Irancell"
        else:
            operator_name = "Rightel"
        print(operator_name, "charge purchased:", int(amount), "Toman")
    else:
        if operator_error != "":
            print("Error:", operator_error)
        if amount_error != "":
            print("Error:", amount_error)

# TASK 23
elif task == "23":
    my_phone = "09121234567"
    balance = 500000
    correct_pin = "2580"
    print("Your balance:", balance)
    destination = input("Destination number: ")
    amount = input("Amount: ")
    pin = input("PIN: ")

    destination_error = ""
    if destination == "":
        destination_error = "destination number is empty"
    elif not destination.isdigit():
        destination_error = "destination must contain only digits"
    elif len(destination) != 11:
        destination_error = "destination must have exactly 11 digits"
    elif not destination.startswith("09"):
        destination_error = "destination must start with 09"
    elif destination == my_phone:
        destination_error = "destination cannot be your own number"

    amount_error = ""
    if amount == "":
        amount_error = "amount is empty"
    elif not amount.isdecimal():
        amount_error = "amount must contain only digits"
    elif int(amount) <= 0:
        amount_error = "amount must be greater than zero"
    elif int(amount) > balance:
        amount_error = "amount is more than your balance"

    pin_error = ""
    if pin == "":
        pin_error = "PIN is empty"
    elif len(pin) != 4:
        pin_error = "PIN must have exactly 4 digits"
    elif not pin.isdigit():
        pin_error = "PIN must contain only digits"
    elif pin != correct_pin:
        pin_error = "PIN is incorrect"

    if destination_error + amount_error + pin_error == "":
        balance = balance - int(amount)
        print("Transfer completed")
        print("New balance:", balance)
    else:
        if destination_error != "":
            print("Error:", destination_error)
        if amount_error != "":
            print("Error:", amount_error)
        if pin_error != "":
            print("Error:", pin_error)

# TASK 24
elif task == "24":
    bill_id = input("Bill ID: ")
    payment_id = input("Payment ID: ")

    bill_error = ""
    if bill_id == "":
        bill_error = "bill ID is empty"
    elif " " in bill_id:
        bill_error = "bill ID cannot contain spaces"
    elif not bill_id.isdigit():
        bill_error = "bill ID must contain only digits"
    elif len(bill_id) < 6:
        bill_error = "bill ID must have at least 6 digits"
    elif len(bill_id) > 15:
        bill_error = "bill ID must have at most 15 digits"

    payment_error = ""
    if payment_id == "":
        payment_error = "payment ID is empty"
    elif " " in payment_id:
        payment_error = "payment ID cannot contain spaces"
    elif not payment_id.isdigit():
        payment_error = "payment ID must contain only digits"
    elif len(payment_id) < 6:
        payment_error = "payment ID must have at least 6 digits"
    elif len(payment_id) > 15:
        payment_error = "payment ID must have at most 15 digits"

    if bill_error + payment_error != "":
        if bill_error != "":
            print("Error:", bill_error)
        if payment_error != "":
            print("Error:", payment_error)
    elif bill_id == payment_id:
        print("Error: bill ID and payment ID cannot be the same")
    else:
        print("Bill payment information is valid")

# TASK 25
elif task == "25":
    print("Main menu")
    print("1. Account")
    print("2. Services")
    print("3. Payment")
    print("4. Exit")
    choice = input("Your choice: ")
    if choice == "":
        print("Error: input is empty")
    elif not choice.isdigit():
        print("Error: only numbers are allowed")
    elif choice not in ("1", "2", "3", "4"):
        print("Error: choice is out of range (1-4)")
    elif choice == "1":
        print("Account menu")
        print("1. View balance")
        print("2. View transactions")
        print("3. Change PIN")
        sub = input("Your choice: ")
        if sub == "":
            print("Error: input is empty")
        elif not sub.isdigit():
            print("Error: only numbers are allowed")
        elif sub not in ("1", "2", "3"):
            print("Error: choice is out of range (1-3)")
        elif sub == "1":
            print("Showing balance...")
        elif sub == "2":
            print("Showing transactions...")
        else:
            print("Changing PIN...")
    elif choice == "2":
        print("Services menu")
        print("1. Buy charge")
        print("2. Transfer money")
        print("3. Back")
        sub = input("Your choice: ")
        if sub == "":
            print("Error: input is empty")
        elif not sub.isdigit():
            print("Error: only numbers are allowed")
        elif sub not in ("1", "2", "3"):
            print("Error: choice is out of range (1-3)")
        elif sub == "1":
            print("Buying charge...")
        elif sub == "2":
            print("Transferring money...")
        else:
            print("Going back to the main menu")
    elif choice == "3":
        print("Payment menu")
        print("1. Pay bill")
        print("2. Pay internet")
        print("3. Back")
        sub = input("Your choice: ")
        if sub == "":
            print("Error: input is empty")
        elif not sub.isdigit():
            print("Error: only numbers are allowed")
        elif sub not in ("1", "2", "3"):
            print("Error: choice is out of range (1-3)")
        elif sub == "1":
            print("Paying bill...")
        elif sub == "2":
            print("Paying internet...")
        else:
            print("Going back to the main menu")
    else:
        print("Goodbye")

# TASK 26
elif task == "26":
    contact1_name = "Ali"
    contact1_phone = "09121111111"
    contact2_name = "Sara"
    contact2_phone = "09122222222"
    contact3_name = "Reza"
    contact3_phone = "09123333333"

    search = input("Name to search: ")
    search = search.strip().lower()
    if search == "":
        print("Error: name is empty")
    elif search == contact1_name.lower():
        print("Phone number:", contact1_phone)
    elif search == contact2_name.lower():
        print("Phone number:", contact2_phone)
    elif search == contact3_name.lower():
        print("Phone number:", contact3_phone)
    else:
        print("Contact not found")

# TASK 28
elif task == "28":
    contact1 = "Ali"
    contact2 = "Sara"
    contact3 = "Reza"
    name = input("Contact name to delete: ")
    name = name.strip().lower()
    found = name in (contact1.lower(), contact2.lower(), contact3.lower())

    if name == "":
        print("Error: name is empty")
    elif not found:
        print("Contact not found")
    else:
        print("Are you sure you want to delete the contact?")
        answer = input("y / n: ")
        if answer == "y" or answer == "Y":
            print("Contact deleted.")
        elif answer == "n" or answer == "N":
            print("Operation canceled.")
        else:
            print("Error: invalid input (only y, Y, n, N are allowed)")
