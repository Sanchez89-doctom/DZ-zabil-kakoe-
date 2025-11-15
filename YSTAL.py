try:
    user_input = input("Введіть число ")
    number = int(user_input)
    print("Число", number)
except ValueError:
    print("Помилка404, не можна перетворити на ціле число")
