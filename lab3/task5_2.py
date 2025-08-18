def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float or int): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Raises:
        TypeError: If input is not a number.
    """
    # Validate input type
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a numeric value.")
    
    # Perform conversion
    return celsius * 9/5 + 32

# Example usage
celsius = 100
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
