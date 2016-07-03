def format_to_two_bytes(val):
	binformat = bin(val & 0b1111111111111111)
	hexformat = hex(int(binformat, 2))
	print hexformat
	firstbyte, secondbyte = divmod(int(hexformat,16), 0x100)
	return str(firstbyte) + ' ' + str(secondbyte)
	
print format_to_two_bytes(1)