"""Example of how Python file.seek works

$ py seek.py
b'fghijklmno'
b'abcdefghijklmnoNew dataxyz\nABCDEFGHIJKLMNOPQRSTUVWXYZ\n'

before
```
abcdefghijklmnoNew dataxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
after
```
abcdefghijklmnoNew dataxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```
"""

with open("example.bin", "rb+") as file:
    # Move the file pointer to the 5th byte
    file.seek(5)

    # Read 10 bytes from the file
    data = file.read(10)
    print(data)

    # Write new data to the file
    file.write(b"New data")

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Read the entire file
    data = file.read()
    print(data)
