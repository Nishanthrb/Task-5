# ================= BREAK STATEMENT (FOR LOOP) =================

# 1. Print numbers from 1 to 20 and stop when the number is 10
for i in range(1, 21):
    print(i)
    if i == 10:
        break

# 2. Password checker
correct_password = "python123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break

# 3. Accept numbers and stop when user enters 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break

# 4. Search for a specific element in a list
numbers = [5, 10, 15, 20, 25]
target = 15
for num in numbers:
    if num == target:
        print("Found:", target)
        break

# 5. Print numbers from 1 to 100 and stop at first multiple of 17
for i in range(1, 101):
    print(i)
    if i % 17 == 0:
        break

# 6. Menu-driven program
while True:
    print("1. Start")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == "2":
        print("Exiting...")
        break

# 7. Keep asking until user enters quit
while True:
    text = input("Enter text: ")
    if text.lower() == "quit":
        break

# 8. Find first even number in a list
numbers = [1, 3, 5, 8, 10]
for num in numbers:
    if num % 2 == 0:
        print("First even:", num)
        break

# ================= CONTINUE STATEMENT (FOR LOOP) =================

# 1. Print numbers from 1 to 20, skipping 10
for i in range(1, 21):
    if i == 10:
        continue
    print(i)

# 2. Print only odd numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)

# 3. Print only even numbers from 1 to 50
for i in range(1, 51):
    if i % 2 != 0:
        continue
    print(i)

# 4. Print numbers from 1 to 100, skipping multiples of 5
for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i)

# 5. Print all letters except vowels
name = "PythonProgramming"
for ch in name:
    if ch.lower() in "aeiou":
        continue
    print(ch)

# 6. Print numbers from 1 to 30, skipping multiples of 3
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)

# 7. Print all elements except negative numbers
numbers = [5, -2, 8, -1, 10]
for num in numbers:
    if num < 0:
        continue
    print(num)

# 8. Print numbers from 1 to 20, skipping even numbers
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

# ================= PASS STATEMENT =================

# 1. Empty function
def student_details():
    pass

# 2. Empty class
class Employee:
    pass

# 3. While loop with pass
count = 1
while count <= 5:
    pass
    count += 1

# 4. For loop with pass
for i in range(5):
    pass

# 5. Placeholder calculator function
def calculator():
    pass

# 6. Placeholder class
class BankAccount:
    pass

# 7. Menu structure
choice = 1
if choice == 1:
    pass
elif choice == 2:
    pass

# 8. Empty if block
x = 10
if x > 5:
    pass

# ================= MIXED TASKS =================

# 1. Skip multiples of 4 and stop at 40
for i in range(1, 51):
    if i % 4 == 0:
        continue
    if i == 40:
        break
    print(i)

# 2. Login system (3 attempts)
correct_user = "admin"
correct_pass = "1234"
for attempt in range(3):
    user = input("Username: ")
    pwd = input("Password: ")
    if user == correct_user and pwd == correct_pass:
        print("Login Successful")
        break

# 3. Skip multiples of 10 and stop at 75
for i in range(1, 101):
    if i % 10 == 0:
        continue
    if i == 75:
        break
    print(i)

# 4. ATM menu
while True:
    print("1. Balance")
    print("2. Deposit")
    print("3. Exit")
    choice = input("Choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        break

# 5. Skip even numbers and stop at 25
for i in range(1, 31):
    if i % 2 == 0:
        continue
    if i == 25:
        break
    print(i)

# ================= WHILE LOOP - BREAK =================

# 1. Stop at 5
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

# 2. Stop at 15
i = 1
while i <= 20:
    print(i)
    if i == 15:
        break
    i += 1

# 3. Stop when user enters 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break

# 4. Password checker
correct_password = "python123"
while True:
    password = input("Password: ")
    if password == correct_password:
        print("Correct Password")
        break

# 5. Stop at 50
i = 1
while i <= 100:
    print(i)
    if i == 50:
        break
    i += 1

# ================= WHILE LOOP - CONTINUE =================

# 1. Skip 5
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

# 2. Skip 10
i = 0
while i < 20:
    i += 1
    if i == 10:
        continue
    print(i)

# 3. Only odd numbers
i = 0
while i < 20:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 4. Only even numbers
i = 0
while i < 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# 5. Skip multiples of 3
i = 0
while i < 30:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

# ================= WHILE LOOP - PASS =================

# 1. While loop with pass
i = 1
while i <= 5:
    pass
    i += 1

# 2. Use pass when number is 3
i = 1
while i <= 5:
    if i == 3:
        pass
    else:
        print(i)
    i += 1

# 3. Empty while loop
i = 0
while i < 5:
    pass
    i += 1

# 4. Pass inside if
i = 1
while i <= 5:
    if i == 2:
        pass
    else:
        print(i)
    i += 1

# 5. Placeholder program
running = True
while running:
    pass
    running = False

# ================= WHILE LOOP - MIXED =================

# 1. Skip 5 and stop at 15
i = 0
while i < 20:
    i += 1
    if i == 5:
        continue
    if i == 15:
        break
    print(i)

# 2. Skip multiples of 4 and stop at 25
i = 0
while i < 30:
    i += 1
    if i % 4 == 0:
        continue
    if i == 25:
        break
    print(i)

# 3. Login system using break
correct_password = "admin123"
while True:
    password = input("Enter Password: ")
    if password == correct_password:
        print("Login Successful")
        break

# 4. Print only odd numbers
i = 0
while i < 20:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 5. Menu program
while True:
    print("1. Add")
    print("2. Delete")
    print("3. Exit")
    choice = input("Choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        break
