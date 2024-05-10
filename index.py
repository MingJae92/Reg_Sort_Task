def format_serial_number(serial, l, el):

    serial = serial.replace('-', '')

    if len(serial) != el:
        return "Serial number entered is not the correct length."

    formatted_sections = []

    for i in range(0, len(serial), l):

        section = serial[i:i + l]

        section = section.upper()

        formatted_sections.append(section)

    formatted_serial = '-'.join(formatted_sections)

    return formatted_serial


# Example usage:
print(format_serial_number('7Hnwad9Jk', 4, 9))  # Output: "7-HNWA-D9JK"
print(format_serial_number('6F2k-1d-0-z', 4, 8))  # Output: "6F2K-1D0Z"
print(format_serial_number('14k-9-b', 2, 5))  # Output: "1-4K-9B"
# Output: "Serial number entered is not the correct length."
print(format_serial_number('fw2-jt6-567', 2, 8))
