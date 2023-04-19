# buffer-pool

```py
from collections import OrderedDict

# Creating an OrderedDict
od = OrderedDict()

# Adding elements to the OrderedDict
od['apple'] = 3
od['banana'] = 1
od['orange'] = 2

# Accessing elements
print(od['apple'])  # Output: 3

# Iterating through the OrderedDict
for key, value in od.items():
    print(key, value)
# Output:
# apple 3
# banana 1
# orange 2

# Updating an existing element (moves the element to the end of the OrderedDict)
od['banana'] = 4

# Displaying the updated OrderedDict
for key, value in od.items():
    print(key, value)
# Output:
# apple 3
# orange 2
# banana 4

# Removing the least recently used (LRU) element (the first element)
od.popitem(last=False)  # Output: ('apple', 3)

# Displaying the updated OrderedDict after removing the LRU element
for key, value in od.items():
    print(key, value)
# Output:
# orange 2
# banana 4
```

---

Here's a cool explanation of struct in Python:

Import the module:

```py
import struct
```
Format Strings:

Format strings are used to define the data layout in bytes. Some common format codes are:
- 'b': signed char (1 byte)
- 'B': unsigned char (1 byte)
- 'h': short (2 bytes)
- 'H': unsigned short (2 bytes)
- 'i': int (4 bytes)
- 'I': unsigned int (4 bytes)
- 'f': float (4 bytes)
- 'd': double (8 bytes)

You can specify the endianness (byte order) with the following characters:

- '<': little-endian
- '>': big-endian
- '=': native byte order
- '!': network byte order (big-endian)


Packing Data:


Use struct.pack() to convert Python data types into a binary string.

Example:

```py
data = (1, 2, 3.14)
binary_data = struct.pack('<Ihf', *data)
```

Here, the format string `'<Ihf'` indicates little-endian, unsigned int, short, and float. The *data is used to unpack the tuple, so the function takes the values in the tuple as individual arguments.

Unpacking Data:
Use struct.unpack() to convert a binary string back to Python data types.

Example:

```py
binary_data = b'\x01\x00\x00\x00\x02\x00\xc3\xf5H@'
data = struct.unpack('<Ihf', binary_data)
print(data)  # Output: (1, 2, 3.140000104904175)
```

Calculating Struct Size:

struct.calcsize() gives you the size of the binary string based on the format string.


Example:

```python
size = struct.calcsize('<Ihf')
print(size)  # Output: 10
```
And that's the struct module in Python! It's super useful when you need to work with binary data or need a specific data layout for communication with other systems.

---

Import the module:

```py
import struct
```

Format Strings:

Format strings are used to define the data layout in bytes. Some common format codes are:
- 'b': signed char (1 byte)
- 'B': unsigned char (1 byte)
- 'h': short (2 bytes)
- 'H': unsigned short (2 bytes)
- 'i': int (4 bytes)
- 'I': unsigned int (4 bytes)
- 'f': float (4 bytes)
- 'd': double (8 bytes)

You can specify the endianness (byte order) with the following characters:
- '<': little-endian
- '>': big-endian
- '=': native byte order
- '!': network byte order (big-endian)

Packing Data:

Use struct.pack() to convert Python data types into a binary string.

Example:
```py
data = (1, 2, 3.14)
binary_data = struct.pack('<Ihf', *data)
```

Here, the format string '<Ihf' indicates little-endian, unsigned int, short, and float. The *data is used to unpack the tuple, so the function takes the values in the tuple as individual arguments.

Unpacking Data:

Use struct.unpack() to convert a binary string back to Python data types.

Example:
```py
binary_data = b'\x01\x00\x00\x00\x02\x00\xc3\xf5H@'
data = struct.unpack('<Ihf', binary_data)
print(data)  # Output: (1, 2, 3.140000104904175)
```

Calculating Struct Size:

struct.calcsize() gives you the size of the binary string based on the format string.

Example:
```py
size = struct.calcsize('<Ihf')
print(size)  # Output: 10
```

And that's the struct module in Python! It's super useful when you need to work with binary data or need a specific data layout for communication with other systems.

---

These symbols are used as format characters in Python's struct module to specify the byte order when packing or unpacking binary data. The byte order determines the order in which a sequence of bytes is stored in memory.

Here's a brief explanation of each format character:

<: little-endian
- The least significant byte (LSB) is stored first, followed by the other bytes in increasing significance.
- For example, when storing the 32-bit integer 0x12345678, it would be stored as 0x78 0x56 0x34 0x12.
- Little-endian is the default byte order for Intel (x86 and x86-64) and ARM processors.

`>:` big-endian
- The most significant byte (MSB) is stored first, followed by the other bytes in decreasing significance.
- For example, when storing the 32-bit integer 0x12345678, it would be stored as 0x12 0x34 0x56 0x78.
- Big-endian is the default byte order for PowerPC, SPARC, and MIPS processors.

=: native byte order
- Uses the byte order of the system on which the Python interpreter is running.
- If the system is little-endian, it will use little-endian byte order; if the system is big-endian, it will use big-endian byte order.

!: network byte order (big-endian)
- This is an alias for big-endian byte order.
- When transmitting data over a network, it's common to use network byte order (big-endian) to ensure consistency between different systems.

These format characters are used at the beginning of the format string in struct.pack and struct.unpack functions to specify the byte order of the data being packed or unpacked. For example:

import struct

# Packing an integer in little-endian byte order
```py
packed_data = struct.pack('<I', 0x12345678)
print(packed_data)  # Output: b'\x78\x56\x34\x12'
```
# Unpacking an integer in big-endian byte order
```py
unpacked_data = struct.unpack('>I', b'\x12\x34\x56\x78')
print(unpacked_data[0])  # Output: 305419896 (0x12345678 in decimal)
```
