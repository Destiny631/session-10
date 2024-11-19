# Problem 1: Forecast next month's sales based on the month and sales
def forecast_sales(month, sales):
    forecast_percent = 0
    if month in ['Jan', 'Feb', 'Mar']:
        forecast_percent = 0.10
    elif month in ['Apr', 'May', 'Jun']:
        forecast_percent = 0.15
    elif month in ['Jul', 'Aug', 'Sep']:
        forecast_percent = 0.20
    elif month in ['Oct', 'Nov', 'Dec']:
        forecast_percent = 0.25

    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales

# Problem 2: Compute square footage of a room and gallons of paint needed
def compute_paint_gallons(length, width, height):
    square_footage = 2 * length * width + 2 * length * height + 2 * width * height
    gallons_needed = square_footage / 50
    return gallons_needed

# Problem 3: Compute the out-the-door price of an automobile based on discounts and taxes
def compute_out_the_door_price(msrp, make, model, is_electric):
    discount_percent = 0
    if make == "Honda" and model == "Accord":
        discount_percent = 0.10
    elif make == "Toyota" and model == "Rav4":
        discount_percent = 0.15
    elif is_electric == "Y":
        discount_percent = 0.30
    else:
        discount_percent = 0.05

    discounted_price = msrp * (1 - discount_percent)
    sales_tax = discounted_price * 0.07
    total_price = discounted_price + sales_tax
    return total_price

# Problem 4: Compute the train ticket price based on distance from downtown Chicago
def compute_train_ticket_price(miles):
    if miles >= 30:
        ticket_price = 12
    elif miles >= 20:
        ticket_price = 10
    elif miles >= 10:
        ticket_price = 8
    else:
        ticket_price = 5
    return ticket_price

# Problem 5: Compute the assessed value of a home based on market value and county
def compute_assessed_value(county, market_value):
    assessed_value_percent = 0
    if county == "Cook":
        assessed_value_percent = 0.90
    elif county == "DuPage":
        assessed_value_percent = 0.80
    elif county == "McHenry":
        assessed_value_percent = 0.75
    elif county == "Kane":
        assessed_value_percent = 0.60
    else:
        assessed_value_percent = 0.70

    assessed_value = market_value * assessed_value_percent
    return assessed_value

# Main function to handle repeated user input for all problems
def main():
    total_msrp = 0
    total_sales_price = 0
    total_market_value = 0
    total_assessed_value = 0
    total_ticket_price = 0

    # Problem 1
    while input("Do you want to continue with the sales forecast program? (Yes/No): ").strip().lower() == "yes":
        last_name = input("Enter your last name: ")
        month = input("Enter the month: ")
        sales = float(input("Enter your sales for the month: "))
        next_month_sales = forecast_sales(month, sales)
        print(f"Next month's forecasted sales for {last_name}: {next_month_sales:.2f}")

    # Problem 2
    while input("Do you want to continue with the paint calculation program? (Yes/No): ").strip().lower() == "yes":
        length = float(input("Enter the length of the room: "))
        width = float(input("Enter the width of the room: "))
        height = float(input("Enter the height of the room: "))
        gallons_needed = compute_paint_gallons(length, width, height)
        print(f"Gallons of paint needed: {gallons_needed:.2f}")

    # Problem 3
    while input("Do you want to continue with the car price calculation program? (Yes/No): ").strip().lower() == "yes":
        make = input("Enter the car make: ")
        model = input("Enter the car model: ")
        electric = input("Is it an electric vehicle? (Y/N): ").strip().upper()
        msrp = float(input("Enter the MSRP (sticker price) of the car: "))
        out_the_door_price = compute_out_the_door_price(msrp, make, model, electric)
        print(f"Out the door price for {make} {model}: ${out_the_door_price:.2f}")
        total_msrp += msrp
        total_sales_price += out_the_door_price

    # Problem 4
    while input("Do you want to continue with the train ticket program? (Yes/No): ").strip().lower() == "yes":
        last_name = input("Enter your last name: ")
        miles = float(input("Enter miles from downtown Chicago: "))
        ticket_price = compute_train_ticket_price(miles)
        print(f"Ticket price for {last_name}: ${ticket_price:.2f}")
        total_ticket_price += ticket_price

    # Problem 5
    while input("Do you want to continue with the home assessment program? (Yes/No): ").strip().lower() == "yes":
        county = input("Enter the county: ")
        market_value = float(input("Enter the market value of the home: "))
        assessed_value = compute_assessed_value(county, market_value)
        print(f"Assessed value for the home: ${assessed_value:.2f}")
        total_market_value += market_value
        total_assessed_value += assessed_value

    # Final totals display
    print("\nSummary of totals:")
    print(f"Total MSRP of cars: ${total_msrp:.2f}")
    print(f"Total sales price of cars: ${total_sales_price:.2f}")
    print(f"Total ticket price: ${total_ticket_price:.2f}")
    print(f"Total market value of homes: ${total_market_value:.2f}")
    print(f"Total assessed value of homes: ${total_assessed_value:.2f}")

# Run the program
if __name__ == "__main__":
    main()
