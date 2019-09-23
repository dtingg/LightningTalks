"""
Final Project
Python 3 - Horoscope Program
Enter your name, birth month, and birth day to see your daily horoscope from The Seattle Times
If you have used this program before, it will remember your data
"""

# Import modules
import datetime
import requests
from bs4 import BeautifulSoup

# Define global variables
birth_month = ""
birth_day = 0
sign = ""

# Figure out what the current month and current day are
now = datetime.datetime.now()
month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}
current_month = month_dict[now.month]
current_day = now.day

# Pull in data for previous players with signs.txt.
previous_data = []

with open("signs.txt", "r") as f:
    for line in f:
        line = line.strip()
        parts = line.split(", ")
        previous_data.append(parts)

# Introduce the program
print("Welcome to Dianna Tingg's Daily Horoscope Program!")

# Ask the user for their name:
name = input("\nWhat is your name? ").title()
while name == "":
    name = input("Error. Please enter your name: ").title()

# Check to see if the person has played before
previous_users = ""

for x in previous_data:
    if x[0] == name:
        previous_users = x[0]
        birth_month = x[1]
        birth_day = int(x[2])
        sign = x[3]

# Ask the user for their birth month
if birth_month == "":
    birth_month = input("What month were you born? (January, February, etc) ").title()
    while birth_month not in month_dict.values():
        birth_month = input("Error. Please enter the full name of a month: ").title()

# Ask the user for their birth day
if birth_day == 0:
    birth_day = int(input("What day were you born? (1, 2, etc) "))
    while birth_day not in range(1, 32):
        birth_day = int(input("Error. Please enter a number (1-31): "))


# Figure out what the user's sign is based on their birth month and birth day
def get_sign(birth_month, birth_day):
    if birth_month == "January":
        if birth_day <= 19:
            sign = "Capricorn"
        else:
            sign = "Aquarius"

    elif birth_month == "February":
        if birth_day <= 18:
            sign = "Aquarius"
        else:
            sign = "Pisces"

    elif birth_month == "March":
        if birth_day <= 20:
            sign = "Pisces"
        else:
            sign = "Aries"

    elif birth_month == "April":
        if birth_day <= 19:
            sign = "Aries"
        else:
            sign = "Taurus"

    elif birth_month == "May":
        if birth_day <= 20:
            sign = "Taurus"
        else:
            sign = "Gemini"

    elif birth_month == "June":
        if birth_day <= 20:
            sign = "Gemini"
        else:
            sign = "Cancer"

    elif birth_month == "July":
        if birth_day <= 22:
            sign = "Cancer"
        else:
            sign = "Leo"

    elif birth_month == "August":
        if birth_day <= 22:
            sign = "Leo"
        else:
            sign = "Virgo"

    elif birth_month == "September":
        if birth_day <= 22:
            sign = "Virgo"
        else:
            sign = "Libra"

    elif birth_month == "October":
        if birth_day <= 22:
            sign = "Libra"
        else:
            sign = "Scorpio"

    elif birth_month == "November":
        if birth_day <= 21:
            sign = "Scorpio"
        else:
            sign = "Sagittarius"

    elif birth_month == "December":
        if birth_day <= 21:
            sign = "Sagittarius"
        else:
            sign = "Capricorn"
    return sign


if sign == "":
    sign = get_sign(birth_month, birth_day)

# Repeat the information to the user and tell them what their sign is
print("\nHi {}! Your birthday is {} {}. Your astrological sign is {}.".format(name, birth_month, birth_day, sign))

# Check if today is the user's birthday
birthday = (birth_month == current_month and birth_day == current_day)

# Set up horoscope url as a string
url = "https://www.seattletimes.com/horoscopes/"

# Pull down all the html and store it in a page variable
response = requests.get(url)
content = response.content

# Convert content to beautiful soup format
soup = BeautifulSoup(content, "html.parser")

# For Today's Birthday horoscope
if birthday == True:
    soup = str(soup.find_all("div", {"class": "birthday"}))
    horoscope = soup.split("</span>")
    horoscope = horoscope[1].split("</p>")
    horoscope = horoscope[0]
    print("Today is {} {}. Happy Birthday!".format(current_month, current_day))

# For other horoscopes, isolate section and convert to a string
else:
    soup = str(soup.find_all("div", {"class": "horoscopes"}))
    soup = soup.split("<strong>")

# Iterate over list to find the correct horoscope
    for line in soup:
        if line.startswith(sign):
            line = line.split("</span>")
            horoscope = line[1]

# Print the user's horoscope
print("\nHere is your daily horoscope from The Seattle Times: \n{}".format(horoscope))

# Save user to signs.txt
if name != previous_users:
    with open('signs.txt', 'a') as f:
        x = ", "
        data = (name, birth_month, str(birth_day), sign)
        f.write(x.join(data))
        f.write("\n")
