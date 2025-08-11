# july_2025_python_tasks.py

# 1️⃣ Program: Accepts user input to create a list of integers & compute the sum
numbers = input("Enter integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
print("Sum of the integers:", sum(numbers))

print("-" * 40)

# 2️⃣ Program: Tuple of favorite books & printing each
favorite_books = ("Atomic Habits", "Rich Dad Poor Dad", "The Alchemist", "Sapiens", "Deep Work")
print("My Favorite Books:")
for book in favorite_books:
    print(book)

print("-" * 40)

# 3️⃣ Program: Dictionary to store person's info
person = {}
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")
print("Person Information:", person)

print("-" * 40)

# 4️⃣ Program: Two sets & common elements
set1 = set(map(int, input("Enter integers for set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for set 2 separated by spaces: ").split()))
common_set = set1 & set2
print("Common elements in both sets:", common_set)

print("-" * 40)

# 5️⃣ Program: Words with odd number of characters
words = ["python", "code", "learning", "AI", "loop", "tuple"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
