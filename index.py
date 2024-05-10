def format_serial_number(serial, l, el):
    # Remove any hyphens from input serial number entered by user
    serial = serial.replace('-', '')

    # Check if the length of the input serial number matches the expected length
    if len(serial) != el:
        return "Serial number entered is not the correct length."

    # We have an empty list declared to store formatted sections of the serial number
    formatted_sections = []

    # Loop through the serial number and group it into sections of length l
    for i in range(0, len(serial), l):
        # Get an index of the serial number and plus 1
        section = serial[i:i + l]

        # Convert the section to uppercase
        section = section.upper()

        # Append the formatted section to the list
        formatted_sections.append(section)

    # Join the sections with dashes to create the formatted serial number
    formatted_serial = '-'.join(formatted_sections)

    return formatted_serial


# Example usage:
print(format_serial_number('7Hnwad9Jk', 4, 9))  # Output: "7-HNWA-D9JK"
print(format_serial_number('6F2k-1d-0-z', 4, 8))  # Output: "6F2K-1D0Z"
print(format_serial_number('14k-9-b', 2, 5))  # Output: "1-4K-9B"
# Output: "Serial number entered is not the correct length."
print(format_serial_number('fw2-jt6-567', 2, 8))
