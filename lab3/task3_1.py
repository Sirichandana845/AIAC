def calculate_power_bill(units):
    """
    Calculate the power bill based on the number of units consumed.
    Example slab:
        - First 100 units: Rs. 5 per unit
        - Next 100 units (101-200): Rs. 7 per unit
        - Above 200 units: Rs. 10 per unit
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

def main():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units != int(units):
            print("Warning: Units should be an integer. Rounding down.")
        units = int(units)
        total_bill = calculate_power_bill(units)
        print(f"Total power bill for {units} units: Rs. {total_bill}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
