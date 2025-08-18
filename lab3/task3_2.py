def calculate_electricity_bill(kwh_used, rate_per_kwh):
    """
    Calculate the monthly electricity bill.

    Args:
        kwh_used (float): Total kilowatt-hours used in the month.
        rate_per_kwh (float): Fixed rate per kilowatt-hour.

    Returns:
        float: Total bill amount.
    """
    if kwh_used < 0:
        raise ValueError("kWh used cannot be negative.")
    if rate_per_kwh < 0:
        raise ValueError("Rate per kWh cannot be negative.")
    return kwh_used * rate_per_kwh

def main():
    try:
        kwh = float(input("Enter total kWh used this month: "))
        rate = float(input("Enter fixed rate per kWh (in Rs.): "))
        total_bill = calculate_electricity_bill(kwh, rate)
        print(f"Total electricity bill: Rs. {total_bill:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
