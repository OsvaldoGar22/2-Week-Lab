# Exercise 1 - Personal Information
# name = "Cameron Calero"
# address = "123 Good Street 12345 CA"
# phone_number = "(123)112-4455"
# major = "Cybersecurity"

# print(f"{name}", f"{address}", f"{phone_number}", f"{major}", sep="\n")

# -------------------------------------------------------------------------------


# Exercise 2 - Sales Prediction
# annual_profit = 0.23

# projected_total_sales = float(input("What is the companies projected sales? "))
# profit = projected_total_sales * 0.23
# print(f"Your company total profit is: ${profit:.2f}")

# -------------------------------------------------------------------------------

# Exercise 3 - Land Calculation
# total_square_feet = int(input("Enter the total square feet: "))
# acres = total_square_feet / 43560
# print(f"The number of acres is {int(acres)}")

# -------------------------------------------------------------------------------

# Exercise 4 - Total Purchase

# price1 = float(input("What is the price for the first item: "))
# price2 = float(input("What is the price for the second item: "))
# price3 = float(input("What is the price for the third item: "))
# price4 = float(input("What is the price for the fourth item: "))
# price5 = float(input("What is the price for the fifth item: "))
#
# subtotal = price1 + price2 + price3 + price4 + price5
# print(f"Subtotal: ${subtotal:.2f}")
# sales_tax = subtotal * 0.07
# print(f"Sales Tax: ${sales_tax:.2f}")
# total = subtotal + sales_tax
# print(f"Total: ${total:.2f}")

# -------------------------------------------------------------------------------

# Exercise 5 - Distance Traveled
# distance_traveled = 6
#
# formula = 70 * distance_traveled
# print(f"The distance traveled in 6 hours is: {formula}")
#
# distance_traveled = 10
#
# formula = 70 * distance_traveled
# print(f"The distance traveled in 10 hours is: {formula}")
#
#
# distance_traveled = 15
#
# formula = 70 * distance_traveled
# print(f"The distance traveled in 15 hours is: {formula}")

# -------------------------------------------------------------------------------

# Exercise 6 - Sales Tax

# price = float(input("How much does the item cost? $"))
#
# sales_tax = price * 0.05
# county_sales_tax = price * 0.025
# total = price + sales_tax + county_sales_tax
#
# print(f"Total: ${total:.2f}")

# -------------------------------------------------------------------------------

# Exercise 7 - Miles-per-Gallon
# miles_driven = int(input("How many miles were driven? "))
# gallons_used = int(input("How many gallons of gas did you use? "))
#
# miles_per_gallon = miles_driven / gallons_used
#
# print(f"Your car's MPG is: {miles_per_gallon:.2f}")

# -------------------------------------------------------------------------------

# Exercise 8 - Tip, tax, and Total

# meal_price = float(input("How much did the meal cost? $"))
#
# tip = meal_price * 0.18
# sales_tax = meal_price * 0.07
# total = meal_price + tip + sales_tax
# print(f"Total: ${total:.2f}")

# -------------------------------------------------------------------------------

# Exercise 9 - Celsius to Fahrenheit Temperature Converter
# temp = int(input("What is the Temperature (Celsius)? "))
#
# celsius_temp = (9 / 5) * temp + 32
# print(f"The Temperature in Fahrenheit is: {celsius_temp}")

# -------------------------------------------------------------------------------

# Exercise 10 - Ingredient Adjuster

# amount_cookies = float(input("How many cookies do you want to make? "))
#
# cookie_adjustment = amount_cookies / 48
# sugar_adjustment = 1.5 * cookie_adjustment
# butter_adjustment= 1 * cookie_adjustment
# flour_adjustment = 2.75 * cookie_adjustment
#
# print(f"The amount of cookies wanted: {amount_cookies:.0f}")
# print(f"{sugar_adjustment:.2f} cups of sugar")
# print(f"{butter_adjustment:.2f} cups of butter")
# print(f"{flour_adjustment:.2f} cups of flour")

# -------------------------------------------------------------------------------

# Exercise 11 - Lion and tiger Percentages

# lions = float(input("How many Lions are in the exhibit? "))
# tigers = float(input("How many Tigers are in the exhibit? "))
#
# amount_big_cats = lions + tigers
# lions_percentage = lions / amount_big_cats * 100
# tigers_percentage = tigers / amount_big_cats * 100
#
# print(f"There are a total of {amount_big_cats:.0f} cats in the Big Cat Exhibit")
# print(f"{lions_percentage:.2f}% of the Big Cats are Lions: {lions:.0f}")
# print(f"{tigers_percentage:.2f}% of the Big Cats are Tigers: {tigers:.0f}")

# -------------------------------------------------------------------------------

# Exercise 12 - Stock transaction program
# number_of_shares = 2000
# price_per_share = 40.00
# stock_cost = number_of_shares * price_per_share
# commission = 0.03 * stock_cost
# total_cost = number_of_shares * price_per_share + commission
# print(
#    f"Joe paid ${total_cost:.2f} for {number_of_shares} Shares at the price of ${price_per_share:.2f} with a commission of {0.03 * 100:.2f}%."
# )
#
# sold_price_per_share = 42.75
# sold_stock_cost = number_of_shares * sold_price_per_share
# sold_commission = 0.03 * sold_stock_cost
# sold_total_cost = number_of_shares * sold_price_per_share + sold_commission
# print(
#    f"Joe sold his {number_of_shares} shares for a total of ${sold_total_cost:.2f} at the price of ${sold_price_per_share:.2f} with a commission of {0.03 * 100:.2f}%."
# )
#
# print(f"He made a total profit of ${sold_total_cost - total_cost:.2f}")

# -------------------------------------------------------------------------------

# Exercise 13 - Planting Grapevines

# length = int(input("What is the length of the row, in feet: "))
# space_needed = int(
#    input("What is the amount of space used by and end-post assembly, in feet: ")
# )
# space_between = int(input("What is the amount of space between the vines, in feet: "))
#
# grapevines = length - (2 * space_needed) / space_between
#
# print(f"The amount of grapevines that will fit is {grapevines}")

# -------------------------------------------------------------------------------

# Exercise 14 - Compound Interest

principal_amount = float(
    input("What is the amount of principal originally deposited into the account: $")
)
annual_interest_rate = float(
    input("What is the annual interest rate paid by the account: ")
)
times_per_year_compounded = float(
    input("What is the number of times per year that the interest is compounded: ")
)
number_of_years = int(
    input("What is the number of years the account will be left to earn interest: ")
)

interest_rate_percentage = annual_interest_rate / 100

amount_of_money = principal_amount * (
    1 + interest_rate_percentage / times_per_year_compounded
) ** (times_per_year_compounded * number_of_years)

print(
    f"The total amount of money after {number_of_years} years will be ${amount_of_money:.2f}"
)
