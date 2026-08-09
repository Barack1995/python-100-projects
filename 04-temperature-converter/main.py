def temperature_convertor(temp, conversion):
    if conversion == 'C':
        return  (temp*9/5) + 32
    elif conversion == 'F':
        return (temp-32) * 5/9

    
while True:
    try:
        temperature = float(input("Enter the temperature: "))
        conversion = input("Enter conversion (C/F): ").upper()
        if conversion not in ['C','F']:
            print("Error: Invalid conversion. Please enter one of C,F")
            continue
        result = temperature_convertor(temperature,conversion)
        print("Result:", round(result,2))
        break

    except ValueError:
        print("Error: Please enter valid integers for temperature.")




