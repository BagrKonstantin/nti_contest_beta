# This is a sample Python script.
import sqlite3

con = sqlite3.connect("bd.db")
cur = con.cursor()
a = cur.execute("""SELECT * FROM products""")
print(a)
print("1с говнbot dfgdfgdfafgdfgsdfgg")

# ёбаные одинэсеры, я перебью ваши семьи, друзей, собак, кошек, рыбок ваших нахуй


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
