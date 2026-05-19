def binary_to_intel_hex(binary_lines):
    intel_hex = []
    address = 0
    for i in range(0, len(binary_lines), 16):
        # Grab 16 lines at a time
        chunk = binary_lines[i:i + 16]
        byte_count = len(chunk)
        
        # Convert each binary string to integer, then to hex
        data = [int(line, 2) for line in chunk]
        
        # Build the Intel HEX line
        record_type = 0x00
        record = [byte_count, (address >> 8) & 0xFF, address & 0xFF, record_type] + data
        checksum = (-(sum(record) & 0xFF)) & 0xFF  # Two's complement
        
        # Format the record
        hex_line = ":{:02X}{:04X}{:02X}".format(byte_count, address, record_type)
        hex_line += "".join("{:02X}".format(b) for b in data)
        hex_line += "{:02X}".format(checksum)
        intel_hex.append(hex_line)
        
        # Increment address by the byte count
        address += byte_count
    
    # Append the End of File record
    intel_hex.append(":00000001FF")
    
    return "\n".join(intel_hex)

# Example usage:
binary_lines = """00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111
00000000
00000001
00000010
00000011
00000100
00000101
00000110
00000111""".splitlines()

result = binary_to_intel_hex(binary_lines)
print(result)