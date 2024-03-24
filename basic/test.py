
import re
symbol = "!"
string = "Hello World!呵呵呵"

binary = string.encode('gbk')
print(binary)


string1 = binary.decode('gbk')
print(string1)